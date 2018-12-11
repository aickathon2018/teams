import cv2
import sys
import requests # pip install requests
import json     # pip install json
from pprint import pprint
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk

#USER INTEFACE
window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('1200x1200')
lbl = Label(window, text="Hello")
lbl.pack(side = TOP, fill=X )

def clicked():
   # 6dir = filedialog.askdirectory()
   fileupload = filedialog.askopenfilename() #filetypes = (("JPG Files","*.jpg"),("all files","*.*"))
   lbl.configure(text="Upload Success")
   path = fileupload
   img = ImageTk.PhotoImage(Image.open(path))
   img = ImageTk.PhotoImage(Image.open(path))
   panel = Label(window, image=img)
   panel.photo = img
   panel.pack( side = LEFT, fill=Y)
   # Path of image (jpg/jpeg/png)
   

   # url name
   url = "https://face.recoqnitics.com/analyze"
   accessKey = "61c03187783de1dfd6b4"
   secretKey = "daa8ba04f100d119bf3779b596e3fc9fa3bf5b03"

   # access_key and secret_key
   data = {'access_key': accessKey,
     'secret_key': secretKey }

   filename = {'filename': open(fileupload,'rb')}
   r = requests.post(url, files = filename, data=data)
   content = json.loads(r.content)
   pprint(dict(content))
   
   

   final_listAge = []
   for sub_listAge in content['faces']:
      final_listAge.append(sub_listAge['age'])
      print(final_listAge)
   final_listH = []
   for sub_listH in content['faces']:
      final_listH.append(sub_listH['boundingBox'])
   valueH = []
   for sub_listH in final_listH:
      valueH.append(sub_listH['h'])
   print(valueH)

   final_listW = []
   for sub_listW in content['faces']:
      final_listW.append(sub_listW['boundingBox'])
   valueW = []
   for sub_listW in final_listW:
      valueW.append(sub_listW['w'])
   print(valueW)

   final_listX = []
   for sub_listX in content['faces']:
      final_listX.append(sub_listX['boundingBox'])
   valueX = []
   for sub_listX in final_listX:
      valueX.append(sub_listX['x'])
   print(valueX)

   final_listY = []
   for sub_listY in content['faces']:
      final_listY.append(sub_listY['boundingBox'])
   valueY = []
   for sub_listY in final_listY:
      valueY.append(sub_listX['y'])
   print(valueY)

   final_listAngry = []
   for sub_listAngry in content['faces']:
      final_listAngry.append(sub_listAngry['emotions'])
   valueAngry = []
   for sub_listAngry in final_listAngry:
      valueAngry.append(sub_listAngry['angry'])
   print(valueAngry)

   final_listDisgust = []
   for sub_listDisgust in content['faces']:
      final_listDisgust.append(sub_listDisgust['emotions'])
   valueDisgust = []
   for sub_listDisgust in final_listDisgust:
      valueDisgust.append(sub_listDisgust['disgust'])
   print(valueDisgust)

   final_listFear = []
   for sub_listFear in content['faces']:
      final_listFear.append(sub_listFear['emotions'])
   valueFear = []
   for sub_listFear in final_listFear:
      valueFear.append(sub_listFear['fear'])
   print(valueFear)

   final_listHappy = []
   for sub_listHappy in content['faces']:
      final_listHappy.append(sub_listHappy['emotions'])
   valueHappy = []
   for sub_listHappy in final_listHappy:
      valueHappy.append(sub_listHappy['happy'])
   print(valueHappy)

   final_listNeutral = []
   for sub_listNeutral in content['faces']:
      final_listNeutral.append(sub_listNeutral['emotions'])
   valueNutral = []
   for sub_listNeutral in final_listNeutral:
      valueNutral.append(sub_listNeutral['neutral'])
   print(valueNutral)

   final_listSad = []
   for sub_listSad in content['faces']:
      final_listSad.append(sub_listSad['emotions'])
   valueSad = []
   for sub_listSad in final_listSad:
      valueSad.append(sub_listSad['sad'])
   print(valueSad)

   final_listSurprise = []
   for sub_listSurprise in content['faces']:
      final_listSurprise.append(sub_listSurprise['emotions'])
   valueSurprise = []
   for sub_listSurprise in final_listSurprise:
      valueSurprise.append(sub_listSurprise['surprise'])
   print(valueSurprise)

   final_listCon = []
   for sub_listCon in content['faces']:
      final_listCon.append(sub_listCon['faceConfidence'])
   print(final_listCon)

   final_listGenCon = []
   for sub_listGenCon in content['faces']:
      final_listGenCon.append(sub_listGenCon['gender'])
   valueGenCon = []
   for sub_listGenCon in final_listGenCon:
      valueGenCon.append(sub_listGenCon['confidence'])
   print(valueGenCon)

   final_listGen = []
   for sub_listGen in content['faces']:
      final_listGen.append(sub_listGen['gender'])
   valueGen = []
   for sub_listGen in final_listGen:
      valueGen.append(sub_listGen['value'])
   print(valueGen)
   a=0
   T = Text(window, height=50, width=30)
   
   #show attriute
   while(a<len(valueGen)):
      text = "Face Confidence: " + str(final_listCon[a]) + "\nAGE: " + str(final_listAge[a]) + "\nGENDER: " + str(valueGen[a]) + "\nGENDER Confidence: "+str(valueGenCon[a])+"\nAngry: "+str(valueAngry[a])+"\nDisgust: "+str(valueDisgust[a])+"\nFear: "+str(valueFear[a])+"\nHappy: "+str(valueHappy[a])+"\nNeutral: "+str(valueNutral[a])+"\nSad: "+str(valueSad[a])+"\nSurpise: "+str(valueSurprise[a])+"\n"+"\n"+"\n"
      if max(content['faces'][a]['emotions'].items(), key = lambda x : x[1])[0] == "fear":
         
         r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBIFVzWWIFXMsjc7FvfCNuuqWs8ikrSFRE")
         content = json.loads(r.content)
         text += "Fear!!! Report police!!!! "+str((dict(content)))
         print("report")
         print(dict(content))
      T.insert(END, text)
      T.pack(side=TOP,fill=X)
      a=a+1

