#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
import os
import json
from pathlib import Path
from datetime import datetime

# 确保所有 print 语句实时刷新
class Unbuffered:
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def update_config(platform, keywords, time_type=0, max_notes=15, max_comments=10, enable_sub_comments=False, enable_tavily_img=False, max_images_per_result=3):
    """更新配置文件中的PLATFORM和KEYWORDS"""
    config_file = 'config/base_config.py'
    
    # 读取配置文件
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新PLATFORM
    content = re.sub(r'PLATFORM = ".*"', f'PLATFORM = "{platform}"', content)
    
    # 更新KEYWORDS
    content = re.sub(r'KEYWORDS = ".*"', f'KEYWORDS = "{keywords}"', content)
    
    # 更新爬取视频数量
    content = re.sub(r'CRAWLER_MAX_NOTES_COUNT = \d+', f'CRAWLER_MAX_NOTES_COUNT = {max_notes}', content)
    
    # 更新单视频评论数量
    content = re.sub(r'CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = \d+', f'CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = {max_comments}', content)
    
    # 更新是否启用评论获取（如果指定了评论数量，则启用）
    enable_get_comments = max_comments > 0
    content = re.sub(r'ENABLE_GET_COMMENTS = \w+', f'ENABLE_GET_COMMENTS = {enable_get_comments}', content)
    
    # 更新是否启用二级评论
    content = re.sub(r'ENABLE_GET_SUB_COMMENTS = \w+', f'ENABLE_GET_SUB_COMMENTS = {enable_sub_comments}', content)

    # 更新CRAWLER_TYPE为search（关键词搜索模式）
    content = re.sub(r'(CRAWLER_TYPE = \(\s*)"detail"', r'\1"search"', content)

    # 写回配置文件
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 更新平台特定配置
    if platform == 'dy':
        dy_config_file = 'config/dy_config.py'
        with open(dy_config_file, 'r', encoding='utf-8') as f:
            dy_content = f.read()
        
        # 将任意天数适配到抖音支持的最小范围
        # 抖音支持: 0(不限), 1(一天内), 7(一周内), 180(半年内)
        if time_type == 0:
            dy_time_type = 0
        elif time_type < 7:
            dy_time_type = 1
        elif time_type < 180:
            dy_time_type = 7
        else:
            dy_time_type = 180
        
        # 更新PUBLISH_TIME_TYPE
        dy_content = re.sub(r'PUBLISH_TIME_TYPE = \d+', f'PUBLISH_TIME_TYPE = {dy_time_type}', dy_content)
        
        with open(dy_config_file, 'w', encoding='utf-8') as f:
            f.write(dy_content)
        
        print(f'已更新抖音时间类型为: {dy_time_type} (输入: {time_type}天)')
    elif platform == 'bili':
        bili_config_file = 'config/bilibili_config.py'
        with open(bili_config_file, 'r', encoding='utf-8') as f:
            bili_content = f.read()
        
        # 根据time_type更新BILI_SEARCH_MODE
        # time_type == 0 表示不限时间，使用 normal 模式（search_by_keywords方法传递pubtime_begin_s=0, pubtime_end_s=0）
        # time_type > 0 表示在指定时间范围内搜索，使用 all_in_time_range 或 daily_limit_in_time_range 模式
        if time_type == 0:
            bili_content = re.sub(r'BILI_SEARCH_MODE = ".*"', 'BILI_SEARCH_MODE = "normal"', bili_content)
            print(f'已更新B站搜索模式为: normal (不限时间)')
        else:
            import datetime
            today = datetime.date.today()
            end_day = today.strftime('%Y-%m-%d')
            start_day = (today - datetime.timedelta(days=time_type)).strftime('%Y-%m-%d')
            bili_content = re.sub(r'BILI_SEARCH_MODE = ".*"', 'BILI_SEARCH_MODE = "all_in_time_range"', bili_content)
            bili_content = re.sub(r'START_DAY = ".*"', f'START_DAY = "{start_day}"', bili_content)
            bili_content = re.sub(r'END_DAY = ".*"', f'END_DAY = "{end_day}"', bili_content)
            print(f'已更新B站时间范围为: {start_day} 至 {end_day}')
        
        with open(bili_config_file, 'w', encoding='utf-8') as f:
            f.write(bili_content)
    elif platform == 'tavily':
        tavily_config_file = 'config/tavily_config.py'
        with open(tavily_config_file, 'r', encoding='utf-8') as f:
            tavily_content = f.read()
        
        # 将任意天数适配到 Tavily 支持的最小范围
        # Tavily 支持: None(不限), "day"(一天内), "week"(一周内), "month"(一个月内), "year"(一年内)
        if time_type == 0:
            tavily_time_range = None
        elif time_type < 7:
            tavily_time_range = "day"
        elif time_type < 30:
            tavily_time_range = "week"
        elif time_type < 365:
            tavily_time_range = "month"
        else:
            tavily_time_range = "year"
        
        # 更新CURRENT_TIME_RANGE
        if tavily_time_range is None:
            updated_value = 'None'
        else:
            updated_value = f'"{tavily_time_range}"'
        tavily_content = re.sub(r'CURRENT_TIME_RANGE = .*', f'CURRENT_TIME_RANGE = {updated_value}', tavily_content)
        
        # 更新ENABLE_TAVILY_IMG
        tavily_content = re.sub(r'ENABLE_TAVILY_IMG = \w+', f'ENABLE_TAVILY_IMG = {enable_tavily_img}', tavily_content)
        
        # 更新MAX_IMAGES_PER_RESULT
        tavily_content = re.sub(r'MAX_IMAGES_PER_RESULT = \d+', f'MAX_IMAGES_PER_RESULT = {max_images_per_result}', tavily_content)
        
        with open(tavily_config_file, 'w', encoding='utf-8') as f:
            f.write(tavily_content)
        
        print(f'已更新Tavily时间范围为: {tavily_time_range} (输入: {time_type}天)')
        print(f'已更新Tavily图片下载为: {enable_tavily_img}')
        print(f'已更新Tavily最大图片数量为: {max_images_per_result}')
    
    print(f'已更新PLATFORM为: {platform}')
    print(f'已更新KEYWORDS为: {keywords}')
    print(f'已更新爬取视频数量为: {max_notes}')
    print(f'已更新单视频评论数量为: {max_comments}')
    print(f'已更新是否启用二级评论为: {enable_sub_comments}')

