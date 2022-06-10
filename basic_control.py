from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import sys,tty,os,termios
import cv2


picar.setup()
pan_tilt_enable	= True

bw = back_wheels.Back_Wheels()
fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)
picar.setup()

pan_servo_offset = 0
tilt_servo_offset = 0



pos_min = 45
pos_max = 135
pan_pos = 90
tilt_pos = 90
speed = 0
drive_state = 0 
fw_pos = 90

drive_change = False
speed_change = False
fw_change = False
pan_change = False
tilt_change = False


def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) >= 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left',
		119: 'w',
		97: 'a',
		115: 's',
		100: 'd',
                49: '1',
		50: '2',
		51: '3',
		52: '4',
		53: '5'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
try:
    while True:
        k = getkey()
        if k == 'esc':
            quit()
        if k == 'left':
            if (pan_pos < pos_max):
                pan_pos+=5
            pan_change = True;
        if k == 'right':
            if (pan_pos > pos_min):
                pan_pos-=5
            pan_change = True;
        if k == 'up':
            if (tilt_pos < pos_max):
                tilt_pos+=5
            tilt_change = True;
        if k == 'down':
            if (tilt_pos > pos_min):
                tilt_pos-=5
            tilt_change = True;
        if k == 'w':
            drive_state = -1
            drive_change = True
        if k == 's':
            drive_state = 1
            drive_change = True
        if k == 'space':
            drive_state = 0 
            drive_change = True
        if k == 'a':
            if (fw_pos > pos_min):
                fw_pos-=5
            fw_change = True;
        if k == 'd':
            if (fw_pos < pos_max):
                fw_pos+=5
            fw_change = True;
        if k == '0':
            speed=0
            speed_change=True
        if k == '1':
            speed=10
            speed_change=True
        if k == '2':
            speed=20
            speed_change=True
        if k == '3':
            speed=30
            speed_change=True
        if k == '4':
            speed=40
            speed_change=True
        if k == '5':
            speed=50
            speed_change=True
        else:
            print(k)

        if (pan_change):
            print("Pan: ", pan_pos)
            pan_servo.write(pan_pos)
            pan_change = False
        if (tilt_change):
            print("Tilt: ", tilt_pos)
            tilt_servo.write(tilt_pos)
            tilt_change = False
        if (speed_change):
            print("Speed: ", speed)
            bw.speed = speed
            speed_change = False
        if (drive_change):
            print("Drive: ", drive_state)
            if (drive_state == 0):
                bw.speed = 0 
                bw.stop()
            if (drive_state == 1):
                bw.speed = speed
                bw.forward()
            if (drive_state == -1):
                bw.speed = speed
                bw.backward()
            drive_change = False
        if (fw_change):
            print("FW Position: ", fw_pos)
            fw.turn(fw_pos)
            fw_change = False

except (KeyboardInterrupt, SystemExit):
    os.system('stty sane')
    print('stopping.')


#for x in range(45,135,5):
#	print(x)
#	fw.turn(x)
#	sleep(0.5)
#
#for x in range(45,135,5):
#	print(x)
#	pan_servo.write(x)
#	sleep(0.5)
#
#for x in range(45,135,5):
#	print(x)
#	tilt_servo.write(x)
#	sleep(0.5)
