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
PLATFORM = "dy"  # Platform, xhs | dy | ks | bili | wb | tieba | zhihu | tavily

# 是否使用海外版小红书 (rednote.com)
# 开启后 API 走 webapi.rednote.com，cookie 域使用 .rednote.com
XHS_INTERNATIONAL = False

KEYWORDS = "小米yu7 gt"  # Keyword search configuration, separated by English commas
LOGIN_TYPE = "cookie"  # qrcode or phone or cookie
CRAWLER_TYPE = (
    "detail"  # Crawling type, search (keyword search) | detail (post details) | creator (creator homepage data)
)


# Cookie configuration
bili_cookie = "buvid3=77786437-77D8-FBC9-BF3B-3F1B91C782E114345infoc; b_nut=1776258514; _uuid=D1688F31-21066-1E2D-3643-42F8105106101D415047infoc; home_feed_column=5; buvid_fp=a79ef04da05c36ff87b4cd4da5dae4a4; buvid4=E54F71E6-C289-686A-57FA-5B3631446D2614857-026041521-Q2nbNRIYxKPMEGKNmsjQ+g%3D%3D; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzY1MjAwNzUsImlhdCI6MTc3NjI2MDgxNSwicGx0IjotMX0.AiUwpNg882axh_i-SYrdQAmM_4QBrq7cqscTyFL8w5s; bili_ticket_expires=1776520015; SESSDATA=3c961852%2C1791812905%2C51786%2A42CjDYkFkIi75MKlo4EqtXABvPO0juIzyKF1AFHR7Ha1NH87aFKytJaChx42jTIShllu4SVkVENkdLc3ZPNWY2aWFWbUtrOUlTTFU5OGZ0N2c1dWFvS0VwSEhEQ2lGZ2gwbFNMOG5NZUtOa0YtZFZIdGk0dDk2ZjJ2dTFqZVo4NmhMQm9aSGk2Y2t3IIEC; bili_jct=6ef5c692f86cf1ce1a470a83d2638587; DedeUserID=325729166; DedeUserID__ckMd5=d82f0493c30e1d2d; theme-tip-show=SHOWED; sid=70emon06; CURRENT_FNVAL=4048; CURRENT_QUALITY=0; rpdid=|(um|Jl~lmRm0J'u~~YkY|mu|; browser_resolution=1798-1308; b_lsid=4FA39060_19D9166E9DB"
xhs_cookie = ""
dy_cookie = "enter_pc_once=1; UIFID_TEMP=3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b5ef687373370d429fd5dc5edfae84ae5faacec54822a45110e3fbb6c6eaede15c6f9c390543b6afe280dff18901a8898d; hevc_supported=true; strategyABtestKey=%221776262372.517%22; is_dash_user=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; passport_csrf_token=024b02a821635288fb544ad25fb0d315; passport_csrf_token_default=024b02a821635288fb544ad25fb0d315; bd_ticket_guard_client_web_domain=2; UIFID=3b6adaced0a588dab6f51c731af48a99e86229cd7fa27db4535ff73b415f88b5ef687373370d429fd5dc5edfae84ae5fc871a9a82bddd869e5512a5dfe452c8a4281abfb014af88fe889a607d475b8b9b8343889a9fbdc2d5fc0df9c8b31bd66e3245c13411774a6620f3dfdba5d5f7c94a4675a72fda70de11600539b0c04f1187012fb66f9dbd321d06a50ecac44f168f7b37563d0fd344e9ebee32d928211; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f27353d3d33303630333733323234272927676c715a75776a716a666a69273f2763646976602778; bit_env=CdhMgBl9rWWSX8F9PwMdeSjTqZpXrFcLoNZXTaWu0W-MZPM4MDnLlRPcTXTvEji3Zgn1G6O3b2iisWV1sUySJJiYhuE3VZlq3p7-HgnzC9hHu3TBzOuxDcqq6NqNOq52AF_xgLFPcEXtVKzYGHHYtVBLQ_bq4X_VA3nJtQ2akIuS2VZXi90g5HCF73x9QLprR0K8Xb3dYWDTIGlIxCLNcvmhThM6gWxss-Q1oijM3KGDppN1FcDb-QvJb5IZezqveAbXVwxh5IO9G2Ysn50DynoTtE8Fx5CxT1jT0p5eQAC6PVJ588k0LQvQZg5iDZhrINvhqhAYxVXqZpvQRzum2zLwlWALVpuXdPYO5BAj-TwnXSABvM8OS2S978uvYYiNcKfIo62xetuX5CS8keZ5vRtZRkdRNxh8ZPfEy2bhU9FSgqkSHBwrqpE6jL4wvrvGfvgamB7mzChh5vxvefOadmCK39_tbefnJP2YieaPoiYmdgAwhSXzAyi9EDyjh5aSp1sdjSlC9JDAi7lQEnil_II2S6E4FhLsQtg45nxV5lM%3D; gulu_source_res=eyJwX2luIjoiYzA3ZDQzMmJmM2E3YmU5Mjc0ZjBmODA2OGQwZjQ3N2M1Y2I2Mzc2NjNlZTdhOTBiMjlhZWNjZWE3YzQxMjgxYSJ9; passport_auth_mix_state=tumd29z9mnxhibktis88sqwp7xo270nk; passport_mfa_token=CjUDklsufPKAu1Xn%2FMasyOrU%2BxuRl%2BCIT3dHEbXXFedby5hHdM3701a1k5rQ2NnB4IhKElH9ihpKCjwAAAAAAAAAAAAAUE7NQxREKAuNSIh8jMM5FPkaI%2FdpnghlNYDyOo5%2BMzAmCpQyBhhoJStKUhw6TDIDpBkQzfOODhj2sdFsIAIiAQPQCHGX; d_ticket=5cafb9238e1c9fc2b031c4943ef23fd6c8996; passport_assist_user=Cjw1_izEVbTAOSI3H1ZVG7pAxGOygR6lA4MfJeW4NUCesDHF0SF1dHvyTbaA7QK3j22pCtYICR76fMPJpQ8aSgo8AAAAAAAAAAAAAFBORAVob6PPjCkGjiEkuIgaE3U2V1ReDg8BBtK6tr-ldb3xOYpI94dJlrq1p4pwzJasENvyjg4Yia_WVCABIgED0L90Sg%3D%3D; n_mh=1NpTZPU7IRgj-RNu_i-31sjRfot6pfOIBpBSH_balgA; passport_auth_status=97948c3e3cceb0fcf5c73b7563e5ee63%2C; passport_auth_status_ss=97948c3e3cceb0fcf5c73b7563e5ee63%2C; sid_guard=4cdda53690c55e9f2368daa67f7f61a8%7C1776265410%7C5184000%7CSun%2C+14-Jun-2026+15%3A03%3A30+GMT; uid_tt=c705d028e0063a32e85c3b19c78e8961; uid_tt_ss=c705d028e0063a32e85c3b19c78e8961; sid_tt=4cdda53690c55e9f2368daa67f7f61a8; sessionid=4cdda53690c55e9f2368daa67f7f61a8; sessionid_ss=4cdda53690c55e9f2368daa67f7f61a8; session_tlb_tag=sttt%7C12%7CTN2lNpDFXp8jaNqmf39hqP_________2H134B4dOeb6oKV31D0bTGQ-JL6P3PfUITxoJXm6Ny8c%3D; is_staff_user=false; has_biz_token=false; sid_ucp_v1=1.0.0-KDMxODMwMDZmODAzMjVlM2Q3NTM1YTQwYjBiZDg1ZTExZmRlOTNiYjcKHwjxvu7-3wIQwtH-zgYY7zEgDDDg-O7UBTgCQPEHSAQaAmxmIiA0Y2RkYTUzNjkwYzU1ZTlmMjM2OGRhYTY3ZjdmNjFhOA; ssid_ucp_v1=1.0.0-KDMxODMwMDZmODAzMjVlM2Q3NTM1YTQwYjBiZDg1ZTExZmRlOTNiYjcKHwjxvu7-3wIQwtH-zgYY7zEgDDDg-O7UBTgCQPEHSAQaAmxmIiA0Y2RkYTUzNjkwYzU1ZTlmMjM2OGRhYTY3ZjdmNjFhOA; _bd_ticket_crypt_cookie=fc89c67976140b626e83cb6f43853f92; __security_mc_1_s_sdk_sign_data_key_web_protect=2f8c619d-4017-9fd1; __security_mc_1_s_sdk_cert_key=66067dd8-4bc1-b84c; __security_mc_1_s_sdk_crypt_sdk=45746177-45b7-a389; __security_server_data_status=1; login_time=1776265411471; publish_badge_show_info=%220%2C0%2C0%2C1776265411780%22; DiscoverFeedExposedAd=%7B%7D; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A32%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA3Klc3wNNcfyn-BMIlVRUD0SccRaoK_I_kp1RosekCJo%2F1776268800000%2F0%2F1776265412806%2F0%22; SelfTabRedDotControl=%5B%5D; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSUpzZUtIdWxsTTNQU3lFLzIxY05kcFhqN1ZubjA2QlVrQVdIY2toNFNCT093SWwxUy9yNkF5cS9wZlkySDFzQzk0Y3hNMkZobXdOUDRtTFVjKzhyUmM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=fc09b8d23c903e612b721b32c45c6b991333544eece518d963782380e0d99d953ddaedef692c0c56941398e21cc10dcf706e458c71b5fab3a6ca720d4aa48b43; ttwid=1%7CW_y7_4FhJui4QHvHorjniO0j0Xx5BR8sgUlnp_aAoLY%7C1776265414%7C3fef98f1656c3f9dd7434f95ce47afaa51283afc7d2df9fc3c41f3139549d43c; biz_trace_id=a7e62f02; bd_ticket_guard_client_data_v2=eyJyZWVfcHVibGljX2tleSI6IkJJSnNlS0h1bGxNM1BTeUUvMjFjTmRwWGo3Vm5uMDZCVWtBV0hja2g0U0JPT3dJbDFTL3I2QXlxL3BmWTJIMXNDOTRjeE0yRmhtd05QNG1MVWMrOHJSYz0iLCJ0c19zaWduIjoidHMuMi4yNWFkNDNmMzBiYWZjZTcxZDEwNTkyNDA2NWJjNTdjNWYzODg5MTU2ZGRlZDdhYzFhMTUyOGY4ZDQ4ZmQ1NzlhYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50Ijoic2VjX3RzIiwicmVxX3NpZ24iOiJKUnZmUjNuNDY5WVpISnJJUTFiNVc1N0VDbWx1RGs2V0Q0MDVvdk9PcVE4PSIsInNlY190cyI6IiMzT2ZtQzhrelYzOWo4emxzVTdwV3ZZSi92L25UbTlOTEFSaVFRMEZDbEszU3l2RlJxd2Q2dml1V0J3YUMifQ%3D%3D"
ks_cookie = ""
wb_cookie = ""
tieba_cookie = ""
zhihu_cookie = ""


