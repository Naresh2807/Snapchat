import cv2
import cvzone
from time import sleep
key = cv2. waitKey(1)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
overlay = cv2.imread('spider.png', cv2.IMREAD_UNCHANGED)
sleep(2)
while True:

    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
            overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5))) 
            frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
            print("Image saved!")
            
            break
        
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break