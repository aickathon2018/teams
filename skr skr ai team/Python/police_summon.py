from sklearn.externals import joblib

import requests
import json
import pyrebase
import numpy as np
import xlwt

# Path of image (jpg/jpeg/png)
file = r'C:\Users\MARK\Desktop\AI HACKATHON\datasets\occupied.jpg'

# url name
url = "https://lpr.recoqnitics.com/detect"
accessKey = "c4ba17f0e24772ba71d2"
secretKey = "3b3c36f8da1adcfd4061d529fa1f04b3e4885c86"

# access_key and secret_key
data = {'access_key': accessKey,
  'secret_key': secretKey}

filename = {'filename': open(file, 'rb')}
r = requests.post(url, files = filename, data=data)
content = json.loads(r.content)
plate = content["licensePlates"][0]["licensePlateNumber"]
print(content)
try:
    platearray = [0, 0, 0, 0]
    for i in range (0, 3):
        platearray[i] = content["licensePlates"][i]["licensePlateNumber"]
    z=1
except:
    platearray = [0, 0, 0]
    for i in range(0, 2):
        platearray[i] = content["licensePlates"][i]["licensePlateNumber"]
    z=0
config = {
    "apiKey": "AIzaSyBmehyMgBL4UfCaB66I05cuknt5dQl_T4g",
    "authDomain": "rpiappcontrol-1f76e.firebaseapp.com",
    "databaseURL": "https://rpiappcontrol-1f76e.firebaseio.com/",
    "projectId": "rpiappcontrol-1f76e",
    "storageBucket": "rpiappcontrol-1f76e.appspot.com",
    "messagingSenderId": "537116058868"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataC = [0, 0, 0, 0, 0, 0]
dataET = [0, 0, 0, 0, 0, 0]
dataPT = [0, 0, 0, 0, 0, 0]
dataHP = [0, 0, 0, 0, 0, 0]
dataGT = [0, 0, 0, 0, 0, 0]
dataExT = [0, 0, 0, 0, 0, 0]

loaded_model = joblib.load('Train.joblib')

park = ["park1", "park2", "park3", "park4", "park5"]
for i in range(0, 5):
    users = db.child("jompay").child(park[i]).child("carplate").get()
    dataC[i] = users.val()
    users = db.child("jompay").child(park[i]).child("expiredtime").get()
    dataET[i] = users.val()
    users = db.child("jompay").child(park[i]).child("paymenttime").get()
    dataPT[i] = users.val()
    users = db.child("jompay").child(park[i]).child("hrpaid").get()
    dataHP[i] = users.val()
    users=db.child("jompay").child(park[i]).child("exit_time").get()
    dataExT[i] = users.val()
    users = db.child("jompay").child(park[i]).child("gaptime").get()
    dataGT[i] = users.val()
input = np.array([dataET, dataGT], dtype=float)
input = np.transpose(input)
s = loaded_model.predict(input)
common = set(dataC).intersection(platearray)
difference = set(common).symmetric_difference(platearray)
difference = ', '.join(str(e) for e in difference)
if difference != '':
    index = platearray.index(difference)
    s[index] = 0
    print(s)
else:
    print(s)
x=0
for i in range(0, 4):
    if s[i]==1:
        dataC[i]=dataC[i]
        dataExT[i]=dataExT[i]
        dataPT[i]=dataPT[i]
        dataHP[i]=dataHP[i]
    x+=1

wb=xlwt.Workbook()
ws=wb.add_sheet("Summon List")
ws.write(0, 0, "Carplate")
ws.write(0, 1, "Exit Time")
ws.write(0, 2, "Payment Time")
ws.write(0, 3, "Hour Paid")
for i in range (1,x ):
    if dataC[i]!=0:
        ws.write(i, 0, dataC[i])
        ws.write(i, 1, dataExT[i])
        ws.write(i, 2, dataPT[i])
        ws.write(i, 3, dataHP[i])
if z==0:
    wb.save("Police.xls")
else :
    wb.save("Police2.xls")