import time

def run_crawler(platform, keywords, time_type=0, max_notes=15, max_comments=10, enable_sub_comments=False, enable_tavily_img=False, max_images_per_result=3, max_retries=3, retry_delay=5):
    """运行单个平台的爬虫"""
    print(f'=========================================')
    print(f'开始爬取平台: {platform}')
    print(f'关键词: {keywords}')
    print(f'时间类型: {time_type}')
    print(f'爬取视频数量: {max_notes}')
    print(f'单视频评论数量: {max_comments}')
    print(f'启用二级评论: {enable_sub_comments}')
    print(f'Tavily图片下载: {enable_tavily_img}')
    print(f'每个搜索结果最大图片数: {max_images_per_result}')
    print(f'最大重试次数: {max_retries}')
    print(f'重试等待时间: {retry_delay}秒')
    print(f'=========================================')
    
    for attempt in range(max_retries + 1):
        try:
            # 更新配置
            update_config(platform, keywords, time_type, max_notes, max_comments, enable_sub_comments, enable_tavily_img, max_images_per_result)
            
            # 运行爬虫
            exit_code = os.system('python main.py')
            
            if exit_code != 0:
                print(f'警告: 平台 {platform} 爬虫退出码为 {exit_code}')
                if attempt < max_retries:
                    print(f'尝试 {attempt + 1}/{max_retries + 1} 失败，{retry_delay}秒后重试...')
                    time.sleep(retry_delay)
                    continue
            
            print(f'平台 {platform} 爬取完成')
            break
        except Exception as e:
            print(f'错误: 平台 {platform} 爬取失败: {str(e)}')
            if attempt < max_retries:
                print(f'尝试 {attempt + 1}/{max_retries + 1} 失败，{retry_delay}秒后重试...')
                time.sleep(retry_delay)
                continue
            else:
                print(f'已达到最大重试次数 {max_retries}，将继续执行下一个平台...')
 

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print('用法: python run_crawler.py <platforms> <keywords> [time_type] [max_notes] [max_comments] [enable_sub_comments]')
        print('示例: python run_crawler.py dy,ks 闪充 0 15 10 false')
        print('时间类型: 0=不限, 1=一天内, 7=一周内, 180=半年内')
        print('爬取视频数量: 默认为15')
        print('单视频评论数量: 默认为10')
        print('启用二级评论: true/false, 默认为false')
        sys.exit(1)
    
    platforms_str = sys.argv[1]
    keywords = sys.argv[2]
    time_type = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    max_notes = int(sys.argv[4]) if len(sys.argv) > 4 else 15
    max_comments = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    enable_sub_comments = sys.argv[6].lower() == 'true' if len(sys.argv) > 6 else False
    
    # 将平台字符串转换为数组
    platforms = [p.strip() for p in platforms_str.split(',')]
    
    # 为每个平台运行爬虫
    for platform in platforms:
        try:
            run_crawler(platform, keywords, time_type, max_notes, max_comments, enable_sub_comments, max_retries=3, retry_delay=5)
        except Exception as e:
            print(f'严重错误: 平台 {platform} 处理过程中发生未捕获的异常: {str(e)}')
            print(f'将继续执行下一个平台...')
            print('')

