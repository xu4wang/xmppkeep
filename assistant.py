#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import time
import json
import traceback

__redis_instance = None

def get_redis():
    global __redis_instance
    if not __redis_instance:
        __redis_instance = redis.Redis(host='127.0.0.1',port=6379,db=0)
    return  __redis_instance

#create one dict with 3 keys, time, list and content
#LPUSH the dict into redis queue named token.
def process_message_with_path(token, path, msg):
    global __redis_instance
    r = get_redis()
    d = {}
    d["time"] = time.time()
    d["list"] = path
    d["content"] = msg
    data = json.dumps(d)
    try:
        r.lpush(token,data)
    except:
        __redis_instance = None
        err_msg = traceback.format_stack()
        return str(err_msg)
    else:
        return "OK"
