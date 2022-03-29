#!/usr/bin/env python
#coding=utf-8

import rospy
import time
import json
from std_msgs.msg import Float32
from ubt_msgs.msg import servo_read
from ubt_msgs.msg import servo_write
from ubt_msgs.msg import servo_write_list
from ubt_msgs.srv import servo_read_list
from ubt_msgs.srv import string_set

servo_read_req = [
        "RightShoulderRoll",
        "RightElbowFlex",
        "RightShoulderFlex",
        "NeckLR",
        "LeftShoulderRoll",
        "LeftShoulderFlex",
        "LeftElbowFlex",
        "RightHipLR",
        "RightHipFB",
        "RightKneeFlex",
        "RightAnkleFB",
        "RightAnkleUD",
        "LeftHipLR",
        "LeftHipFB",
        "LeftKneeFlex",
        "LeftAnkleFB",
        "LeftAnkleUD"
]

servo_read_two = ["NeckLR","LeftHipLR"]

servo_read_head = ["NeckLR"]

def init():
        rospy.init_node('motor_talker', anonymous=True)
        pub = rospy.Publisher('/hal_servo_write', servo_write_list, queue_size=10)
        srv = rospy.ServiceProxy('/hal_servo_read', servo_read_list)
        return pub, srv
def talk(value, pub):
        pub.publish(value)

def request(service, data):
        reply = service(data)
        print(reply.data)
        print(reply.data[0].name)
        print(reply.data[0].angle)

def set_head_angle(value):
	info = servo_write()
	info_list = servo_write_list()
	info.name = "NeckLR"
	info.angle = value
	info.runtime = 20 #ms
	info_list.data.append(info)
	talk(info_list, pub)

if __name__ == '__main__':
        pub, srv = init()
        request(srv,servo_read_head)
        info = servo_write()
        info_list = servo_write_list()
        tmp_angle = 0
        counter = 0
        while counter < 12:
                print("send...")
                set_head_angle(tmp_angle)
                if(counter < 6):
                        tmp_angle+=30
                else:
                        tmp_angle-=30
                counter += 1
                time.sleep(1)
        set_head_angle(90)
