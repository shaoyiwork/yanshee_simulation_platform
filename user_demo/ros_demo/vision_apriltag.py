#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
import math
from ubt_msgs.srv import ctrl_april_tag_continuous_detector
from ubt_msgs.srv import check_april_tag_status
from ubt_msgs.msg import StandaloneTag

WAIT_TIME = 3

def set_apriltag_task_client(enable,tags,enable_stream):
    rospy.wait_for_service("april_tag_detector_task",WAIT_TIME)
    try:
        do_vision = rospy.ServiceProxy("april_tag_detector_task", ctrl_april_tag_continuous_detector)
        resp = do_vision(enable,tags,enable_stream)
        return resp.rc
    except :
        rospy.logerr(" Service task call failed!")
def get_apriltag_result_client():
    rospy.wait_for_service("april_tag_result",WAIT_TIME)
    try:
        get_vision = rospy.ServiceProxy("april_tag_result", check_april_tag_status)
        res = get_vision()
        return res
    except :
        rospy.logerr("Service reault call failed!")


if __name__ == '__main__':
    tag =  StandaloneTag()
    tag_list = []
    tag.id = 13
    tag.size = 0.021
    tag_list.append(tag) 
    set_apriltag_task_client(True,tag_list,True)
    time.sleep(1)
    while True:
        res = get_apriltag_result_client()
        #print(res)
        time.sleep(5)
        if(res.enable == True):
            #print(res.april_tag_status.detections)
            if(len(res.april_tag_status.detections) == 0):
                print("not found...")
                continue
            aprilTag_list = []
            for detection in res.april_tag_status.detections:
                aprilTag = {}
                aprilTag["id"] =  detection.id[0]
                aprilTag["position-x"] = detection.pose.pose.pose.position.x
                aprilTag["position-y"] = detection.pose.pose.pose.position.y
                aprilTag["position-z"] = detection.pose.pose.pose.position.z
                aprilTag["orientation-x"] = detection.pose.pose.pose.orientation.x
                aprilTag["orientation-y"] = detection.pose.pose.pose.orientation.y
                aprilTag["orientation-z"] = detection.pose.pose.pose.orientation.z
                aprilTag["orientation-w"] = detection.pose.pose.pose.orientation.w
                aprilTag_list.append(aprilTag)
            print(aprilTag_list)
            for followTag in aprilTag_list:
                if followTag["id"] == 13:
                    ## 四元组转换为欧拉角
                    w = followTag["orientation-w"]
                    x = followTag["orientation-x"]
                    y = followTag["orientation-y"]
                    z = followTag["orientation-z"]
                    r = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))
                    p = math.asin(2*(w*y-z*x))
                    y = math.atan2(2*(w*z+x*y),1-2*(z*z+y*y))
                    angleR = r*180/math.pi
                    angleP = p*180/math.pi
                    angleY = y*180/math.pi
                    print(angleP)
                    ##正向距离
                    distance = followTag["position-z"]
                    print("distance: " + str(distance))

