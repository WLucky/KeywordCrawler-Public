# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/config/base_config.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# Basic configuration
PLATFORM = "bili"  # Platform, xhs | dy | ks | bili | wb | tieba | zhihu

# 是否使用海外版小红书 (rednote.com)
# 开启后 API 走 webapi.rednote.com，cookie 域使用 .rednote.com
XHS_INTERNATIONAL = False

KEYWORDS = "比亚迪 闪充"  # Keyword search configuration, separated by English commas
LOGIN_TYPE = "cookie"  # qrcode or phone or cookie
CRAWLER_TYPE = (
    "search"  # Crawling type, search (keyword search) | detail (post details) | creator (creator homepage data)
)


# Cookie configuration
bili_cookie = "buvid3=77786437-77D8-FBC9-BF3B-3F1B91C782E114345infoc; b_nut=1776258514; _uuid=D1688F31-21066-1E2D-3643-42F8105106101D415047infoc; home_feed_column=5; buvid_fp=a79ef04da05c36ff87b4cd4da5dae4a4; buvid4=E54F71E6-C289-686A-57FA-5B3631446D2614857-026041521-Q2nbNRIYxKPMEGKNmsjQ+g%3D%3D; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzY1MjAwNzUsImlhdCI6MTc3NjI2MDgxNSwicGx0IjotMX0.AiUwpNg882axh_i-SYrdQAmM_4QBrq7cqscTyFL8w5s; bili_ticket_expires=1776520015; SESSDATA=3c961852%2C1791812905%2C51786%2A42CjDYkFkIi75MKlo4EqtXABvPO0juIzyKF1AFHR7Ha1NH87aFKytJaChx42jTIShllu4SVkVENkdLc3ZPNWY2aWFWbUtrOUlTTFU5OGZ0N2c1dWFvS0VwSEhEQ2lGZ2gwbFNMOG5NZUtOa0YtZFZIdGk0dDk2ZjJ2dTFqZVo4NmhMQm9aSGk2Y2t3IIEC; bili_jct=6ef5c692f86cf1ce1a470a83d2638587; DedeUserID=325729166; DedeUserID__ckMd5=d82f0493c30e1d2d; theme-tip-show=SHOWED; sid=70emon06; CURRENT_FNVAL=4048; CURRENT_QUALITY=0; rpdid=|(um|Jl~lmRm0J'u~~YkY|mu|; browser_resolution=1798-1308; b_lsid=4FA39060_19D9166E9DB"
xhs_cookie = ""
dy_cookie = "enter_pc_once=1; UIFID_TEMP=d9c83d80110ac3c8e785b8c343d751a11fe18d1882e6e45bacc56136cf7b8ae9b5d1da2f27a1cc3470d70c62673802987407b22bf63117cffafdc4f0a597e32e0f7b3ee4ce6f76df969e3d1f52d361a0; hevc_supported=true; strategyABtestKey=%221776128078.737%22; is_dash_user=1; passport_csrf_token=5a228c012331b8d9b019fb6397736f1a; passport_csrf_token_default=5a228c012331b8d9b019fb6397736f1a; bd_ticket_guard_client_web_domain=2; passport_assist_user=CjweD1s3K9w72yuhunDoMaTvLbEMVg1MszPJExTiVg8WppNh5wD-Zvh0mT8vSf93qCY6Fn0FXlTOormZBJ0aSgo8AAAAAAAAAAAAAFBMgw0B6qCjxucNKM_f9qIUPaFIKGyCzaLx3Oj6rN6XEbcZkhz55vtCAKK1cqiQcqm3EOvhjg4Yia_WVCABIgEDufs-4Q%3D%3D; n_mh=1NpTZPU7IRgj-RNu_i-31sjRfot6pfOIBpBSH_balgA; sid_guard=e9a0418cf5d85f9d7ad9b6d374c73055%7C1776128101%7C5184000%7CSat%2C+13-Jun-2026+00%3A55%3A01+GMT; uid_tt=62f51fbe2b2ad4171a5a278280d16f9e; uid_tt_ss=62f51fbe2b2ad4171a5a278280d16f9e; sid_tt=e9a0418cf5d85f9d7ad9b6d374c73055; sessionid=e9a0418cf5d85f9d7ad9b6d374c73055; sessionid_ss=e9a0418cf5d85f9d7ad9b6d374c73055; session_tlb_tag=sttt%7C4%7C6aBBjPXYX5162bbTdMcwVf_________9iA8V4ONJrEOqU2H2bTkkJ5VwsTM_6WbnfoOJ9aQBsQo%3D; is_staff_user=false; has_biz_token=false; sid_ucp_v1=1.0.0-KDdhYTg0MTBiYWE1ZDYyNzZlYTliNDgxODNmZmFjOTJhZjcwMTM4YzkKHwjxvu7-3wIQ5aD2zgYY7zEgDDDg-O7UBTgHQPQHSAQaAmxmIiBlOWEwNDE4Y2Y1ZDg1ZjlkN2FkOWI2ZDM3NGM3MzA1NQ; ssid_ucp_v1=1.0.0-KDdhYTg0MTBiYWE1ZDYyNzZlYTliNDgxODNmZmFjOTJhZjcwMTM4YzkKHwjxvu7-3wIQ5aD2zgYY7zEgDDDg-O7UBTgHQPQHSAQaAmxmIiBlOWEwNDE4Y2Y1ZDg1ZjlkN2FkOWI2ZDM3NGM3MzA1NQ; _bd_ticket_crypt_cookie=d7341a0b76c8a3c5c3cd70adbd4cdba3; __security_mc_1_s_sdk_sign_data_key_web_protect=1c0c96f2-4754-a50b; __security_mc_1_s_sdk_cert_key=03baedb1-44f9-8941; __security_mc_1_s_sdk_crypt_sdk=d4e414cf-4d99-8e3c; __security_server_data_status=1; login_time=1776128103095; publish_badge_show_info=%220%2C0%2C0%2C1776128103405%22; DiscoverFeedExposedAd=%7B%7D; UIFID=d9c83d80110ac3c8e785b8c343d751a11fe18d1882e6e45bacc56136cf7b8ae9b5d1da2f27a1cc3470d70c6267380298c4b132adea875f8df1995d8d436e7e877e859c95c2a827b125f47e5517cf5d2a956b3cd48c78f4e5dce7408fdadff6407d1217ae2483b09ae4b881583c1b974fdd8ac6a058789fc996f0a0a290225f924e1c2da1ffe2b042e6bd2dbd8928450675d021ad9e3b8379a03a3271509d460a; SelfTabRedDotControl=%5B%5D; ttwid=1%7Cv-52CjBFpMuFC_r7yJC6Fulys-vsoiBWjHjp0HQN_Cg%7C1776128105%7Cf29fb8769f096e27d37e5880d1b0c4e03c8f2d29c53e0d7558a1aa477b71a8ad; playRecommendGuideTagCount=1; totalRecommendGuideTagCount=1; my_rd=2; download_guide=%222%2F20260414%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRnRiY1dqdWFzZnFkVXkrQ0xOVUM2ZUsyZ3dVVVQ4NDVmU3pHZXk2dVMzb1BDSERCYmtaWTU3MEtTNytBUXRjbmVMd3drVUdaQjc5RC9tVkk0L1JKb2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA3Klc3wNNcfyn-BMIlVRUD0SccRaoK_I_kp1RosekCJo%2F1776182400000%2F0%2F0%2F1776169087669%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA3Klc3wNNcfyn-BMIlVRUD0SccRaoK_I_kp1RosekCJo%2F1776182400000%2F0%2F0%2F1776169687669%22; odin_tt=538e2c21c2269b5aaac21125cb9678a4739691db03018973a84c890b43677d655609b04d3089ff7c9d4992584194cf9b99d61b37bd9d435681f2fa080851fb24; home_can_add_dy_2_desktop=%221%22; biz_trace_id=e0d3b4bd; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273c3133373c313d333433323234272927676c715a75776a716a666a69273f2763646976602778; bit_env=PrWB0C16cl8Arn525EmLsC-bfcB5D0i8DF5xYo8HpozXQ7fuM0Ily3D1phNqPfVf4EyojGiVpKvbDinaWd4XaMegKV1VKHeOsemq-J39pkaa5jfQUnszshoE8BlLUdqFVIsgHlVIKEvKfmSMnBoM-hmBFoBCbhQmHENOBJYRCk90-0uodb-ZfmuMl2954ZKGTE9JHvP9LpU0FkWFaP9TW1C5OVPOFby9i6sY6XjA9klGmks2r-hZm6lVQqlsuesWQLFrbnHGbk8TodBkoOOIB5LejbQRzeryxep9Sgd1cx-W6R0p24uJiGea3-QvdMwCF5m26bPsuZJvpp5YjJnXVG35vycFxj5dgvsvMp81uLugwMylvPJMhSwLrUdjYY7dAy3TS9Lzgb_wUNV9-QxQzrNqfic_Sp02SEMHH8YJOVBuMGdwLirVwXCIgieWwkPabIfriVOjwRBSfwoEQNbCRlHzypu6RUaAI6SCHJsUq17IfZNE8Aj73kkljw1GcGwIgr6nKi2bXlnJN00RCu22zg6fhlQr3C2kGAzFBKS5v8I%3D; gulu_source_res=eyJwX2luIjoiZWQ4OTJkZTQxNGQ4NGI4MzgwNWEwYjA4MDY3MTA0MzU4MTFlNGFjOGQyYzEwZjAxMjZiMTJiYjAzYTEyZDlkNCJ9; passport_auth_mix_state=kdtdfvgv88bn708kgq8t222c8bu2ior7pwbu4ce1jsoadooz; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJGdGJjV2p1YXNmcWRVeStDTE5VQzZlSzJnd1VVVDg0NWZTekdleTZ1UzNvUENIREJia1pZNTcwS1M3K0FRdGNuZUx3d2tVR1pCNzlEL21WSTQvUkpvZz0iLCJ0c19zaWduIjoidHMuMi4xZmIxNTJhZGE2ZjY4MDAxNTgwMGU0NGI1ZjVjM2U2M2UyYTNlYTcyM2I3YTJmYzNmOGM5ZmY3MmRkMzhhYjI1YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJYNjZqWHlNUjVYQlZnNEMwckUzMzd4OHdxSnFkbkRDTVNseE5sWVgyRzhjPSIsInNlY190cyI6IiM0TGM1Y1huSEdMR1VQczFRNTBQNGRDNWdSaWwwM2huK2p1MEtPeXVnSU1OMXZYckZHWkZHNHRQQm1tTVkifQ%3D%3D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; IsDouyinActive=true"
ks_cookie = ""
wb_cookie = ""
tieba_cookie = ""
zhihu_cookie = ""


