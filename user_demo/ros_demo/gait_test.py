#!/usr/bin/env python
#coding=utf-8

import rospy
import time
import json
from std_msgs.msg import Float32
from ubt_msgs.srv import string_set
from ubt_msgs.msg import gait_para
from ubt_msgs.srv import gait_operation


def do_gait_client(data):
    rospy.wait_for_service('set_gait_play')
    try:
        do_gait = rospy.ServiceProxy('set_gait_play', gait_operation)
        resp = do_gait(data)
        return resp.rc
    except :
        rospy.logerr("Service call failed!")


if __name__ == '__main__':
        para = gait_para()
        para.period = 5 # int 1-5
        para.speed_v = 5 # int -5~0 backward 0~5 forward
        para.speed_h = 0 
        para.wave = False # bool : wave hand or not 
        para.steps = 20  # walk steps
        para.timestamp = int(time.time() * 1000)
        do_gait_client(para)
