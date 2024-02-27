from ultralytics import YOLO
import cv2
from collections import defaultdict
import numpy as np
from matplotlib import pyplot as plt
import base64
from datetime import datetime
#  uvicorn controller:app --reload
class ProcessImg:

    def __init__(self) -> None:
        self.model : YOLO = YOLO("./Model/best.pt")   
        #self.model : YOLO = YOLO("yolov8m.pt")
    
    def process(self, x64: str):
        picture_name = str(datetime.now()).replace(" ","-").replace(":", "-").replace(".", "-")
        file = 'C:/HoleDetector/%s.png' %picture_name
        print(file)
        img_array = np.frombuffer(base64.b64decode(x64), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        results = self.model(img, stream=True)

        for result in results:
            img = result.plot()
            data = result.boxes
            result.save(filename= file)  

        # plt.figure(figsize=(10, 10))
        # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # plt.axis('off')
        # plt.show()
        return data.data.size(0), file
        
