#!/usr/bin/env python
#coding=utf-8

import time
import rospy
from ubt_msgs.srv import led_write
from ubt_msgs.msg import led

def led_handle_client(x):
    led_function = rospy.ServiceProxy('set_led',led_write)
    resp = led_function(x)
    return resp.rc

def head_led_set():
    led.name = "camera"
    led.mode = "on"
    led.value = "red"
    led_handle_client(led)

def head_led_normal():
    led.name = "camera"
    led.mode = "on"
    led.value = "blue"
    led_handle_client(led)

def button_led_set():
    led.name = "button"
    led.mode = "breath"
    led.value = "red"
    led_handle_client(led)

def button_led_normal():
    led.name = "button"
    led.mode = "breath"
    led.value = "blue"
    led_handle_client(led)

if __name__ == "__main__":
    rospy.loginfo("---This is a LED test for Yanshee robot by Ros API---")
    button_led_set()
    time.sleep(3)
    button_led_normal()
    time.sleep(3)
    head_led_set()
    time.sleep(3)
    head_led_normal()