# 根据PLATFORM导入对应的平台配置并赋值COOKIES
if PLATFORM == "bili":
    COOKIES = bili_cookie
elif PLATFORM == "xhs":
    COOKIES = xhs_cookie
elif PLATFORM == "dy":
    COOKIES = dy_cookie
elif PLATFORM == "ks":
    COOKIES = ks_cookie
elif PLATFORM == "wb":
    COOKIES = wb_cookie
elif PLATFORM == "tieba":
    COOKIES = tieba_cookie
elif PLATFORM == "zhihu":
    COOKIES = zhihu_cookie

# Whether to enable IP proxy
ENABLE_IP_PROXY = False

# Number of proxy IP pools
IP_PROXY_POOL_COUNT = 2

# Proxy IP provider name
IP_PROXY_PROVIDER_NAME = "kuaidaili"  # kuaidaili | wandouhttp

# Setting to True will not open the browser (headless browser)
# Setting False will open a browser
# If Xiaohongshu keeps scanning the code to log in but fails, open the browser and manually pass the sliding verification code.
# If Douyin keeps prompting failure, open the browser and see if mobile phone number verification appears after scanning the QR code to log in. If it does, manually go through it and try again.
HEADLESS = True

# Whether to save login status
SAVE_LOGIN_STATE = True

