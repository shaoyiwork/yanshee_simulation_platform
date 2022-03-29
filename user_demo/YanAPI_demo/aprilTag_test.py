import YanAPI
import math
import time
import threading

tags=[{"id":10,"size":0.021},{"id":13,"size":0.021}]
ret = YanAPI.start_aprilTag_recognition(tags,True)
print(ret)

timer = None
def do_recognition():
    global timer
    ret = YanAPI.get_aprilTag_recognition_status()
    print(ret)
    if ret["code"]==0 and ret["status"]=='run':
        timer = threading.Timer(5, do_recognition)
        timer.start()
        followTag = None
        for aprilTagStatus in ret['data']["AprilTagStatus"]:
            if aprilTagStatus["id"] == 13:
                followTag = aprilTagStatus
        if followTag is not None:
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
            print(distance)
timer = threading.Timer(5, do_recognition)
timer.start()

#ret = YanAPI.stop_aprilTag_recognition()
#print(ret)
