import cv2
import numpy as np
import dlib
from math import hypot

import time



import random





cap = cv2.VideoCapture(0) #to capture video
board = np.zeros((300, 700), np.uint8) #lower and upper bound of keyboard to shape the dataset and 
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")



   


def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))


    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio




while True:


  while True :

     
  
    
    
    
    _, frame = cap.read()
   
    rows, cols, _ = frame.shape

    keyboard[:] = (26, 26, 26)
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw a white space for loading bar
    frame[rows - 50: rows, 0: cols] = (255, 255, 255)

    if select_keyboard_menu is True:
        draw_menu()

    # Keyboard selected
    if keyboard_selected == "left":
        keys_set = keys_set_1

    active_letter = keys_set[letter_index]

    # Face detection
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        left_eye, right_eye = eyes_contour_points(landmarks)

        # Detect blinking
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # Eyes color
        cv2.polylines(frame, [left_eye], True, (0, 0, 255), 2)
        cv2.polylines(frame, [right_eye], True, (0, 0, 255), 2)


        if select_keyboard_menu is True:
            # Detecting gaze to select Left or Right keybaord
            gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
            gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
            gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
            print(gaze_ratio)

            if gaze_ratio <= 5:
                keyboard_selected = "right"
                keyboard_selection_frames += 1
                # If Kept gaze on one side more than 15 frames, move to keyboard
                if keyboard_selection_frames == 15:
                    select_keyboard_menu = False
##                    right_sound.play()
                    # Set frames count to 0 when keyboard selected
                    frames = 0
                    keyboard_selection_frames = 0
                if keyboard_selected != last_keyboard_selected:
                    last_keyboard_selected = keyboard_selected
                    keyboard_selection_frames = 0


        else:
            # Detect the blinking to select the key that is lighting up
            if blinking_ratio > 5:
                # cv2.putText(frame, "BLINKING", (50, 150), font, 4, (255, 0, 0), thickness=3)
                blinking_frames += 1
                frames -= 1

                # Show green eyes when closed
                cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
                cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)

                # Typing letter
                if blinking_frames == frames_to_blink:
                    if active_letter != "E" and active_letter != "C":
                        count=count+1
                        text += active_letter
                        text1.append(active_letter)
                        print('text1 {}'.format(text1))
                    if active_letter == "E" or active_letter == "C" :
                        text += " "

                        count=count-1
                        text1.pop(count)
                        print('del {}'.format(text1))

                    text += " "
                    print(text)
            

            else:
                blinking_frames = 0


    # Display letters on the keyboard
    if select_keyboard_menu is False:
        if frames == frames_active_letter:
            letter_index += 1
            frames = 0
        if letter_index == 11:
            letter_index = 0
        for i in range(11):
            if i == letter_index:
                light = True
            else:
                light = False
            draw_letters(i, keys_set[i], light)

    # Show the text we're writing on the board
    cv2.putText(board, str(text1), (80, 100), font, 9, 0, 3)

    # Blinking loading bar
    percentage_blinking = blinking_frames / frames_to_blink
    loading_x = int(cols * percentage_blinking)
    cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (51, 51, 51), -1)


    cv2.imshow("Frame", frame)
    cv2.imshow("Virtual keyboard", keyboard)
##    cv2.imshow("Board", board)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

##    key = cv2.waitKey(1)
##    if key == 27:
##        break

cap.release()
cv2.destroyAllWindows()