# ==================== CDP (Chrome DevTools Protocol) Configuration ====================
# Whether to enable CDP mode - use the user's existing Chrome/Edge browser to crawl, providing better anti-detection capabilities
# Once enabled, the user's Chrome/Edge browser will be automatically detected and started, and controlled through the CDP protocol.
# This method uses the real browser environment, including the user's extensions, cookies and settings, greatly reducing the risk of detection.
ENABLE_CDP_MODE = False

# CDP debug port, used to communicate with the browser
# If the port is occupied, the system will automatically try the next available port
CDP_DEBUG_PORT = 9222

# Custom browser path (optional)
# If it is empty, the system will automatically detect the installation path of Chrome/Edge
# Windows example: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# macOS example: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CUSTOM_BROWSER_PATH = ""

# Whether to enable headless mode in CDP mode
# NOTE: Even if set to True, some anti-detection features may not work well in headless mode
CDP_HEADLESS = False

# Browser startup timeout (seconds)
BROWSER_LAUNCH_TIMEOUT = 60

# Whether to automatically close the browser when the program ends
# Set to False to keep the browser running for easy debugging
AUTO_CLOSE_BROWSER = True

# Data saving type option configuration, supports: csv, db, json, jsonl, sqlite, excel, postgres. It is best to save to DB, with deduplication function.
SAVE_DATA_OPTION = "csv"  # csv or db or json or jsonl or sqlite or excel or postgres