def generate_video_download_markdown(platforms, keywords):
    """
    生成视频下载链接的markdown文件
    
    Args:
        platforms: 平台列表
        keywords: 搜索关键词
    """
    data_dir = Path('data')
    markdown_lines = []
    
    # 添加标题和时间
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    markdown_lines.append(f"# 视频下载链接汇总")
    markdown_lines.append(f"")
    markdown_lines.append(f"**搜索关键词**: {keywords}")
    markdown_lines.append(f"**生成时间**: {timestamp}")
    markdown_lines.append(f"")
    
    for platform in platforms:
        markdown_lines.append(f"## {get_platform_name(platform)}")
        markdown_lines.append(f"")
        
        # 查找内容文件 - 支持多种存储路径
        content_files = []
        platform_name = get_platform_name(platform)
        
        # 搜索路径：data/csv/ 目录（全局CSV存储）
        csv_dir = data_dir / 'csv'
        if csv_dir.exists():
            for ext in ['csv']:
                content_files.extend(list(csv_dir.glob(f'*{platform}*contents*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform}*video*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform}*content*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform_name}*contents*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform_name}*video*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform_name}*content*.{ext}')))
                platform_full_names = {
                    'dy': 'douyin',
                    'bili': 'bilibili',
                    'xhs': 'xiaohongshu',
                    'ks': 'kuaishou',
                    'wb': 'weibo'
                }
                if platform in platform_full_names:
                    content_files.extend(list(csv_dir.glob(f'*{platform_full_names[platform]}*contents*.{ext}')))
                    content_files.extend(list(csv_dir.glob(f'*{platform_full_names[platform]}*video*.{ext}')))
                    content_files.extend(list(csv_dir.glob(f'*{platform_full_names[platform]}*content*.{ext}')))
        
        # 搜索路径：data/{platform}/ 目录
        platform_dir = data_dir / platform
        if platform_dir.exists():
            for ext in ['json', 'jsonl', 'csv']:
                content_files.extend(list(platform_dir.glob(f'**/*contents*.{ext}')))
        
        # 搜索路径：data/ 根目录
        for ext in ['json', 'jsonl']:
            content_files.extend(list(data_dir.glob(f'*{platform}*contents*.{ext}')))
        
        # 去重文件列表
        content_files = list(set(content_files))
        
        print(f"找到 {len(content_files)} 个内容文件")
        for f in content_files:
            print(f"  - {f}")
        
        # 提取视频下载链接
        video_links = []
        for content_file in content_files:
            try:
                if content_file.suffix == '.json':
                    with open(content_file, 'r', encoding='utf-8') as f:
                        items = json.load(f)
                        if isinstance(items, list):
                            for item in items:
                                extract_video_links(item, video_links, platform)
                        elif isinstance(items, dict):
                            extract_video_links(items, video_links, platform)
                
                elif content_file.suffix == '.jsonl':
                    with open(content_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if line:
                                try:
                                    item = json.loads(line)
                                    extract_video_links(item, video_links, platform)
                                except json.JSONDecodeError:
                                    continue
                
                elif content_file.suffix == '.csv':
                    import csv
                    # 处理带有BOM的UTF-8文件
                    with open(content_file, 'r', encoding='utf-8-sig', errors='replace') as f:
                        reader = csv.DictReader(f)
                        print(f"CSV文件列头: {reader.fieldnames}")
                        for row in reader:
                            extract_video_links(row, video_links, platform)
            
            except Exception as e:
                print(f"读取文件 {content_file} 时出错: {str(e)}")
        
        print(f"从文件中提取到 {len(video_links)} 个视频链接")

        seen_download_urls = set()
        seen_original_urls = set()
        for idx, (title, original_url, download_url) in enumerate(video_links, 1):
            download_display = ""
            if download_url and download_url not in seen_download_urls:
                seen_download_urls.add(download_url)
                download_display = f" | [下载链接]({download_url})"

            original_display = ""
            if original_url and original_url not in seen_original_urls:
                seen_original_urls.add(original_url)
                display_title = title[:50] + '...' if len(title) > 50 else title
                original_display = f"[{display_title}]({original_url})"

            if original_display or download_display:
                if original_display and download_display:
                    markdown_lines.append(f"{idx}. {original_display}{download_display}")
                elif original_display:
                    markdown_lines.append(f"{idx}. {original_display}")
                elif download_display:
                    markdown_lines.append(f"{idx}. [下载链接]({download_url})")

        if not video_links:
            markdown_lines.append(f"- 暂无视频链接")

        markdown_lines.append(f"")
    
    # 添加图片信息（如果存在）
    markdown_lines = add_images_to_markdown(markdown_lines, keywords)
    
    # 写入markdown文件
    sanitized_keywords = keywords.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    markdown_filename = data_dir / f"视频下载链接_{sanitized_keywords}.md"
    
    with open(markdown_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))
    
    print(f"\n已生成视频下载链接markdown文件: {markdown_filename}")


