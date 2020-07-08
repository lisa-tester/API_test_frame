"""
用requests完成论坛注册
"""


import requests
import re
from collections import OrderedDict

# 论坛主机地址
hosts = 'http://47.107.178.45'
# 使用requests的session方法创建session对象
session = requests.session()

# ----------------  01、进入论坛首页
# 请求地址
res01 = session.get(url=hosts + '/phpwind/')
# 响应内容
body01 = res01.content.decode('utf-8')
# 使用正则表达式来获取响应数据中的内容（取筛选出来的第一个--可能有多个值）
csrf_token = re.findall('name="csrf_token" value="(.+?)"/>', body01)[0]
# print(csrf_token)

# --------------------02、进入注册页面
# 请求参数
get_params = {
    "m": "u",
    "c": "register"
}
# 使用头信息将打印内容以其他格式输出，不加默认显示HTML格式
headers_info = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
# 请求
res02 = session.get(url=hosts+'/phpwind/index.php',
                    params=get_params,
                    headers=headers_info
                    )
# 请求响应内容
body02 = res02.content.decode('utf8')
# print(body02)


# ---------------------3、注册
# 请求参数
get_params = {
    "m": "u",
    "c": "login",
    "a": "dorun"
}
# 请求正文
data = {
    "username": "xxl",
    "password": "123456",
    "repassword": "123456",
    "email": "",
    "csrf_token": csrf_token
}
# 头信息
headers_info = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
# 请求
res03 = session.post(url=hosts+'/phpwind/index.php',
                     params=get_params,
                     data=data,
                     headers=headers_info
                     )
# 请求响应内容
body03 = res03.content.decode('utf8')
print(body03)