# Data saving path, if not specified by default, it will be saved to the data folder.
SAVE_DATA_PATH = ""

# Browser file configuration cached by the user's browser
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# The number of pages to start crawling starts from the first page by default
START_PAGE = 1

# Control the number of crawled videos/posts
CRAWLER_MAX_NOTES_COUNT = 15

# Controlling the number of concurrent crawlers
MAX_CONCURRENCY_NUM = 1

# Whether to enable crawling media mode (including image or video resources), crawling media is not enabled by default
ENABLE_GET_MEIDAS = False

# Whether to enable comment crawling mode. Comment crawling is enabled by default.
ENABLE_GET_COMMENTS = True

# Control the number of crawled first-level comments (single video/post)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 10

# Whether to enable the mode of crawling second-level comments. By default, crawling of second-level comments is not enabled.
# If the old version of the project uses db, you need to refer to schema/tables.sql line 287 to add table fields.
ENABLE_GET_SUB_COMMENTS = False

# word cloud related
# Whether to enable generating comment word c  louds
ENABLE_GET_WORDCLOUD = False
# Custom words and their groups
# Add rule: xx:yy where xx is a custom-added phrase, and yy is the group name to which the phrase xx is assigned.
CUSTOM_WORDS = {
    "零几": "年份",  # Recognize "zero points" as a whole
    "高频词": "专业术语",  # Example custom words
}

# Deactivate (disabled) word file path
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# Chinese font file path
FONT_PATH = "./docs/STZHONGS.TTF"

# Crawl interval
CRAWLER_MAX_SLEEP_SEC = 2

# 是否禁用 SSL 证书验证。仅在使用企业代理、Burp Suite、mitmproxy 等会注入自签名证书的中间人代理时设为 True。
# 警告：禁用 SSL 验证将使所有流量暴露于中间人攻击风险，请勿在生产环境中开启。
DISABLE_SSL_VERIFY = False

# 根据PLATFORM导入对应的平台配置
from .bilibili_config import *
from .xhs_config import *
from .dy_config import *
from .ks_config import *
from .weibo_config import *
from .tieba_config import *
from .zhihu_config import *
