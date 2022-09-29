from turtle import width
import torch
import mss 
import numpy as np
import cv2
import time
import keyboard
import pyautogui
import win32api,win32con


def click(x,y):
    win32api.SetCursorPos((x,y)) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #uses time api, to simulate normal input.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#model = torch.hub.load('ultralytics/yolov5', 'yolov5s',pretrained=True)
#loading model with trained weights on valorant data
model = torch.hub.load('ultralytics/yolov5', 'custom',path='best.pt')


#grabbing screen size to capture
with mss.mss() as sct:
    monitor = {'top':20,'left':0,'width':1024,'height':768}


while True:
    t = time.time()

    #grabbing screen
    img = np.array(sct.grab(monitor))
    #results = model(img)
    img = cv2.resize(img, dsize=(960, 960), interpolation=cv2.INTER_CUBIC)

    results = model(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), size=400)

    r1 = results.xyxy[0].tolist()
    #checking if predictions
    if len(r1) > 0:
        if r1[0][4] > 0.5: #confidence score
            if r1[0][5] == 0 or r1[0][5] == 1:
                x = int(r1[0][2])
                y = int(r1[0][3])
                width = int(r1[0][2] - r1[0][0])
                print('width: ',width)
                height = int(r1[0][3] - r1[0][1])
                print('height: ',height)

                xpos = int(.37 * ((x - (width)) - pyautogui.position()[0]))
                ypos = int(.37 * ((y - (height/2)) - pyautogui.position()[1]))

                click(xpos,ypos)


    cv2.imshow('s',np.squeeze(results.render()))

    print('fps: {}'.format(1/ (time.time()-t)))

    cv2.waitKey(1)

    if keyboard.is_pressed('q'):
        break

cv2.destroyAllWindows()