# 从文件中读取COOKIES的函数
def read_cookie_from_file(platform):
    cookie_file = f"./config/cookies/{platform}_cookie.txt"
    try:
        with open(cookie_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

# 根据PLATFORM导入对应的平台配置并赋值COOKIES
if PLATFORM == "bili":
    COOKIES = read_cookie_from_file("bili")
elif PLATFORM == "xhs":
    COOKIES = read_cookie_from_file("xhs")
elif PLATFORM == "dy":
    COOKIES = read_cookie_from_file("dy")
elif PLATFORM == "ks":
    COOKIES = read_cookie_from_file("ks")
elif PLATFORM == "wb":
    COOKIES = read_cookie_from_file("wb")
elif PLATFORM == "tieba":
    COOKIES = read_cookie_from_file("tieba")
elif PLATFORM == "zhihu":
    COOKIES = read_cookie_from_file("zhihu")
else:
    COOKIES = ""

# Whether to enable IP proxy
ENABLE_IP_PROXY = False

# ==================== Timestamp Filter Configuration ====================
# Enable timestamp filtering (when platform API time range is not precise, filter by video timestamp)
ENABLE_TIMESTAMP_FILTER = True

# Time filter traversal multiplier (stop searching when reaching N times the target count)
TIMESTAMP_FILTER_MULTIPLIER = 1.5

# Original target time range (days), passed from run_crawler.py
TARGET_TIME_RANGE_DAYS = 0

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
SAVE_DATA_OPTION = "excel"  # csv or db or json or jsonl or sqlite or excel or postgres

# Data saving path, if not specified by default, it will be saved to the data folder.
SAVE_DATA_PATH = ""

# Browser file configuration cached by the user's browser
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# The number of pages to start crawling starts from the first page by default
START_PAGE = 1

# Control the number of crawled videos/posts
CRAWLER_MAX_NOTES_COUNT = 3

# Controlling the number of concurrent crawlers
MAX_CONCURRENCY_NUM = 1

# Whether to enable crawling media mode (including image or video resources), crawling media is not enabled by default
ENABLE_GET_MEIDAS = True

# Whether to enable comment crawling mode. Comment crawling is enabled by default.
ENABLE_GET_COMMENTS = True

# Control the number of crawled first-level comments (single video/post)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 3

# Whether to enable the mode of crawling second-level comments. By default, crawling of second-level comments is not enabled.
# If the old version of the project uses db, you need to refer to schema/tables.sql line 287 to add table fields.
ENABLE_GET_SUB_COMMENTS = True

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
from .tavily_config import *
