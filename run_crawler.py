#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
import os

def update_config(platform, keywords, time_type=0, max_notes=15, max_comments=10, enable_sub_comments=False):
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
    
    # 更新是否启用二级评论
    content = re.sub(r'ENABLE_GET_SUB_COMMENTS = \w+', f'ENABLE_GET_SUB_COMMENTS = {enable_sub_comments}', content)
    
    # 写回配置文件
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 更新平台特定配置
    if platform == 'dy':
        dy_config_file = 'config/dy_config.py'
        with open(dy_config_file, 'r', encoding='utf-8') as f:
            dy_content = f.read()
        
        # 更新PUBLISH_TIME_TYPE
        dy_content = re.sub(r'PUBLISH_TIME_TYPE = \d+', f'PUBLISH_TIME_TYPE = {time_type}', dy_content)
        
        with open(dy_config_file, 'w', encoding='utf-8') as f:
            f.write(dy_content)
        
        print(f'已更新抖音时间类型为: {time_type}')
    
    print(f'已更新PLATFORM为: {platform}')
    print(f'已更新KEYWORDS为: {keywords}')
    print(f'已更新爬取视频数量为: {max_notes}')
    print(f'已更新单视频评论数量为: {max_comments}')
    print(f'已更新是否启用二级评论为: {enable_sub_comments}')

def run_crawler(platform, keywords, time_type=0, max_notes=15, max_comments=10, enable_sub_comments=False):
    """运行单个平台的爬虫"""
    print(f'=========================================')
    print(f'开始爬取平台: {platform}')
    print(f'关键词: {keywords}')
    print(f'时间类型: {time_type}')
    print(f'爬取视频数量: {max_notes}')
    print(f'单视频评论数量: {max_comments}')
    print(f'启用二级评论: {enable_sub_comments}')
    print(f'=========================================')
    
    try:
        # 更新配置
        update_config(platform, keywords, time_type, max_notes, max_comments, enable_sub_comments)
        
        # 运行爬虫
        exit_code = os.system('python main.py')
        
        if exit_code != 0:
            print(f'警告: 平台 {platform} 爬虫退出码为 {exit_code}')
        
        print(f'平台 {platform} 爬取完成')
    except Exception as e:
        print(f'错误: 平台 {platform} 爬取失败: {str(e)}')
        print(f'将继续执行下一个平台...')
    finally:
        print('')

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
            run_crawler(platform, keywords, time_type, max_notes, max_comments, enable_sub_comments)
        except Exception as e:
            print(f'严重错误: 平台 {platform} 处理过程中发生未捕获的异常: {str(e)}')
            print(f'将继续执行下一个平台...')
            print('')

if __name__ == '__main__':
    main()