#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from ubt_msgs.srv import vision_task_set
from ubt_msgs.srv import vision_result

WAIT_TIME = 3

def set_vision_task_client(task,data):
    rospy.wait_for_service(task,WAIT_TIME)
    try:
        do_vision = rospy.ServiceProxy(task, vision_task_set)
        resp = do_vision(data)
        return resp.rc
    except :
        rospy.logerr("Service call failed!")

def get_vision_result_client(task,srv):
    rospy.wait_for_service(task,WAIT_TIME)
    try:
        get_vision = rospy.ServiceProxy(task, srv)
        res = get_vision()
        return res
    except :
        rospy.logerr("Service call failed!")


if __name__ == '__main__':
    set_vision_task_client("color_recognition_task","start")
    while True:
        res = get_vision_result_client("color_rec_result",vision_result)
        if(res.status == "idle"):
            print("color: " + res.result)
            print(res.local_info)
            exit(0)

