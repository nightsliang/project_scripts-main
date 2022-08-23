#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
sys.setrecursionlimit(10000000)
import traceback
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 发送钉钉消息通知
def send_dingding(task, msg, args='!!'):
    Headers = {
        'Content-Type': 'application/json'
    }

    MSG = f"""TASK_NAME :   {task} 
INFO:   {msg} 
MSG:   {args}
"""

    data = {
        "msgtype": "text",
        "text": {
            "content": MSG
        },
        "at": {
            "atMobiles": [
                # "15999957156",
            ],
        }
    }

    URL = "https://oapi.dingtalk.com/robot/send?access_token=7f147783c3f17bef1e6095a238ad3c202ef9c6a688fe030ed865601b62d19398"
    try:
        requests.post(URL, headers=Headers, data=json.dumps(data), timeout=9.1)
    except:

        traceback.print_exc()
    print('钉钉')


if __name__ == '__main__':
    send_dingding('测试', '这是一条测试推送', args='!!')
