#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3031377531'
APP_KEY = 'BZwGpQORFJKNHWnV'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'


def progress(task_id = None):
    params = {
        # 注意替换为提交作画任务时返回的task_id
        'task_id': task_id
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    uri_params = ''
    for key, value in params.items():
        uri_params = uri_params + key + '=' + value + '&'
    uri_params = uri_params[:-1]

    url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
    ## print('url:', url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.json())
        return response.json(),response.json()['result']['finished']
    else:
        # print(response.status_code, response.text)
        return None,False  # 这里一定注意需要返回值，否则会报错TypeError: cannot unpack non-iterable NoneType object


if __name__ == '__main__':
    progress()
