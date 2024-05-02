import json
import webbrowser

import ai绘画.提交任务
import ai绘画.查询
import ai绘画.取消任务
from 蓝心大模型 import lanxin

word = input()
lanxin.sync_vivogpt(word)
task_id = ai绘画.提交任务.submit(word)
draw_result = None
is_finished_drawing = False

while (is_finished_drawing) == False: # 跳出该循环时，ai绘画已然完成
    draw_result, is_finished_drawing = ai绘画.查询.progress(task_id)

url_of_drawing = "".join(draw_result['result']['images_url'])      # 列表转字符串方法可不是str（）

webbrowser.open(url_of_drawing)

# print(draw_result['result'][])

# 2.要设置回答不出来时的绘图策略
# 3.提问的逻辑（画的是我问的还是它回答的）
# 4.怎么实现持续性回答问题




