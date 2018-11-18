import requests # pip install requests
import json     # pip install json
import csv

def Customer():
    # Path of image (jpg/jpeg/png)
    file = "test2.jpg"

    # url name
    url = "https://face.recoqnitics.com/analyze"
    accessKey = "defe6ae5679c8fe463da"
    secretKey = "1095abb379dda81b7624c423f02ff4812e223e19"

    # access_key and secret_key
    data = {'access_key': accessKey,
      'secret_key': secretKey}

    filename = {'filename': open(file,'rb')}
    r = requests.post(url, files = filename, data=data)
    content = json.loads(r.content)
      
    print(content)
    with open('data.json', 'w') as outfile:
        json.dump(content, outfile)

    print("\n-------------------\n")

    with open('test2.csv', 'a', newline='') as outfile:
        #order input
        print("If no item type 0 ")
    
        #product name input
        p_name=input("Please insert product name.")
        while (p_name!="0"):

            #poduct quantity
            p_quan = input("Please insert quantity.")
          
            f = csv.writer(outfile)
            #f.writerow(["product_name","quantity","age","gender"])
            print(len(content['faces']))
            ##for i in range(len(content['faces'])):
            #assume one person per transaction
            facething =content['faces'][0]
            gender = facething['gender']
            print(facething['age'])
            print(gender['value'])
            if gender['value']=="Male":
               f.writerow([p_name,p_quan,facething['age'],'M'])
            elif gender['value']=="Female":
               f.writerow([p_name,p_quan,facething['age'],'F'])
            #product name input
            p_name = input("Please insert product name.")

if __name__=='__main__':
    import sys
    Customer()
