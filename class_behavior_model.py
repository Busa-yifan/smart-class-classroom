# 内置 python 时间模块，这里准备用来计算每一帧视频的耗费
import time
# 用来调用摄像头与图形相关的函数功能
import cv2
import numpy as np
# 整个神经网络建构于此模块中，用以导出最终计算结果
from darkflow.net.build import TFNet


condition = {
    'model': 'cfg/tiny-yolo-voc-44c.cfg',
    'load': 3000,
    'threshold': 0.05,
    'gpu': 1
}
net = TFNet(condition)

def addlabel(img):
    normal_num = 0;
    phone_num = 0;
    sleep_num = 0;
    person_sum = 0;
    results = net.return_predict(img)
    for result in results:
        LABEL = result['label']
        CONF = result['confidence']
        TLC = (result['topleft']['x'], result['topleft']['y'])
        BRC = (result['bottomright']['x'], result['bottomright']['y'])
        note = '{}: {:.0f}%'.format(LABEL, CONF * 100)
        if(CONF>0.3):
            person_sum += 1
            if(LABEL=='normal'):
                normal_num+=1
                color = [0,255,0]
            elif(LABEL=='sleep'):
                sleep_num+=1
                color = [255,255,0]
            elif (LABEL == 'phone'):
                phone_num+=1
                color = [0, 0, 255]
            img = cv2.rectangle(img, TLC, BRC, color, 2)
            img = cv2.putText(img, note, TLC, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    return img,person_sum,normal_num,phone_num,sleep_num

