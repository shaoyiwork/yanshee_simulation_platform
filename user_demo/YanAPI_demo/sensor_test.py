import YanAPI

def test_get_sensors_list_value():
    res = YanAPI.get_sensors_list_value()
    print(res)
def test_get_sensors_list():
    res = YanAPI.get_sensors_list()
    print(res)
def test_get_sensors_gyro():
    res = YanAPI.get_sensors_gyro()
    print(res["data"]["gyro"])
def test_get_sensors_infrared_value():
    res = YanAPI.get_sensors_infrared_value()
    print(res)
def test_get_sensors_infrared():
    res = YanAPI.get_sensors_infrared()
    for key in res["data"]["infrared"]:
        print(key["name"]+" : "+str(key["value"]))

if __name__ == '__main__':
    test_get_sensors_list_value()
    test_get_sensors_gyro()
    test_get_sensors_infrared()
