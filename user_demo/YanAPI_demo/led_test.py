import YanAPI
import time

YanAPI.set_robot_led("button","yellow","blink")
time.sleep(3)
YanAPI.set_robot_led("button","blue","breath")

time.sleep(1)
YanAPI.set_robot_led("camera","red","blink")
time.sleep(3)
YanAPI.set_robot_led("camera","blue","on")
