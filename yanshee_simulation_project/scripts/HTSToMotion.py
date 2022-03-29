import sys
import os

HTS_BYTE = 33
SERVO = 17
MCU_TIME_LEVEL = 20 # 20ms
AVERAGE_BYTE = 1
PI = 3.14

servo_name = [
	"RShoulderPitchMotor",
	"RShoulderYawMotor",
	"RElbowYawMotor",
	"LShoulderPitchMotor",
	"LShoulderYawMotor",
	"LElbowYawMotor",
	"RHipYawMotor",
	"RHipPitchMotor",
	"RKneePitchMotor",
	"RAnklePitchMotor",
	"RAnkleYawMotor",
	"LHipYawMotor",
	"LHipPitchMotor",
	"LKneePitchMotor",
	"LAnklePitchMotor",
	"LAnkleYawMotor",
	"KneckRollMotor"
]

def calcuteTime(time):
	str_time = ""
	# minus
	minus = int(time/60000)
	if minus > 9:
		str_time = str(minus)
	else:
		str_time = "0" + str(minus)
	str_time += ":"
	# seconds
	seconds = int((time - minus * 60000)/1000)
	if seconds > 9:
		str_time += str(seconds)
	else:
		str_time += ("0" + str(seconds))
	str_time += ":"
	miliseconds = (time - minus * 60000 - seconds * 1000)
	if miliseconds > 99:
		str_time +=  str(miliseconds)
	elif miliseconds > 9 and miliseconds <= 99:
		str_time += ("0" + str(miliseconds))
	else:
		str_time += ("00" + str(miliseconds))
	return str_time + ","

def calculatePose(frame):
	return "Pose" + str(frame) + ","

def calculateAngle(servo):
	str_servo = ""
	for i in range(0, len(servo)):
		if servo[i] != -1:
			str_servo += (str(round(servo[i]/180*PI, 5)) + ",")
	return str_servo[0:len(str_servo)-1] + "\n"


if __name__ == '__main__':
	# sys.argv[1] --> .hts abs file
	# sys.argv[2] --> destination dir
	# Remember ff means nothing, but in motion file, we do not add such 
	#try:
	on_first = True
	elapsed_time = 0
	frame = 1
	hts_name = sys.argv[1].rsplit('/')[-1].rsplit('.')[0]
	motion_dir = sys.argv[2] + hts_name + ".motion"
	print("open target hts %s" % sys.argv[1])
	hts_file = open(sys.argv[1],'rb+')
	print("open target motion %s" % motion_dir)
	motion_file = open(motion_dir, "wb+")
	servo = [ -1 for i in range(SERVO) ]
	hts_file.seek(HTS_BYTE, 0)
	line = "#WEBOTS_MOTION,V1.0,"
	while True:
		data = hts_file.read(HTS_BYTE)
		if data[0] != 0xfb:
			break;
		for i in range(0, SERVO):
			if data[8 + i] != 0xff:
				if on_first:
					line += (servo_name[i] + ",")
				servo[i] = data[8 + i]
		if on_first:
			# write servo name
			motion_file.write(bytes(line[0:len(line) - 1] + "\n", encoding='utf-8'))
			on_first = False
		line = ""
		# runtime = (data[28] + (AVERAGE_BYTE * 0xff + 1) * data[27]) * MCU_TIME_LEVEL
		# totaltime = (data[30] + (AVERAGE_BYTE * 0xff + 1) * data[29]) * MCU_TIME_LEVEL
		runtime = (data[28]) * MCU_TIME_LEVEL
		totaltime = (data[30] + (AVERAGE_BYTE * 0xff + 1) * data[29]) * MCU_TIME_LEVEL
		elapsed_time += runtime
		if frame == 1:
			elapsed_time = 0
		line += calcuteTime(elapsed_time)
		line += calculatePose(frame)
		line += calculateAngle(servo)
		motion_file.write(bytes(line[0:len(line)], encoding='utf-8'))
		frame += 1
		if totaltime - runtime == 0:
			continue
		line = ""
		elapsed_time += (totaltime - runtime)
		line += calcuteTime(elapsed_time)
		line += calculatePose(frame)
		line += calculateAngle(servo)
		motion_file.write(bytes(line[0:len(line)], encoding='utf-8'))
		frame += 1
	motion_file.close()
	hts_file.close()
	print("finish convert")
	#except:
	#	print("something wrong, exit")
