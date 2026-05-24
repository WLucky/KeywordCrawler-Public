# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/media_platform/tavily/core.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1

from typing import List, Dict, Any
import asyncio
import json
import os
import pathlib
import aiofiles
import httpx

from base.base_crawler import AbstractCrawler
from config import (
    PLATFORM, KEYWORDS, TAVILY_API_KEY, SEARCH_DEPTH, MAX_RESULTS,
    CHUNKS_PER_SOURCE, INCLUDE_DOMAINS, CURRENT_TIME_RANGE
)
from tools.async_file_writer import AsyncFileWriter


class TavilyCrawler(AbstractCrawler):
    def __init__(self):
        super().__init__()
        self.platform = PLATFORM
        self.keywords = KEYWORDS
        self.api_key = TAVILY_API_KEY
        self.search_depth = SEARCH_DEPTH
        self.max_results = MAX_RESULTS
        self.chunks_per_source = CHUNKS_PER_SOURCE
        self.include_domains = INCLUDE_DOMAINS
        self.time_range = CURRENT_TIME_RANGE
        self.file_writer = AsyncFileWriter(
            platform=self.platform,
            crawler_type="search",
        )
        self.image_store_path = "data/images"
        self.image_config = []
    
    async def start(self):
        """开始爬取"""
        print(f"[Tavily] 开始搜索关键词: {self.keywords}")
        print(f"[Tavily] 时间范围: {self.time_range}")
        print(f"[Tavily] 包含域名: {self.include_domains}")
        
        try:
            from tavily import TavilyClient
            
            client = TavilyClient(self.api_key)
            
            search_params = {
                "query": self.keywords,
                "search_depth": self.search_depth,
                "max_results": self.max_results,
                "chunks_per_source": self.chunks_per_source,
                "include_domains": self.include_domains,
                "include_images": True  # 必须显式启用图片搜索
            }
            
            if self.time_range:
                search_params["time_range"] = self.time_range
            
            response = client.search(**search_params)
            
            await self._process_search_results(response)
            
            print(f"[Tavily] 搜索完成，共获取 {len(response.get('results', []))} 个结果")
            
            # 动态读取配置（确保使用最新修改的配置值）
            import config
            enable_img = getattr(config, 'ENABLE_TAVILY_IMG', False)
            max_images = getattr(config, 'MAX_IMAGES_PER_RESULT', 3)
            
            if enable_img:
                print(f"[Tavily] 图片下载已启用，将下载图片...")
                await self._download_images(response, max_images)
                
                if self.image_config:
                    await self._save_image_config()
                    await self._update_markdown_with_images()
            else:
                print(f"[Tavily] 图片下载已禁用")
            
        except ImportError:
            print("[Tavily] 错误: 未安装 tavily-python 库，请运行 'pip install tavily-python'")
        except Exception as e:
            print(f"[Tavily] 搜索过程中出错: {str(e)}")
    
    async def _process_search_results(self, response: Dict[str, Any]):
        """处理搜索结果"""
        results = response.get('results', [])
        
        for i, result in enumerate(results):
            item = {
                "platform": self.platform,
                "keyword": self.keywords,
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "content": result.get("content", ""),
                "score": result.get("score", 0),
                "published_date": result.get("published_date", ""),
                "images": result.get("images", []),
                "chunks": result.get("chunks", []),
                "id": f"tavily_{i+1}",
                "create_time": "",
                "author": "",
                "view_count": 0,
                "like_count": 0,
                "comment_count": 0,
                "share_count": 0,
                "comments": [],
                "sub_comments": []
            }
            
            import config
            if config.SAVE_DATA_OPTION == "csv":
                await self.file_writer.write_to_csv(item, "contents")
            elif config.SAVE_DATA_OPTION == "jsonl":
                await self.file_writer.write_to_jsonl(item, "contents")
            elif config.SAVE_DATA_OPTION == "json":
                await self.file_writer.write_single_item_to_json(item, "contents")
            else:
                await self.file_writer.write_to_jsonl(item, "contents")
    
    async def _download_images(self, response: Dict[str, Any], max_images_per_result: int = 3):
        """下载搜索结果中的图片"""
        # Tavily API 的图片在顶层的 images 字段中，而不是在每个 result 里
        top_level_images = response.get('images', [])
        results = response.get('results', [])
        pathlib.Path(self.image_store_path).mkdir(parents=True, exist_ok=True)
        
        print(f"[Tavily] 发现 {len(top_level_images)} 张顶层图片")
        
        # 下载顶层图片
        for img_idx, img_url in enumerate(top_level_images[:max_images_per_result]):
            try:
                async with httpx.AsyncClient() as client:
                    img_response = await client.get(img_url, timeout=30)
                    img_response.raise_for_status()
                    
                    ext = self._get_file_extension(img_url)
                    filename = f"image_{img_idx + 1}{ext}"
                    filepath = os.path.join(self.image_store_path, filename)
                    
                    async with aiofiles.open(filepath, 'wb') as f:
                        await f.write(img_response.content)
                    
                    # 尝试找到相关的搜索结果作为来源信息
                    source_title = ""
                    source_url = ""
                    source_content = ""
                    if results:
                        source_title = results[0].get("title", "")
                        source_url = results[0].get("url", "")
                        source_content = results[0].get("content", "")[:100]  # 内容摘要
                    
                    # 构建更丰富的描述
                    description = f"关键词 '{self.keywords}' 相关图片"
                    if source_title:
                        description = f"{source_title[:50]}... - {description}"
                    if source_content:
                        description = f"{description} | 内容摘要: {source_content}..."
                    
                    self.image_config.append({
                        "filename": filename,
                        "url": img_url,
                        "source_title": source_title,
                        "source_url": source_url,
                        "source_content": source_content,
                        "description": description,
                        "download_time": self._get_current_time()
                    })
                    
                    print(f"[Tavily] 下载图片: {filepath}")
                    
            except Exception as e:
                    print(f"[Tavily] 下载图片失败 {img_url}: {str(e)}")
    
    def _get_file_extension(self, url: str) -> str:
        """从URL获取文件扩展名"""
        import urllib.parse
        parsed = urllib.parse.urlparse(url)
        path = parsed.path
        
        # 获取扩展名，处理类似 .png!jpg 的情况
        ext = os.path.splitext(path)[1]
        
        # 如果扩展名包含特殊字符（如 !），只取第一个有效扩展名
        if ext:
            # 找到第一个有效扩展名的位置
            valid_ext_start = ext.find('.')
            if valid_ext_start != -1:
                ext = ext[valid_ext_start:].split('!')[0].split('?')[0]
        
        if not ext or len(ext) > 10:
            ext = ".jpg"
        return ext
    
    def _get_current_time(self) -> str:
        """获取当前时间字符串"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    async def _save_image_config(self):
        """保存图片配置文件"""
        config_path = os.path.join(self.image_store_path, "image_config.json")
        async with aiofiles.open(config_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(self.image_config, ensure_ascii=False, indent=4))
        print(f"[Tavily] 图片配置文件已保存: {config_path}")
    
    async def _update_markdown_with_images(self):
        """图片信息将在run_crawler.py中统一合并到视频下载链接markdown文件"""
        # 图片信息不需要单独生成markdown文件，由run_crawler.py的add_images_to_markdown函数统一处理
        if self.image_config:
            print(f"[Tavily] 图片配置已保存，将由run_crawler.py统一合并到视频下载链接markdown文件")
        pass
    
    async def search(self):
        """搜索关键词"""
        pass
    
    async def launch_browser(self, chromium, playwright_proxy=None, user_agent=None, headless=True):
        """启动浏览器（Tavily API 不需要浏览器）"""
        return None
    
    async def get_comments(self, item_id: str, **kwargs):
        """获取评论（Tavily API 不支持评论获取）"""
        pass
    
    async def get_sub_comments(self, comment_id: str, **kwargs):
        """获取子评论（Tavily API 不支持子评论获取）"""
        pass