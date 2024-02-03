import csv
import cv2
import os
import numpy as np
from PIL import Image

a=input("Enter new DOCTOR name: ")

with open('id.csv', newline='') as f:
    reader = csv.reader(f)
    name_list = list(reader)
employee_id = int(name_list[0][0])
cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = employee_id
samples=100

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
count = 0

while(True):

    ret, img = cam.read()
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", img[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff 
    if k == 27:
        break
    elif count >= samples:
         break

cam.release()
cv2.destroyAllWindows()

import numpy as np
from PIL import Image
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    import numpy as np
    from PIL import Image

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') 
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.save('trainer/trainer.yml') 

print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


with open('id.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([(employee_id+1)])

with open('Doctors.csv', 'a+') as file:
    writer = csv.writer(file)
    writer.writerow([a])
print("Writing the new employee into the system!")
print("Please keep your head straight to collect photo for Profile Picture")
from time import sleep
sleep(3)


import csv
import cv2
import os
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(0)
get_picture_id = 0
while(True):
    ret, frame = cap.read()
    get_picture_id = get_picture_id + 1
    cv2.imshow('frame', frame)
    k = cv2.waitKey(10) & 0xff 
    if k == 27 or get_picture_id==30:
        cv2.imwrite("profile_pictures/" + a + ".jpg",frame)
        break
        
cap.release()
cv2.destroyAllWindows()
