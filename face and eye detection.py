import cv2
import numpy as np
import dlib
from math import hypot

import time


import random


cap = cv2.VideoCapture(0) 
board = np.zeros((300, 700), np.uint8) 
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Keyboard settings
keyboard = np.zeros((1000, 800, 3), np.uint8)


keys_set_1 = {0: "1", 1: "2", 2: "3",
              3: "E",4: "4", 5: "5",
              6: "6", 7: "C",8: "7",
              9: "8", 10: "9",11:"0",12:"2"}



def draw_letters(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 200
        y = 0
    elif letter_index == 2:
        x = 400
        y = 0
    elif letter_index == 3:
        x = 600
        y = 0
    elif letter_index == 4:
        x = 0
        y = 200
    elif letter_index == 5:
        x = 200
        y = 200
    elif letter_index == 6:
        x = 400
        y = 200
    elif letter_index == 7:
        x = 600
        y = 200
    elif letter_index == 8:
        x = 0
        y = 400
    elif letter_index == 9:
        x = 200
        y = 400
    elif letter_index == 10:
        x = 400
        y = 400
    elif letter_index == 11:
        x = 600
        y = 400
    elif letter_index == 12:
       x = 0
       y = 600

    width = 200
    height = 200
    th = 3 # thickness

    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 9
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y

    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (51, 51, 51), font_th)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (51, 51, 51), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 255, 255), font_th)

def draw_menu():
    rows, cols, _ = keyboard.shape
    th_lines = 4 
def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_PLAIN


    

def eyes_contour_points(facial_landmarks):
    left_eye = []
    right_eye = []
    for n in range(36, 42):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        left_eye.append([x, y])
    for n in range(42, 48):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        right_eye.append([x, y])
    left_eye = np.array(left_eye, np.int32)
    right_eye = np.array(right_eye, np.int32)
    return left_eye, right_eye



# Text and keyboard settings
text = "" 
text1=[] #empty list
keyboard_selected = "left"
last_keyboard_selected = "left"
select_keyboard_menu = True
keyboard_selection_frames = 0
count=0
pf =[]

scanned=0

once=1
scanned =1
