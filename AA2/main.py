import numpy as np
import cv2
import math

goalX = 200
goalY = 70

xCords = []
yCords = []

tracker = cv2.legacy.TrackerCSRT_create()

confidenceThreshold = 0.3
NMSThreshold = 0.1

modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

labelsPath = 'coco.names'

labels = open(labelsPath).read().strip().split('\n')

yoloNetwork = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

video = cv2.VideoCapture("bb2.mp4")

detected = False

ballBoxColor = (255, 0, 255)


def drawBox(img, bbox):
    global ballBoxColor
    x = int(bbox[0])
    y = int(bbox[1])
    w = int(bbox[2])
    h = int(bbox[3])

    cv2.rectangle(img, (x, y), ((x+w), (y+h)), ballBoxColor, 3, 1)
    cv2.putText(img, "Tracking", (75, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, ballBoxColor, 2)


def goalTrack(img, bbox):
    global ballBoxColor
    x = int(bbox[0])
    y = int(bbox[1])
    w = int(bbox[2])
    h = int(bbox[3])

    c1 = x + int(w/2)
    c2 = y + int(h/2)

    cv2.circle(img, (c1, c2), 1, (255, 0, 255), 1)

    cv2.circle(img, (int(goalX), int(goalY)), 2, (0, 255, 0), 3)

    dist = math.sqrt(((c1-goalX)**2) + (c2-goalY)**2)

    ballBoxColor = (0, 20000/dist, dist)

    if (dist <= 20):
        cv2.putText(img, "Goal", (300, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    xCords.append(c1)
    yCords.append(c2)

    for i in range(len(xCords)-1):
        # Remove the line to create a circle as trajectory
        cv2.circle(img, (xCords[i], yCords[i]), 1, (0, 0, 255), 2)

        # Check if i>0 and only then draw the line

        # Draw line from xCords[i], yCords[i] to (xChords[i-1], ychords[i-1])


while True:
    readVideo = video.read()
    check = readVideo[0]
    if check:
        image = readVideo[1]
        image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
        dimensions = image.shape[:2]
        H = dimensions[0]
        W = dimensions[1]

        if detected == False:
            blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416))
            yoloNetwork.setInput(blob)

            layerName = yoloNetwork.getUnconnectedOutLayersNames()
            layerOutputs = yoloNetwork.forward(layerName)

            boxes = []
            confidences = []
            classIds = []

            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]

                    if confidence > confidenceThreshold:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY,  width, height) = box.astype('int')
                        x = int(centerX - (width/2))
                        y = int(centerY - (height/2))

                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIds.append(classId)

            detectionNMS = cv2.dnn.NMSBoxes(
                boxes, confidences, confidenceThreshold, NMSThreshold)

            if (len(detectionNMS) > 0):
                for i in detectionNMS.flatten():

                    if labels[classIds[i]] == "sports ball":
                        x = boxes[i][0]
                        y = boxes[i][1]
                        w = boxes[i][2]
                        h = boxes[i][3]
                        color = (255, 0, 0)
                        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                        tracker.init(image, boxes[i])
                        detected = True
        else:
            trackerInfo = tracker.update(image)
            success = trackerInfo[0]
            bbox = trackerInfo[1]

            if success:
                drawBox(image, bbox)
            else:
                cv2.putText(image, "Lost", (75, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            goalTrack(image, bbox)

        cv2.imshow('Image', image)
        cv2.waitKey(1)

    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break
