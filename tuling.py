# -*- coding: utf-8 -*-
import requests
import json


def tuling(info):
    api_url = 'http://www.tuling123.com/openapi/api'
    # 在这里插入你的API_KEY即可
    api_key = "0480791e014245bb92174577c11a779f"
    data = {'key': api_key,
                'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys
