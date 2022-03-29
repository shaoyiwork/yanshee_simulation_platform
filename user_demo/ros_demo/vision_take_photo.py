#!/usr/bin/env python3
#coding=utf-8

import rospy
import time
from ubt_msgs.srv import save_image

WAIT_TIME = 3

def vision_take_photo_client(path_name, quality):
    rospy.wait_for_service("camera_take_photo",WAIT_TIME)
    try:
        do_vision = rospy.ServiceProxy("camera_take_photo", save_image)
        res = do_vision(path_name, quality)
        return res
    except :
        rospy.logerr("Service call failed!")

if __name__ == '__main__':
    name_path = "/tmp/my_photo.jpg" #path you want to save
    quality = 50 #the image quality : int 1~100
    res = vision_take_photo_client(name_path, quality)
    print(res)
