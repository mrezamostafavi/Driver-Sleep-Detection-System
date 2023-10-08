import cv2
#import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
out=cv2.VideoWriter('test.mp4',cv2.VideoWriter_fourcc(*'DIVX'),10.0,(640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if(not len(eyes)):
            t = 0
            while(not len(eyes)):
                t += 1
                if t > 2:   # driver is sleeping
                    print ("driver is sleeping !\n")
                    cv2.putText(frame,'sleeping',(80,410),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,0,255))
                    #GPIO.output(18,GPIO.HIGH)
                    #time.sleep(5)
                    #GPIO.output(18, GPIO.LOW)
                    t=0
                    break
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
