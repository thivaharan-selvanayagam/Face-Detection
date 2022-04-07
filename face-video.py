import cv2

#Trained-Dataset
TrainedDataset= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video=cv2.VideoCapture('videos/human.mp4')
while True:
    sucess,frame=video.read()
    if sucess== True:
        gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces= TrainedDataset.detectMultiScale(gray_image)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
        cv2.imshow('video',frame)
        cv2.waitKey(1)
    else:
        print("Video Completed")
        break