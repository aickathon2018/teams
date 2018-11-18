import csv
import coqnitics
from PIL import Image
import requests
from io import BytesIO
import urllib.request
import function
from db import mydb

reader = csv.reader(open('data.csv', newline=''), delimiter=',')
count = 0

for row in reader:
    if row:
        count += 1
        fav_count = row[0]
        created_at = row[2]
        urllib.request.urlretrieve(row[1], '{}{}{}'.format('tmp/train', count,'.jpg'))
        result = coqnitics.requestAPI(count)
        # GETTERS
        colors = function.getBestColours(result['person']['colors'], 3)
        styles = function.getBestStyles(result['person']['styles'], 3) # for styles
        confidence = function.getBestGarments(result['person']['garments'], 1)

        preparedData = function.prepareData(colors, styles, confidence)

        mycursor = mydb.cursor()
        sql = "INSERT INTO tbl_clothe (Colour1, Colour2, Colour3, Style1, Style2, Style3, Garment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val= (preparedData)
        mycursor.execute(sql, val)
            
        mydb.commit()
        print(mycursor.rowcount, val)