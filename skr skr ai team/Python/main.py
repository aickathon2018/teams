from sklearn.externals import joblib

import yaml
import numpy as np
import cv2
import time
import pyrebase

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
st = firebase.storage()
frame_path = []
frame_path.append(r"C:\Users\MARK\Desktop\AI HACKATHON\datasets\Free.jpg")
frame_path.append(r"C:\Users\MARK\Desktop\AI HACKATHON\datasets\Occupied.jpg")
points_yaml = r"C:\Users\MARK\Desktop\AI HACKATHON\datasets\Input.yml"
config = {'parking_overlay': True, 'parking_detection': True, 'park_laplacian_th': 3.5}

with open(points_yaml, 'r') as stream:
    parking_data = yaml.load(stream)
    parking_contours = []
    parking_bounding_rects = []
    parking_mask = []
    for park in parking_data:
        points = np.array(park['points'])
        rect = cv2.boundingRect(points)
        points_shifted = points.copy()
        points_shifted[:, 0] = points[:, 0] - rect[0]
        points_shifted[:, 1] = points[:, 1] - rect[1]
        parking_contours.append(points)
        parking_bounding_rects.append(rect)
        mask = cv2.drawContours(np.zeros((rect[3], rect[2]), dtype=np.uint8), [points_shifted], contourIdx=-1,
                            color=255, thickness=-1, lineType=cv2.LINE_8)
        mask = mask == 255
        parking_mask.append(mask)

kernel_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)) # morphological kernel
kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 19))
parking_status = [False]*len(parking_data)
parking_buffer = [None]*len(parking_data)

while 1:
    for frame in frame_path:
        # Background Subtraction
        frame_input = cv2.imread(frame, 1)
        frame_blur = cv2.GaussianBlur(frame_input, (5, 5), 0)
        frame_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)
        frame_out = frame_input

        # Draw Overlay
        if config['parking_detection']:
            for ind, park in enumerate(parking_data):
                points = np.array(park['points'])
                rect = parking_bounding_rects[ind]
                roi_gray = frame_gray[rect[1]:(rect[1]+rect[3]), rect[0]:(rect[0]+rect[2])]
                laplacian = cv2.Laplacian(roi_gray, cv2.CV_64F)
                points[:, 0] = points[:, 0] - rect[0]
                points[:, 1] = points[:, 1] - rect[1]
                delta = np.mean(np.abs(laplacian * parking_mask[ind]))
                status = delta < config['park_laplacian_th']
                parking_status[ind] = status
            print(parking_status)

        if config['parking_overlay']:
            for ind, park in enumerate(parking_data):
                points = np.array(park['points'])
                if parking_status[ind]:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                cv2.drawContours(frame_out, [points], contourIdx=-1,
                                 color=color, thickness=2, lineType=cv2.LINE_8)
                moments = cv2.moments(points)
                centroid = (int(moments['m10']/moments['m00'])-3, int(moments['m01']/moments['m00'])+3)
                cv2.putText(frame_out, str(park['id']), (centroid[0]+1, centroid[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(frame_out, str(park['id']), (centroid[0]-1, centroid[1]-1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(frame_out, str(park['id']), (centroid[0]+1, centroid[1]-1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(frame_out, str(park['id']), (centroid[0]-1, centroid[1]+1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(frame_out, str(park['id']), centroid, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame_out)
        number_free = parking_status.count(True)
        str_free = str(number_free)
        data = {"free": str_free}
        db.child("aeon").update(data)
        number_occupied = parking_status.count(False)
        str_occupied = str(number_occupied)
        data2 = {"occupied": str_occupied}
        db.child("aeon").update(data2)
        st.child("carpark")
        st.child("carpark").put(frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        time.sleep(10)

cv2.destroyAllWindows()

# loaded_model = joblib.load('Train.joblib')
# clf.predict
