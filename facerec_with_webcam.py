import cv2
import face_recognition

webcam = cv2.VideoCapture(0)                                 #importo img da webcam
name = 'PERSON'

print("PREMI 'Q' PER USCIRE...")
while True:
    ret, frame = webcam.read()                               #legge frame dalla webcam
    resized = cv2.resize(frame, (0, 0), fx = 1, fy = 1)      #ridimenziono finestra webcam
    rgb_image = resized[:,:,::-1]
    for (top, right, bottom, left) in face_recognition.face_locations(rgb_image):
        cv2.rectangle(resized, (left, top), (right, bottom), (0, 0, 255))
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(resized, name, (left + 0, bottom + 30), font, 1.0, (255, 0, 0), 1)
    cv2.imshow("VIDEOREC", resized)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()

# NOTA: non chiamare il file python con "face_recognition" in quanto creerebbe conflitto con il modulo!!!
