import cv2
import numpy as np
import dlib
from math import hypot

import time


import random


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

   