def add_images_to_markdown(markdown_lines, keywords):
    """
    将图片信息添加到markdown中
    
    Args:
        markdown_lines: 现有的markdown行列表
        keywords: 搜索关键词
    
    Returns:
        更新后的markdown行列表
    """
    data_dir = Path('data')
    images_dir = data_dir / 'images'
    image_config_path = images_dir / 'image_config.json'
    
    if not image_config_path.exists():
        return markdown_lines
    
    try:
        with open(image_config_path, 'r', encoding='utf-8') as f:
            image_config = json.load(f)
        
        if not image_config:
            return markdown_lines
        
        # 添加图片部分标题
        markdown_lines.append(f"## 图片列表（共{len(image_config)}张）")
        markdown_lines.append(f"")
        
        for idx, img_info in enumerate(image_config, 1):
            filename = img_info.get('filename', '')
            url = img_info.get('url', '')
            source_title = img_info.get('source_title', '')
            source_url = img_info.get('source_url', '')
            description = img_info.get('description', '')
            download_time = img_info.get('download_time', '')
            
            markdown_lines.append(f"### {idx}. {filename}")
            markdown_lines.append(f"")
            markdown_lines.append(f"![图片{idx}](images/{filename})")
            markdown_lines.append(f"")
            
            if source_title and source_url:
                display_title = source_title[:50] + '...' if len(source_title) > 50 else source_title
                markdown_lines.append(f"- **来源**: [{display_title}]({source_url})")
            elif source_title:
                markdown_lines.append(f"- **来源**: {source_title}")
            
            if url:
                markdown_lines.append(f"- **原始URL**: {url}")
            
            if description:
                markdown_lines.append(f"- **描述**: {description}")
            
            if download_time:
                markdown_lines.append(f"- **下载时间**: {download_time}")
            
            markdown_lines.append(f"")
        
        # 删除单独的图片下载链接文件（如果存在）
        image_md_path = data_dir / f"图片下载链接_{keywords}.md"
        if image_md_path.exists():
            try:
                os.remove(image_md_path)
                print(f"已删除单独的图片下载链接文件: {image_md_path}")
            except Exception as e:
                print(f"删除图片下载链接文件失败: {str(e)}")
        
    except Exception as e:
        print(f"读取图片配置文件失败: {str(e)}")
    
    return markdown_lines


