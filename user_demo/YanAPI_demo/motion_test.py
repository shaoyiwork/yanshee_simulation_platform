import YanAPI
import time

res = YanAPI.get_motion_list_value()
print(res)

#res = YanAPI.sync_play_motion(name="Victory", repeat=1)
#print(res)

res = YanAPI.start_play_motion(name="WakaWaka", repeat=1)
print(res)

time.sleep(3)

res = YanAPI.stop_play_motion(name = "WakaWaka")
print(res)

time.sleep(1)

YanAPI.sync_play_motion(name="Reset")
