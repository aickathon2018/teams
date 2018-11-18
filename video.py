import requests     # pip install requests
import json         # pip install json
import numpy as np  # pip install numpy 
import cv2          # pip install opencv-python
import tkinter
from tkinter import*
import threading
from threading import Thread
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

def satisfy(listH,listS,listA,listD,listN):
    totalHap = sum(listH)*3
    totalSad = sum(listS)*-1
    totalAng = sum(listA)*-2
    totalDis = sum(listD)*-1.5
    totalNeu = sum(listN)*1
    totalEmo = totalHap+totalSad+totalAng+totalDis+totalNeu
    return totalEmo

root = tkinter.Tk()
root.title("Satisfactometer")
tex = Text(root)

url = "https://face.recoqnitics.com/analyze"
accessKey = "3775e5bc177f9ef16f65"
secretKey = "4e100a9947b9218588eace35238ccf44da58e728"
file = 'img.jpg'
# access_key and secret_key
data = {'access_key': accessKey,
    'secret_key': secretKey}

ThreadList = []
DrawList = []
test = []

#lock = threading.Lock() # Lock

def detect(filename, T):
    r = requests.post(url, files = filename, data=data)
    content = json.loads(r.content)
    result = content['faces']
    for i in range(len(result)):
        test.append(result[i])
    print(T)
    return result

cap = cv2.VideoCapture(0)
time = 0
while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if len(ThreadList) > 0:    
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
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,255,255),3)
        elif high == 'angry':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,0,255),3)
        elif high == 'fear':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(0,0,0),4)
        elif high == 'surprise':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(128,0,128),3)
        elif high == 'sad':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(255,0,0),3)
        elif high == 'disgust':
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(34,139,34),3)
        else:
            frame = cv2.rectangle(frame,(draw[0]['x'],draw[0]['y']),(draw[0]['x']+draw[0]['w'],draw[0]['y']+draw[0]['h']),(192,192,192),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time += 1
    if time % 150 == 0:
        cv2.imwrite(file,frame)
        
        filename = {'filename': open(file,'rb')}
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

angry = []
disgust = [ ]
happy = []
sad = []
neutral = []


print(test)

for x in test:
    angry.append (x["emotions"]["angry"])
    disgust.append (x["emotions"]["disgust"])
    happy.append (x["emotions"]["happy"])
    sad.append (x["emotions"]["sad"])
    neutral.append (x["emotions"]["neutral"])

maxIndex, maxValue = max(enumerate(happy), key=lambda v: v[1])
line = "happiest: photo "+str(maxIndex+1)+" with value "+str('{:f}'.format(maxValue))+"\n"
tex.insert(INSERT,line)

##show most sad photo and value(lis2)
maxIndex2, maxValue2 = max(enumerate(sad), key=lambda v: v[1])
line = "saddest: photo "+str(maxIndex2+1)+" with value "+str('{:f}'.format(maxValue2))+"\n"
tex.insert(INSERT,line)

##show most angry photo and value(lis3)
maxIndex3, maxValue3 = max(enumerate(angry), key=lambda v: v[1])
line = "angriest: photo "+str(maxIndex3+1)+" with value "+str('{:f}'.format(maxValue3))+"\n"
tex.insert(INSERT,line)

##show most disguat photo and value(lis4)
maxIndex4, maxValue4 = max(enumerate(disgust), key=lambda v: v[1])
line = "most disgusted: photo "+str(maxIndex4+1)+" with value "+str('{:f}'.format(maxValue4))+"\n"
tex.insert(INSERT,line)

#show most neutral photo and value(lis5)
maxIndex5, maxValue5 = max(enumerate(neutral), key=lambda v: v[1])
line = "most neutral: photo "+str(maxIndex5+1)+" with value "+str('{:f}'.format(maxValue5))+"\n"
tex.insert(INSERT,line)

total = satisfy(happy,sad,angry,disgust,neutral)

line = "Satisfaction value: " + str('{:f}'.format(total)) +"\n"
tex.insert(INSERT,line)

line = "Satisfaction: "
tex.insert(INSERT,line)
if total == 0:
    line="Neutral"
elif total > 3:
    line="Very Satisfied"
elif total > 0:
    line= "Satisfied"
elif total < -3:
    line="Very unsatisfied"
elif total < 0:
    line="Unsatisfied"

tex.insert(INSERT,line)
tex.pack()
root.mainloop()