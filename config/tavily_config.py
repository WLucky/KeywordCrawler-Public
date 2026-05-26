# -*- coding: utf-8 -*-

# Tavily API 配置
TAVILY_API_KEY = "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"

# 搜索深度：basic 或 advanced
SEARCH_DEPTH = "advanced"

# 最大结果数
MAX_RESULTS = 15

# 每个来源的chunk数
CHUNKS_PER_SOURCE = 5

# 包含的域名
# 设置为空列表以不限制域名
INCLUDE_DOMAINS = []

# 时间范围映射
# 0=不限, 1=一天内, 7=一周内, 30=一个月内, 180=半年内(映射到一年), 365=一年内
TIME_RANGE_MAPPING = {
    0: None,      # 不限
    1: "day",     # 一天内
    7: "week",    # 一周内
    30: "month",  # 一个月内
    180: "year",  # 半年内映射到一年
    365: "year"   # 一年内
}

# 当前时间范围
CURRENT_TIME_RANGE = None

# Target time range in days specified by user (for timestamp filtering)
TARGET_TIME_RANGE_DAYS = 0

# 是否启用图片下载
ENABLE_TAVILY_IMG = False

# 最大下载图片数量（每个搜索结果最多下载的图片数）
MAX_IMAGES_PER_RESULT = 5
