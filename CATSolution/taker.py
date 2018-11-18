import requests     # pip install requests
import json         # pip install json
import numpy as np  # pip install numpy 
import cv2          # pip install opencv-python
import threading
from threading import Thread
from multiprocessing import Process
from multiprocessing.pool import ThreadPool
import vlc

url = "https://face.recoqnitics.com/analyze"
accessKey = "d7595965fdcaeaf6210b"
secretKey = "01ec11cfcd5cdbbd19e95fefb70fa828f68fb443"
file = 'img.jpg'
# access_key and secret_key
data = {'access_key': accessKey,
    'secret_key': secretKey}

ThreadList = []
DrawList = []

p = vlc.MediaPlayer("./Alert.mp3")
play = False

#lock = threading.Lock() # Lock

def detect(filename, T):
    r = requests.post(url, files = filename, data=data)
    content = json.loads(r.content)
    result = content['faces']
    for i in range(len(result)):
        print(result[i])
    print(T)
    return result

cap = cv2.VideoCapture(0)
time = 0
while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if len(ThreadList) > 0:   
        p.stop()
        play = False		
        result = ThreadList[0].get()
        ThreadList.pop(0)
        DrawList = []
        for face in result:
            pos = []
            pos.append(face['boundingBox'])
            pos.append(face['emotions'])
            DrawList.append(pos)
            
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

    # Display the resulting frame
    for draw in DrawList:
        high = 'angry'
        for prop in draw[1]:
            if draw[1][prop] > draw[1][high]:
                high = prop
        if high == 'happy': 
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,255,0),3)
        elif high == 'angry':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,255,255),3)
        elif high == 'fear':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,0,255),4)
            if not play:
                play = True
                p.play()
        elif high == 'surprise':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(255,255,0),3)
        elif high == 'sad':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(255,0,255),3)
        elif high == 'disgust':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(255,0,0),3)
        else:
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(192,192,192),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time += 1
    if time % 150 == 0:
        cv2.imwrite(file,frame)
        
        filename = {'filename': open(file,'rb')}
        print(filename)
        #if len(ThreadList) > 0:
        #    ThreadList[0].join()
        #    t = ThreadList.pop(0)
        pool = ThreadPool(processes=1)
        t = pool.apply_async(detect, ({'filename': open(file,'rb')}, time))
        ThreadList.append(t)
        #t.start()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()