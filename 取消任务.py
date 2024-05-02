import requests
import base64
import json
import uuid
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3031377531'
APP_KEY = 'BZwGpQORFJKNHWnV'
URI = '/api/v1/task_cancel'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

def cancel():
   params = {}
   data = {
    'dataId': str(uuid.uuid4()),
    'businessCode': 'pc',
    # 注意替换为提交作画任务时返回的task_id
    'task_id': '555f7f94287857589fa2bb48f19e8b5a'
   }

   headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
   headers['Content-Type'] = 'application/json'

   url = 'http://{}{}'.format(DOMAIN, URI)
   response = requests.post(url, data=json.dumps(data), headers=headers)
   if response.status_code == 200:
       print(response.json())
   else:
       print(response.status_code, response.text)

if __name__ == '__main__':
   cancel()