

import cv2
import pyautogui
import time
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
movementTimeDuration = 0.0
min_x=2200
min_y=2000
max_x=0
max_y=0
mov_left=0
mov_right=0
prev_left=(500,500)
def mov_l(mov_left):
    if mov_left==1:
        mov_right=0
        cur_curr=pyautogui.position()
        pyautogui.moveTo(cur_curr[0]+20, cur_curr[1], duration = movementTimeDuration)
def mov_r(mov_right):
    if mov_right==1:
        mov_left=0
        cur_curr=pyautogui.position()
        pyautogui.moveTo(cur_curr[0]-20, cur_curr[1], duration = movementTimeDuration)        
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""
    if gaze.is_blinking():
        pyautogui.doubleClick()
        text = "Blinking"
    #     pyautogui.moveTo(toXPositon,600,duration = 0)
    #     timeout = time.time() + 5  # t seconds from now
    #     while True:
    #         test = 0
    #         if test == 5 or time.time() > timeout:
    #             break
    #         test = test - 1
    # elif gaze.is_right():
    #     text = "Looking right"
    #     pyautogui.moveTo(1800, 600, duration = movementTimeDuration) 
    # elif gaze.is_left():
    #     text = "Looking left"
    #     pyautogui.moveTo(200, 600, duration = movementTimeDuration) 
    # elif gaze.is_center():
    #     text = "Looking center"
    mov_l(mov_left)
    mov_r(mov_right)
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    cur_curr=pyautogui.position()
    if left_pupil is not None:
        # if left_pupil[1] < prev_left[1]:
        #     pyautogui.moveTo(cur_curr[0], cur_curr[1]-20, duration = movementTimeDuration)
        # else:
        #     pyautogui.moveTo(cur_curr[0], cur_curr[1]+20, duration = movementTimeDuration)               
        if left_pupil[0] < prev_left[0]:
            mov_left=1
            mov_right=0
        else: 
            mov_right=1
            mov_left=0            
        prev_left=left_pupil
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        print(min_x)
        print(min_y)
        print(max_x)
        print(max_y)
        break