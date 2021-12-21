# Our Libraries (only openCV);
import cv2

#setting up the video capture;
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640)
video_capture.set(4, 480)

#getting our names files so that we can identify objects (coco.names is on yolov3 pretty sure)
_names = []
_files = 'coco.names'
with open(_files, 'rt') as f:
    _names = f.read().rstrip('\n').split('\n')

_threshold = 0.45

#our configuration and weights
configurations = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weights = 'frozen_inference_graph.pb'

#Setting up the detection
net = cv2.dnn_DetectionModel(configPath, weightsPath)
net.setInputSize(320, 320)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#Our loop to detect everything
while True:
    new_, img = cap.read()

    cv2.imshow("DETECTION HAHAHA", img)
    cv2.waitKey(1)

    IDS, Configuration_, boundingBox_ = net.detect(img, confThreshold = 0.5)

    if len(classIds) != 0:
      for ID, Conf, B in zip(
          IDS.flatten(),
          Configuration_.flatten(),
          boundingBox_):
        
        cv2.rectangle(
            
            img,
            box, color = (0, 255, 0),
            thickness = 2
        )
        
        cv2.putText(
            
            img, 
            classNames[classId-1],
            (box[0]+10, box[1]+30),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (0, 255, 0),
            2
            
        )
