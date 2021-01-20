# This is the server and FAR algorithm code you should run on your RPI
# Please configure your IP address and port number accordingly in the function get_HUE()

# Developer: Muhammad Shakeel and Moonjun

# For questions contact: Muhammad at omarshakil100@gmail.com

from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero
import socket
import re

def get_HUE():
    s = socket.socket()
    # Change your IP Here
    host = "192.168.219.156"
    port = 12338
    s.bind((host, port))
    s.listen(5)

    while True:
        try:
            clientsock, addr = s.accept()
        except OSError:
            continue
        message = clientsock.recv(1000)
        color=message.decode("utf-8")
    
        val=re.findall('\d+', color)

        print (val[0])
        return val[0]
        clientsock.close()
    
 
camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
camera.rotation=180
rawCapture = PiRGBArray(camera, size=(image_width, image_height))
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000
 
robot = gpiozero.Robot(left=(22,27), right=(17,18))
forward_speed = 0.8
turn_speed = 0.6
 
HUE_VAL = int(get_HUE())
print(HUE_VAL,"dahab")
 
lower_color = np.array([HUE_VAL-10,100,100])
upper_color = np.array([HUE_VAL+10, 255, 255])
 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
 
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
    color_mask = cv2.inRange(hsv, lower_color, upper_color)
 
    countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
 
    object_area = 0
    object_x = 0
    object_y = 0
 
    for contour in countours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        if object_area < found_area:
            object_area = found_area
            object_x = center_x
            object_y = center_y
    if object_area > 0:
        ball_location = [object_area, object_x, object_y]
    else:
        ball_location = None
 
    if ball_location:
        if (ball_location[0] > minimum_area) and (ball_location[0] < maximum_area):
            if ball_location[1] > (center_image_x + (image_width/3)):
                robot.right(turn_speed)
                print("Turning right")
            elif ball_location[1] < (center_image_x - (image_width/3)):
                robot.left(turn_speed)
                print("Turning left")
            else:
                robot.forward(forward_speed)
                print("Forward")
        elif (ball_location[0] < minimum_area):
            robot.left(turn_speed)
            print("Target isn't large enough, searching")
        else:
            robot.stop()
            print("Target large enough, stopping")
    else:
        robot.left(turn_speed)
        print("Target not found, searching")
 
    rawCapture.truncate(0)
