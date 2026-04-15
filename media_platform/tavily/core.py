# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/media_platform/tavily/core.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1

from typing import List, Dict, Any
import asyncio

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
    
    async def start(self):
        """开始爬取"""
        print(f"[Tavily] 开始搜索关键词: {self.keywords}")
        print(f"[Tavily] 时间范围: {self.time_range}")
        print(f"[Tavily] 包含域名: {self.include_domains}")
        
        try:
            # 动态导入 tavily 库
            from tavily import TavilyClient
            
            # 初始化客户端
            client = TavilyClient(self.api_key)
            
            # 构建搜索参数
            search_params = {
                "query": self.keywords,
                "search_depth": self.search_depth,
                "max_results": self.max_results,
                "chunks_per_source": self.chunks_per_source,
                "include_domains": self.include_domains
            }
            
            # 添加时间范围参数（如果有）
            if self.time_range:
                search_params["time_range"] = self.time_range
            
            # 执行搜索
            response = client.search(**search_params)
            
            # 处理搜索结果
            await self._process_search_results(response)
            
            print(f"[Tavily] 搜索完成，共获取 {len(response.get('results', []))} 个结果")
            
        except ImportError:
            print("[Tavily] 错误: 未安装 tavily-python 库，请运行 'pip install tavily-python'")
        except Exception as e:
            print(f"[Tavily] 搜索过程中出错: {str(e)}")
    
    async def _process_search_results(self, response: Dict[str, Any]):
        """处理搜索结果"""
        results = response.get('results', [])
        
        for i, result in enumerate(results):
            # 构建标准化的数据结构
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
                "create_time": "",  # Tavily API 不返回创建时间
                "author": "",  # Tavily API 不返回作者信息
                "view_count": 0,  # Tavily API 不返回浏览量
                "like_count": 0,  # Tavily API 不返回点赞数
                "comment_count": 0,  # Tavily API 不返回评论数
                "share_count": 0,  # Tavily API 不返回分享数
                "comments": [],  # Tavily API 不返回评论
                "sub_comments": []  # Tavily API 不返回子评论
            }
            
            # 保存数据
            import config
            if config.SAVE_DATA_OPTION == "csv":
                await self.file_writer.write_to_csv(item, "content")
            elif config.SAVE_DATA_OPTION == "jsonl":
                await self.file_writer.write_to_jsonl(item, "content")
            elif config.SAVE_DATA_OPTION == "json":
                await self.file_writer.write_single_item_to_json(item, "content")
            else:
                # 默认使用 jsonl
                await self.file_writer.write_to_jsonl(item, "content")
    
    async def search(self):
        """搜索关键词"""
        # 这里可以实现更灵活的搜索方法
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
