import ai绘画.提交任务
import ai绘画.查询
import ai绘画.取消任务
from 蓝心大模型 import lanxin
from ai绘画 import 提交任务
word = input()
lanxin.sync_vivogpt(word)
task_id = ai绘画.提交任务.submit(word)
draw_result = ai绘画.查询.progress(task_id)
is_finished_drawing = ai绘画.查询.progress(task_id)['result']['finished']
while is_finished_drawing == False:##1.为何已经是true了但还是在循环2.要设置回答不出来时的绘图策略3.提问的逻辑（画的是我问的还是它回答的）4.怎么实现持续性回答问题
    ai绘画.查询.progress(task_id)




