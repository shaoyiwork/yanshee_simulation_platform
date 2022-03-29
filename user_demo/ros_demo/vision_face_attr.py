#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from ubt_msgs.srv import vision_task_set
from ubt_msgs.srv import vision_face_attr_result

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
    set_vision_task_client("face_attribute_task","start")
    while True:
        res = get_vision_result_client("face_attr_result",vision_face_attr_result)
        if(res.status == "idle"):
            #print(res.result)
            if len(res.result)>0:
                if(res.result[0].mask == "none"):
                    face_num = 0
                else :
                    face_num = len(res.result)
            print("face_num: " + str(face_num))
            print("age: "+ str(res.result[0].age))
            print("age_group: "+ res.result[0].age_group)
            print("gender: "+ res.result[0].gender)
            print("glass: "+ res.result[0].glass)
            print("mask: "+ res.result[0].mask)
            print("expression: "+ res.result[0].expression)
            exit(0)
