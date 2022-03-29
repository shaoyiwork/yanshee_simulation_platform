import YanAPI
import time

res = YanAPI.get_servos_angles(["RightShulderFlex","NeckLR"])
print(res["data"])

time.sleep(2)

res = YanAPI.set_servos_angles({"NeckLR":90,"RightShulderFlex":140})
print(res["data"])
