import YanAPI

#quantity | age_group | gender | age | expression | mask(口罩) | glass(眼镜)
res = YanAPI.sync_do_face_recognition("mask")
print(res)

#quantity | age_group | gender | age | expression | mask(口罩) | glass(眼镜)
res = YanAPI.sync_do_face_recognition_value("glass")
print(res)

