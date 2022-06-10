from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep

picar.setup()
pan_tilt_enable	= True

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()

pan_servo_offset = 0
tilt_servo_offset = 0

for x in range(45,135,5):
	print(x)
	fw.turn(x)
	sleep(0.5)

for x in range(45,135,5):
	print(x)
	pan_servo.write(x)
	sleep(0.5)

for x in range(45,135,5):
	print(x)
	tilt_servo.write(x)
	sleep(0.5)