def extract_video_links(item, video_links, platform):
    """
    从内容项中提取视频原链接和下载链接

    Args:
        item: 内容项字典
        video_links: 视频链接列表（用于追加），每个元素是 (title, original_url, download_url) 元组
        platform: 平台名称
    """
    title = None
    original_url = None
    download_url = None

    title_fields = [
        'title',
        'desc',
        'aweme_id',
        'video_id',
        'note_id',
        'content_id'
    ]

    for field in title_fields:
        if field in item and item[field]:
            title = str(item[field])
            break

    download_url_fields = [
        'video_download_url',
        'download_url'
    ]

    for field in download_url_fields:
        if field in item and item[field]:
            download_url = item[field]
            break

    original_url_fields = [
        'url',
        'video_url',
        'aweme_url',
        'share_url',
        'note_url',
        'content_url'
    ]

    for field in original_url_fields:
        if field in item and item[field]:
            original_url = item[field]
            break

    if original_url or download_url:
        if not title:
            title = f"{get_platform_name(platform)}视频"
        video_links.append((title, original_url, download_url))


def get_platform_name(platform):
    """
    获取平台中文名称
    
    Args:
        platform: 平台缩写
    
    Returns:
        平台中文名称
    """
    platform_names = {
        'dy': '抖音',
        'douyin': '抖音',
        'bili': '哔哩哔哩',
        'bilibili': '哔哩哔哩',
        'xhs': '小红书',
        'xiaohongshu': '小红书',
        'ks': '快手',
        'kuaishou': '快手',
        'wb': '微博',
        'weibo': '微博',
        'zhihu': '知乎',
        'tieba': '贴吧',
        'tavily': 'Tavily'
    }
    return platform_names.get(platform.lower(), platform)


def main():
    """主函数"""
    if len(sys.argv) < 3:
        print('用法: python run_crawler.py <platforms> <keywords> [time_type] [max_notes] [max_comments] [enable_sub_comments] [enable_tavily_img] [max_images_per_result]')
        print('示例: python run_crawler.py dy,ks 闪充 0 15 10 false false 3')
        print('时间类型: 0=不限, 1=一天内, 7=一周内, 180=半年内')
        print('爬取视频数量: 默认为15')
        print('单视频评论数量: 默认为10')
        print('启用二级评论: true/false, 默认为false')
        print('Tavily图片下载: true/false, 默认为false')
        print('每个搜索结果最大图片数: 默认为3')
        sys.exit(1)
    
    platforms_str = sys.argv[1]
    keywords = sys.argv[2]
    time_type = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    max_notes = int(sys.argv[4]) if len(sys.argv) > 4 else 15
    max_comments = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    enable_sub_comments = sys.argv[6].lower() == 'true' if len(sys.argv) > 6 else False
    enable_tavily_img = sys.argv[7].lower() == 'true' if len(sys.argv) > 7 else False
    max_images_per_result = int(sys.argv[8]) if len(sys.argv) > 8 else 3
    
    # 将平台字符串转换为数组
    platforms = [p.strip() for p in platforms_str.split(',')]
    
    # 为每个平台运行爬虫
    for platform in platforms:
        try:
            run_crawler(platform, keywords, time_type, max_notes, max_comments, enable_sub_comments, enable_tavily_img, max_images_per_result, max_retries=3, retry_delay=5)
        except Exception as e:
            print(f'严重错误: 平台 {platform} 处理过程中发生未捕获的异常: {str(e)}')
            print(f'将继续执行下一个平台...')
            print('')
    
    # 生成视频下载链接markdown文件
    generate_video_download_markdown(platforms, keywords)


if __name__ == '__main__':
    main()