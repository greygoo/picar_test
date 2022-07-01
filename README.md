# picar_test
just a bunch of scripts for playing around with the sunfounder picar-V

## camera_stream

### Setup (raspbian os):
sudo apt-get install libgl1-mesa-glx python3-pip
pip3 install numpy imutils opencv opencv-python flask

### Run
`cd camera_stream ; python3 webstreaming.py -i 0.0.0.0 -o 8080`

### access:
http://<ip of picar>:8080

## basic_control

### Run
`python3 basic_control.py`

### Controls

Arrow keys: Camera

WASD: Driving

Space: Stop
