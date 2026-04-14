#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
import os

def update_config(platform, keywords):
    """更新配置文件中的PLATFORM和KEYWORDS"""
    config_file = 'config/base_config.py'
    
    # 读取配置文件
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新PLATFORM
    content = re.sub(r'PLATFORM = \".*\"', f'PLATFORM = \"{platform}\"', content)
    
    # 更新KEYWORDS
    content = re.sub(r'KEYWORDS = \".*\"', f'KEYWORDS = \"{keywords}\"', content)
    
    # 写回配置文件
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已更新PLATFORM为: {platform}')
    print(f'已更新KEYWORDS为: {keywords}')

def run_crawler(platform, keywords):
    """运行单个平台的爬虫"""
    print(f'=========================================')
    print(f'开始爬取平台: {platform}')
    print(f'关键词: {keywords}')
    print(f'=========================================')
    
    try:
        # 更新配置
        update_config(platform, keywords)
        
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
        print('用法: python run_crawler.py <platforms> <keywords>')
        print('示例: python run_crawler.py dy,ks 闪充')
        sys.exit(1)
    
    platforms_str = sys.argv[1]
    keywords = sys.argv[2]
    
    # 将平台字符串转换为数组
    platforms = [p.strip() for p in platforms_str.split(',')]
    
    # 为每个平台运行爬虫
    for platform in platforms:
        try:
            run_crawler(platform, keywords)
        except Exception as e:
            print(f'严重错误: 平台 {platform} 处理过程中发生未捕获的异常: {str(e)}')
            print(f'将继续执行下一个平台...')
            print('')

if __name__ == '__main__':
    main()