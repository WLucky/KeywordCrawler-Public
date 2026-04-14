# -*- coding: utf-8 -*-
"""
直接测试修复后的 JavaScript 代码
"""

import execjs

# 读取并编译 JavaScript 文件
with open('libs/douyin.js', encoding='utf-8-sig') as f:
    js_code = f.read()

douyin_sign_obj = execjs.compile(js_code)

# 测试参数
params = "device_platform=webapp&aid=6383&channel=channel_pc_web&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7362810250930783783&msToken=VkDUvz1y24CppXSl80iFPr6ez-3FiizcwD7fI1OqBt6IICq9RWG7nCvxKb8IVi55mFd-wnqoNkXGnxHrikQb4PuKob5Q-YhDp5Um215JzlBszkUyiEvR"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

print("测试修复后的 JavaScript 代码...")
try:
    # 测试 sign_datail 函数
    result1 = douyin_sign_obj.call("sign_datail", params, user_agent)
    print(f"测试 sign_datail 成功！结果: {result1}")
    
    # 测试 sign_reply 函数
    result2 = douyin_sign_obj.call("sign_reply", params, user_agent)
    print(f"测试 sign_reply 成功！结果: {result2}")
    
    print("\n修复成功！JavaScript 代码现在可以正常执行了。")
except Exception as e:
    print(f"测试失败！错误信息: {e}")
