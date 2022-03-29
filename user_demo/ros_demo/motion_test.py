#!/usr/bin/env python
#coding=utf-8

import rospy
import time
import json
from ubt_msgs.srv import motion_list
from ubt_msgs.srv import motion_play
from ubt_msgs.srv import motion_stop


def play_motion_client(name,repeat):
    rospy.wait_for_service('set_motion_play')
    try:
        do_motion = rospy.ServiceProxy('set_motion_play', motion_play)
        resp = do_motion(name,repeat)
        return resp.rc
    except :
        rospy.logerr("Service call failed!")

def stop_motion_client(name):
    rospy.wait_for_service('set_motion_stop')
    try:
        do_motion = rospy.ServiceProxy('set_motion_stop', motion_stop)
        resp = do_motion(name)
        return resp.rc
    except :
        rospy.logerr("Service call failed!")

def get_motion_client():
    rospy.wait_for_service('get_motion_list')
    try:
        get_motion = rospy.ServiceProxy('get_motion_list', motion_list)
        resp = get_motion()
        return resp
    except :
        rospy.logerr("Service call failed!")


if __name__ == '__main__':
    resp = get_motion_client()
    print(resp.name)
    play_motion_client(resp.name[6],1)
    #play_motion_client("WakaWaka",1)
    time.sleep(10)
    stop_motion_client("WakaWaka")
    #stop_motion_client("")
    time.sleep(2)
    play_motion_client("Reset",1)
