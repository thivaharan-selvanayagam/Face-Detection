import cv2

#Trained-Dataset
TrainedDataset= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read-a-image
img=cv2.imread('images/3.JPG')

#Convert-to-grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=TrainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
cv2.imshow('thiva',img)
#cv2.imshow('gray',gray)
cv2.waitKey()