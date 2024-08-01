import numpy as np
import HandTrackingModule as htm
import cv2
import autopy

wCam, hCam = 640, 480
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScreen, hScreen = autopy.screen.size()
frameReduction = 20
smoothening = 7
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = htm.handDetector(maxHands=1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameReduction, frameReduction), (wCam - frameReduction, hCam - frameReduction),
                      (255, 0, 255), 3)

        if fingers[1]==1 and fingers[2]==0:
            x3 = np.interp(x1, (0, wCam), (0, wScreen))
            y3 = np.interp(y1, (0, hCam), (0,hScreen))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            autopy.mouse.move(wScreen-x3, y3)
            cv2.circle(img, (x1, y1), 15, (255,0,255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()



    cv2.imshow("Image", img)
    cv2.waitKey(1)