def openWebcam() :
   cascPath = "C:/Users/ultra/Anaconda3/Library/haarcascade_frontalface_default.xml"
   faceCascade = cv2.CascadeClassifier(cascPath)
   video_capture = cv2.VideoCapture(0)
   url = "https://fashion.recoqnitics.com/detect-person"
   accessKey = "61c03187783de1dfd6b4"
   secretKey = "daa8ba04f100d119bf3779b596e3fc9fa3bf5b03"
   data = {'access_key': accessKey,  'secret_key': secretKey}
   urlFace = "https://face.recoqnitics.com/analyze"
   count = 0
   while True:
      ret, frame = video_capture.read()
      if count == 30:
         cv2.imwrite("C:/Users/ultra/Downloads/asd/frame0.jpg", frame)     # save frame as JPEG file
         file = "C:/Users/ultra/Downloads/asd/frame0.jpg"
         filename = {'filename': open(file,'rb')}
         r = requests.post(urlFace, files = filename, data=data)
         content = json.loads(r.content)    
         if len(content['faces']) > 0 :
            text = "Emotions : "
            a=1
            for x in range(0,len(content['faces'])):
               if max(content['faces'][x]['emotions'].items(), key = lambda x : x[1])[0] == "fear":
                  r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBIFVzWWIFXMsjc7FvfCNuuqWs8ikrSFRE")
                  content = json.loads(r.content)
                  text +="Person "+str(a)+" in "+ "Fear!!! Report police!!!! "+str((dict(content)))


               else :
                  text +="Person "+ str(a)+" in "+max(content['faces'][x]['emotions'].items(), key = lambda x : x[1])[0] + " "
                  a+=1
                  text+="\n"
               # print(x)
               # print(' = ')
               # print(max(content['faces'][x]['emotions'].items(), key = lambda x : x[1])[0])
               # print(content['faces'][x]['emotions'])
               
               # print("report polis")
            T = Text(window, height=5, width=30)
            T.insert(END, text)
            T.pack(side=TOP,fill=X)
            count = 0
      else :
         count += 1
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.1,  
         minNeighbors=5,
         minSize=(30, 30),
         flags=cv2.CASCADE_SCALE_IMAGE)
      for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
      cv2.imshow('Video', frame)
      # img = ImageTk.PhotoImage(Image.open("C:/Users/ASUS/Desktop/aic/test/frame0.jpg"))
      # panel = Label(window, image=img)
      # panel.photo = img
      # panel.pack( side = LEFT, fill=Y)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break
      # tk.update()
   video_capture.release()
   cv2.destroyAllWindows()

btn = Button(window, text="Upload Your Video/Photo Here(MP3,JPEG)",bg="orange", fg="red",command=clicked)
btn.pack( side = TOP, fill=X)
btn2 = Button(window, text="Open live WebCam",bg="blue", fg="black",command=openWebcam)
btn2.pack(side = TOP, fill = X)

window.mainloop()
