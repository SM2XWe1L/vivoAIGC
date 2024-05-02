#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3031377531'
APP_KEY = 'BZwGpQORFJKNHWnV'
URI = '/api/v1/task_submit'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

def submit(content):
   params = {}
   data = {
    'height': 768,
    'width': 576,
    'prompt': content,
    'styleConfig': '8fe3d641be3e589dad231dc6c3b1429a',
    'denoisingStrength':1
   }

   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
   headers['Content-Type'] = 'application/json'

   url = 'http://{}{}'.format(DOMAIN, URI)
   response = requests.post(url, data=json.dumps(data), headers=headers)
   if response.status_code == 200:
       # print(response.json())
       return response.json()['result']['task_id']
   else:
       # print(response.status_code, response.text)
       return None


if __name__ == '__main__':
   submit()
