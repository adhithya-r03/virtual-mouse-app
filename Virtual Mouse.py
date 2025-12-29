import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import win32api
import mediapipe as mp
import pyautogui
import time
import subprocess
import tkinter.font as font

mp_hands = mp.solutions.hands
def proces():
    cap = cv2.VideoCapture(1)
    if not (cap.isOpened()):
        cap = cv2.VideoCapture(0)
    hand_detector = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8,
                                             min_tracking_confidence=0.8)  # from the hand solution calling hand method
    drawing_utils = mp.solutions.drawing_utils  # it used to draw the hand landmarks
    screen_w, screen_h = pyautogui.size()  # getting the size of the screen
    ind_y = 0  # when thumb_y is close to index_y then it make a click
    smooth = 5
    ploc_x, ploc_y = 0, 0
    cloc_x, cloc_y = 0, 0
    framer = 170
    wcam, hcam = 640, 480
    wscr, hscr = pyautogui.size()
    cap.set(3, wcam)
    cap.set(4, hcam)
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)  # flipping in x-axis to avoid opposite reflection
        h, w, c = img.shape
        rbg_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the frame[img]BGR2RBG
        output = hand_detector.process(rbg_img)  # processing the hand_detector in the frame rbg_img
        hands = output.multi_hand_landmarks  # hand landmarks of x,y,z
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(img, hand,
                                             landmark_drawing_spec=drawing_utils.DrawingSpec(color=(0, 0, 255),
                                                                                             circle_radius=2))  # calling drawing_utils to draw hand landmarks in the frame[img]

                landmarks = hand.landmark
                cv2.rectangle(img, (framer, framer), (wcam - framer, hcam - framer), (255, 0, 255), 2)
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * w)  # finding x position
                    y = int(landmark.y * h)
                    if id == 8:
                        cv2.circle(img, center=(x, y), radius=15, color=(0, 255, 255))
                        index_tip_x = screen_w / w * x  # to operate full screen using this
                        index_tip_y = screen_h / h * y
                        index_x = int(np.interp(x, (framer, wcam - framer), (0, wscr)))
                        index_y = int(np.interp(y, (framer, wcam - framer), (0, hscr * 2)))
                        cloc_x = int(ploc_x + (index_x - ploc_x) // smooth)
                        cloc_y = int(ploc_y + (index_y - ploc_y) // smooth)
                        win32api.SetCursorPos((cloc_x, cloc_y))
                        ploc_x, ploc_y = cloc_x, cloc_y
                        if abs(index_tip_y - thumb_y) < 40 or abs(index_tip_y - thumb_y) < -40:
                            if abs(index_tip_x - thumb_x) < 40 or abs(index_tip_x - thumb_x) < -40:
                                print("right click")
                                pyautogui.click(button='right')
                                # pyautogui.hotkey('fn','f4')
                                #time.sleep(0.3)

                    if id == 6:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        ind_x = screen_w / w * x
                        ind_y = screen_h / h * y
                        if abs(thumb_y - ind_y) < 40:
                            if abs(thumb_x - ind_x) < 40:
                                print("double click")
                                pyautogui.doubleClick()
                                #time.sleep(0.3)
                    if id == 16:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        ring_tip_x = screen_w / w * x
                        ring_tip_y = screen_h / h * y
                        if abs(ring_tip_y - ring_1_y) < 40 or abs(ring_tip_y - ring_1_y) < -40:
                            if abs(ring_tip_x - ring_1_x) < 40 or abs(ring_tip_x - ring_1_x) < -40:
                                print("volume up")
                                pyautogui.hotkey('volumeup')
                                #time.sleep(0.1)

                    if id == 14:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        ring_1_x = screen_w / w * x
                        ring_1_y = screen_h / h * y
                    if id == 20:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        pinky_tip_x = screen_w / w * x
                        pinky_tip_y = screen_h / h * y
                        if abs(pinky_tip_y - pinky_1_y) < 40 or abs(pinky_tip_y - pinky_1_y) < -40:
                            if abs(pinky_tip_x - pinky_1_x) < 40 or abs(pinky_tip_x - pinky_1_x) < -40:
                                print("volume down")
                                pyautogui.hotkey('volumedown')
                                #time.sleep(0.1)
                    if id == 18:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        pinky_1_x = screen_w / w * x
                        pinky_1_y = screen_h / h * y

                    if id == 12:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        mid_tip_x = screen_w / w * x
                        mid_tip_y = screen_h / h * y
                        if abs(mid_tip_y - mid_1_y) < 40 or abs(mid_tip_y - mid_1_y) < -40:
                            if abs(mid_tip_x - mid_1_x) < 40 or abs(mid_tip_x - mid_1_x) < -40:
                                print("chrome")
                                pyautogui.hotkey('ctrl', 'alt', 'c')
                                #time.sleep(0.3)

                    if id == 10:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        mid_1_x = screen_w / w * x
                        mid_1_y = screen_h / h * y
                    if id == 5:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        indbtm_x = screen_w / w * x
                        indbtm_y = screen_h / h * y
                        if abs(thumb_y - indbtm_y) < 40:
                            if abs(thumb_x - indbtm_x) < 40:
                                print("single click")

                                pyautogui.click()

                                #time.sleep(0.2)

                    if id == 9:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        mid_x = screen_w / w * x
                        mid_y = screen_h / h * y
                        if abs(thumb_y - mid_y) < 20:
                            if abs(thumb_x - mid_x) < 20:
                                print("scroll down")
                                pyautogui.scroll(-500)
                                #time.sleep(0.3)
                    if id == 13:
                        cv2.circle(img, center=(x, y), radius=17, color=(0, 255, 255))
                        ring_x = screen_w / w * x
                        ring_y = screen_h / h * y
                        if abs(thumb_y - ring_y) < 20:
                            if abs(thumb_x - ring_x) < 20:
                                print("scroll up")
                                pyautogui.scroll(500)
                                #time.sleep(0.3)
                    if id == 4:
                        cv2.circle(img, center=(x, y), radius=20, color=(0, 255, 255))
                        thumb_x = screen_w / w * x
                        thumb_y = screen_h / h * y

        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            cv2.destroyAllWindows()
            break


def open_pdf():
    path = 'Virtual_Mouse_instructions.pdf'
    subprocess.Popen([path], shell=True)


root = tk.Tk()
canvas = tk.Canvas(root, width=650, height=450, background="white")
canvas.grid(columnspan=3, rowspan=4)
logo = Image.open('VIRTUA.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, background="white")
logo_label.image = logo
logo_label.grid(column=1, row=0)
myfont = font.Font(size=20, family='Helvetica')
root.title("Virtual Mouse")
L1 = tk.Label(root, text='''Please read the instructions before you start''', font=("TimesNewRoman", 13),
              background="white")
L1.grid(columnspan=3, column=0, row=1)
browse_text = tk.StringVar()

B = tk.Button(root, textvariable=browse_text, command=proces, bg='black', fg="white", height=1, width=18, font=myfont)
browse_text.set("Start")
B.grid(column=1, row=3)

C = tk.Button(root, text='Instructions', command=open_pdf, bg='#FFFF6A', fg='black', height=2, width=15)

C.grid(column=1, row=2)

root.mainloop()
