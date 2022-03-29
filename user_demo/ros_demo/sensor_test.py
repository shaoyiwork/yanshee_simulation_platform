#!/usr/bin/env python
#coding=utf-8

import time
import rospy
from ubt_msgs.srv import imu_read
from ubt_msgs.srv import get_float

WAIT_TIME = 3

def get_imu_client():
    rospy.wait_for_service('get_imu_data',WAIT_TIME)
    try:
        read_imu = rospy.ServiceProxy('get_imu_data', imu_read)
        resp = read_imu()
        return resp
    except :
        rospy.logerr("Service call failed!")

def get_left_infrared_client(val=True):
    rospy.wait_for_service('distance_left_get_value',WAIT_TIME)
    try:
        read_dis = rospy.ServiceProxy('distance_left_get_value', get_float)
        resp = read_dis(val)
        return resp
    except :
        rospy.logerr("Service call failed!")

def get_right_infrared_client(val=True):
    rospy.wait_for_service('distance_right_get_value',WAIT_TIME)
    try:
        read_dis = rospy.ServiceProxy('distance_right_get_value', get_float)
        resp = read_dis(val)
        return resp
    except :
        rospy.logerr("Service call failed!")

def show_imu_result(res):
    _data = res.data
    gyroD = {}
    gyroD['accel-x'] = _data.imu.linear_acceleration.x
    gyroD['accel-y'] = _data.imu.linear_acceleration.y
    gyroD['accel-z'] = _data.imu.linear_acceleration.z
    gyroD['gyro-x'] = _data.imu.angular_velocity.x
    gyroD['gyro-y'] = _data.imu.angular_velocity.y
    gyroD['gyro-z'] = _data.imu.angular_velocity.z
    gyroD['compass-x'] = _data.compass.magnetic_field.x
    gyroD['compass-y'] = _data.compass.magnetic_field.y
    gyroD['compass-z'] = _data.compass.magnetic_field.z
    gyroD['euler-x'] = _data.euler.euler_x
    gyroD['euler-y'] = _data.euler.euler_y
    gyroD['euler-z'] = _data.euler.euler_z
    print(gyroD)

if __name__ == '__main__':
   res = get_imu_client()
   show_imu_result(res)
   res = get_left_infrared_client()
   print("dis_left:" + str(int(res.value)))
   res = get_right_infrared_client()
   print("dis_right:" + str(int(res.value)))
