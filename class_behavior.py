# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class_behavior.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import cv2
import threading
import os
import class_behavior_model
import time

class Ui_Dialog_class_behavior(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 1051, 741))
        self.label_2.setStyleSheet("QLabel{\n"
"background:white;;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 790, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 80, 111, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 80, 61, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 80, 161, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(880, 510, 101, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(880, 190, 111, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(880, 290, 111, 41))
        self.label_7.setObjectName("label_7")
        self.label_photo = QtWidgets.QLabel(Dialog)
        self.label_photo.setGeometry(QtCore.QRect(40, 150, 821, 501))
        self.label_photo.setStyleSheet("QLabel{\n"
"    background:blue;\n"
"}")
        self.label_photo.setObjectName("label_photo")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 80, 111, 41))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(480, 80, 101, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(710, 80, 111, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(980, 290, 111, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(990, 510, 111, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(990, 190, 120, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(50, 700, 151, 41))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(200, 700, 120, 41))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(580, 700, 120, 41))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(400, 700, 161, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(800, 700, 161, 41))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(940, 700, 120, 41))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(880, 400, 111, 41))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(990, 400, 111, 41))
        self.label_22.setObjectName("label_22")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_photo.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.pushButton_2.raise_()


        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)


        threads = []
        t1 = threading.Thread(target=self.showtime)
        threads.append(t1)
        t2 = threading.Thread(target=self.showcamera)
        threads.append(t2)
        for t in threads:
            t.setDaemon(False)
            t.start()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">教室号：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">班级：</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">正在上的课程是：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">目前人数：</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">上课时间：</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">总人数：</span></p></body></html>"))
        self.label_photo.setText(_translate("Dialog", "我是图片"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">钟海楼03021</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">离散数学</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">软件工程1164</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">6</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">5</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">18:01</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">正常人数/占比：</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">3人/60%</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">1人/20%</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">玩手机人数/占比：</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">睡觉人数/占比：</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">1人/20%</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">签到人数：</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">6</span></p></body></html>"))


    def showcamera(self):
        _translate = QtCore.QCoreApplication.translate
        vc = cv2.VideoCapture('G:/test/tiaozhanbeidataset/video/class_2.mp4')
        while(1):
                # get a frame
                ret, img = vc.read()
                img,person_sum,normal_num,phone_num,sleep_num = class_behavior_model.addlabel(img) # 加上标签

                self.label_13.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:14pt;\">"+str(person_sum)+"</span></p></body></html>"))
                normal_percent = "%.2f%%" % ((normal_num / person_sum)*100)
                phone_percent ="%.2f%%" % ((phone_num / person_sum)*100)
                sleep_percent = "%.2f%%" % ((sleep_num / person_sum)*100)
                self.label_16.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:12pt;\">"+str(normal_num)+"人/"+str(normal_percent)+"</span></p></body></html>"))
                self.label_17.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:12pt;\">"+str(phone_num)+"人/"+str(phone_percent)+"</span></p></body></html>"))
                self.label_20.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:12pt;\">"+str(sleep_num)+"人/"+str(sleep_percent)+"</span></p></body></html>"))

                height, width, bytesPerComponent = img.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                # 转为QImage对象
                self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.label_photo.setPixmap(QPixmap.fromImage(self.image).scaled(self.label_photo.width(), self.label_photo.height()))
                #cv2.waitKey(10)


    def showtime(self):
        _translate = QtCore.QCoreApplication.translate
        second = 0
        min = 0
        hour = 0
        while(1):
            time.sleep(1)
            second+=1
            if(second==60):
                second = 0
                min+=1
            if(min==60):
                min = 0
                hour+=1
            self.label_14.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:14pt;\">"+str('%02d' % hour)+":"+str('%02d' % min)+":"+str('%02d' % second)+"</span></p></body></html>"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_class_behavior()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())