import requests

hosts = 'https://api.weixin.qq.com'
# ---------获取token
params = {
    'grant_type':'client_credential',
    'appid': 'wx55614004f367f8ca',
    'secret': '65515b46dd758dfdb09420bb7db2c67f'
}
res01 = requests.get(url=hosts+'/cgi-bin/token',
                     params=params
                     )
token_id = res01.json()['access_token']

# -----------创建一个标签
get_params = {
    'access_token': token_id
}
post_params = '{ "tag" : { "name" : "newdream111777" } }'
headers = {
    'content_type': 'application/json'
}
res02 = requests.post(url=hosts+'/cgi-bin/tags/create',
                      params=get_params,
                      data=post_params,
                      headers=headers
                       )
print(res02.json())