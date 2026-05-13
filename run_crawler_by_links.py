#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
import os
import json
import time
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


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


def update_config_for_links(video_links_str, max_comments, enable_sub_comments):
    """更新配置文件用于视频链接爬取"""

    dy_config_file = 'config/dy_config.py'
    with open(dy_config_file, 'r', encoding='utf-8') as f:
        dy_content = f.read()

    video_list = [link.strip() for link in video_links_str.split(';') if link.strip()]
    new_list_str = ',\n    '.join([f'"{link}"' for link in video_list])

    pattern = r'DY_SPECIFIED_ID_LIST = \[.*?\]'
    replacement = f'DY_SPECIFIED_ID_LIST = [\n    {new_list_str},\n]'
    dy_content = re.sub(pattern, replacement, dy_content, flags=re.DOTALL)

    with open(dy_config_file, 'w', encoding='utf-8') as f:
        f.write(dy_content)

    print(f'已更新DY_SPECIFIED_ID_LIST，共 {len(video_list)} 个视频链接')

    base_config_file = 'config/base_config.py'
    with open(base_config_file, 'r', encoding='utf-8') as f:
        base_content = f.read()

    base_content = base_content.replace(f'PLATFORM = "xhs"', 'PLATFORM = "dy"')
    base_content = base_content.replace('PLATFORM = "bili"', 'PLATFORM = "dy"')

    base_content = re.sub(
        r'(CRAWLER_TYPE = \(\s*)"search"',
        r'\1"detail"',
        base_content
    )

    base_content = re.sub(r'CRAWLER_MAX_NOTES_COUNT = \d+', f'CRAWLER_MAX_NOTES_COUNT = {max_comments}', base_content)
    base_content = re.sub(r'CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = \d+', f'CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = {max_comments}', base_content)
    base_content = re.sub(r'ENABLE_GET_SUB_COMMENTS = \w+', f'ENABLE_GET_SUB_COMMENTS = {enable_sub_comments}', base_content)

    with open(base_config_file, 'w', encoding='utf-8') as f:
        f.write(base_content)

    print(f'已更新配置: PLATFORM=dy, CRAWLER_TYPE=detail')
    print(f'评论数量: {max_comments}, 二级评论: {enable_sub_comments}')


def get_platform_name(platform):
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


def extract_video_links(item, video_links, platform):
    url = None
    title = None

    url_fields = [
        'video_download_url',
        'video_url',
        'aweme_url',
        'video_play_url',
        'note_url',
        'content_url',
        'download_url'
    ]

    title_fields = [
        'title',
        'desc',
        'aweme_id',
        'video_id',
        'note_id',
        'content_id'
    ]

    for field in url_fields:
        if field in item and item[field]:
            url = item[field]
            break

    for field in title_fields:
        if field in item and item[field]:
            title = str(item[field])
            break

    if url:
        if not title:
            title = f"{get_platform_name(platform)}视频"
        video_links.append((title, url))


def generate_video_download_markdown(platforms, keywords):
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    markdown_lines = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    markdown_lines.append(f"# 视频下载链接汇总")
    markdown_lines.append(f"")
    markdown_lines.append(f"**搜索关键词**: {keywords}")
    markdown_lines.append(f"**生成时间**: {timestamp}")
    markdown_lines.append(f"")

    for platform in platforms:
        markdown_lines.append(f"## {get_platform_name(platform)}")
        markdown_lines.append(f"")

        content_files = []
        platform_name = get_platform_name(platform)

        csv_dir = data_dir / 'csv'
        if csv_dir.exists():
            for ext in ['csv']:
                content_files.extend(list(csv_dir.glob(f'*{platform}*contents*.{ext}')))
                content_files.extend(list(csv_dir.glob(f'*{platform_name}*contents*.{ext}')))
                platform_full_names = {
                    'dy': 'douyin',
                    'bili': 'bilibili',
                    'xhs': 'xiaohongshu',
                    'ks': 'kuaishou',
                    'wb': 'weibo'
                }
                if platform in platform_full_names:
                    content_files.extend(list(csv_dir.glob(f'*{platform_full_names[platform]}*contents*.{ext}')))

        platform_dir = data_dir / platform
        if platform_dir.exists():
            for ext in ['json', 'jsonl', 'csv']:
                content_files.extend(list(platform_dir.glob(f'**/*contents*.{ext}')))

        for ext in ['json', 'jsonl']:
            content_files.extend(list(data_dir.glob(f'*{platform}*contents*.{ext}')))

        content_files = list(set(content_files))

        print(f"找到 {len(content_files)} 个内容文件")
        for f in content_files:
            print(f"  - {f}")

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
                    with open(content_file, 'r', encoding='utf-8-sig', errors='replace') as f:
                        reader = csv.DictReader(f)
                        print(f"CSV文件列头: {reader.fieldnames}")
                        for row in reader:
                            extract_video_links(row, video_links, platform)

            except Exception as e:
                print(f"读取文件 {content_file} 时出错: {str(e)}")

        print(f"从文件中提取到 {len(video_links)} 个视频链接")

        seen_urls = set()
        for idx, (title, url) in enumerate(video_links, 1):
            if url not in seen_urls:
                seen_urls.add(url)
                display_title = title[:50] + '...' if len(title) > 50 else title
                markdown_lines.append(f"{idx}. [{display_title}]({url})")

        if not video_links:
            markdown_lines.append(f"- 暂无视频下载链接")

        markdown_lines.append(f"")

    sanitized_keywords = keywords.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    markdown_filename = data_dir / f"视频下载链接_{sanitized_keywords}.md"

    with open(markdown_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))

    print(f"\n已生成视频下载链接markdown文件: {markdown_filename}")


def run_crawler_by_links(video_links, max_comments, enable_sub_comments):
    """通过视频链接运行爬虫"""
    print(f'=========================================')
    print(f'开始爬取抖音视频评论')
    print(f'视频链接数量: {len(video_links.split(";"))}')
    print(f'评论数量: {max_comments}')
    print(f'二级评论: {enable_sub_comments}')
    print(f'=========================================')

    update_config_for_links(video_links, max_comments, enable_sub_comments)

    print("开始爬取指定视频链接...")
    try:
        exit_code = os.system('python main.py')
        if exit_code != 0:
            print(f'警告: 爬虫退出码为 {exit_code}')
    except Exception as e:
        print(f'爬虫执行异常: {str(e)}')

    try:
        generate_video_download_markdown(['dy'], '抖音视频链接')
    except Exception as e:
        print(f'生成markdown异常: {str(e)}')


def main():
    if len(sys.argv) < 4:
        print('用法: python run_crawler_by_links.py <video_links> <max_comments> <enable_sub_comments>')
        print('示例: python run_crawler_by_links.py "https://www.douyin.com/video/123456" 20 true')
        sys.exit(1)

    video_links = sys.argv[1]
    max_comments = int(sys.argv[2])
    enable_sub_comments = sys.argv[3].lower() == 'true'

    run_crawler_by_links(video_links, max_comments, enable_sub_comments)


if __name__ == '__main__':
    main()
