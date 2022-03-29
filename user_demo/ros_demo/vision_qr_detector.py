#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from ubt_msgs.srv import ctrl_qr_detector
from ubt_msgs.srv import check_qr_status

WAIT_TIME = 3

def set_qr_task_client(enable,enable_stream):
    rospy.wait_for_service("qr_detector_task",WAIT_TIME)
    try:
        do_vision = rospy.ServiceProxy("qr_detector_task", ctrl_qr_detector)
        resp = do_vision(enable,enable_stream)
        return resp.rc
    except :
        rospy.logerr("Service call failed!")
def get_qr_result_client():
    rospy.wait_for_service("qr_detector_result",WAIT_TIME)
    try:
        get_vision = rospy.ServiceProxy("qr_detector_result", check_qr_status)
        res = get_vision()
        return res
    except :
        rospy.logerr("Service call failed!")


if __name__ == '__main__':
    res = set_qr_task_client(True,True)
    while True:
        res = get_qr_result_client()
        time.sleep(1)
        if(res.enable == True):
            if(len(res.contents)>0):
                print(res.contents)
                exit(0)
            else:
                print("not found...")
