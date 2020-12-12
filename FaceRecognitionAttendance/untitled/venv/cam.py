import cv2
face_classifier=cv2.CascadeClassifier('C:/FaceRecognitionAttendance/untitled/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)



    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
cam = cv2.VideoCapture(0)

        detector = cv2.CascadeClassifier('C:/FaceRecognitionAttendance/untitled/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        sampleNum = 0

        while (True):
            ret, img = cam.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray,1.3,5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x, y),(x + w, y + h),(255, 0, 0),2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                name = "F:/faces/user" + Id + '.' + str(sampleNum) + ".jpg"
                cv2.imwrite(name, gray[y:y + h, x:x + w])
                # display the frame

                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 20
            elif sampleNum > 20:
                break
        cam.release()
        cv2.destroyAllWindows()
