# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AXR_KOTRA_MinSave_ui_02.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import csv
import math
import os
import threading
import atexit

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import *

import json
import urllib.request
import sched, time
import datetime

from PyQt5.QtGui import QKeySequence
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1221, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pbStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbStart.sizePolicy().hasHeightForWidth())
        self.pbStart.setSizePolicy(sizePolicy)
        self.pbStart.setObjectName("pbStart")
        self.horizontalLayout_5.addWidget(self.pbStart)
        self.textAdd = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textAdd.sizePolicy().hasHeightForWidth())
        self.textAdd.setSizePolicy(sizePolicy)
        self.textAdd.setObjectName("textAdd")
        self.horizontalLayout_5.addWidget(self.textAdd)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pbGraph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbGraph.sizePolicy().hasHeightForWidth())
        self.pbGraph.setSizePolicy(sizePolicy)
        self.pbGraph.setObjectName("pbGraph")
        self.horizontalLayout_6.addWidget(self.pbGraph)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textStat = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textStat.sizePolicy().hasHeightForWidth())
        self.textStat.setSizePolicy(sizePolicy)
        self.textStat.setObjectName("textStat")
        self.horizontalLayout_4.addWidget(self.textStat)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loGraph01 = QtWidgets.QVBoxLayout()
        self.loGraph01.setObjectName("loGraph01")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.loGraph01.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.loGraph01)
        self.loGraph02 = QtWidgets.QVBoxLayout()
        self.loGraph02.setObjectName("loGraph02")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.loGraph02.addWidget(self.widget_2)
        self.horizontalLayout_2.addLayout(self.loGraph02)
        self.loGraph03 = QtWidgets.QVBoxLayout()
        self.loGraph03.setObjectName("loGraph03")
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.loGraph03.addWidget(self.widget_3)
        self.horizontalLayout_2.addLayout(self.loGraph03)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1223, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 버튼 클릭 명령
        self.pbStart.clicked.connect(self.pbStartClicked)
        self.pbGraph.clicked.connect(self.pbGraphClicked)

        self.path = ''
        self.filepath = ''

        # 그래프 그리기
        self.fig01 = plt.Figure()
        self.canvas01 = FigureCanvas(self.fig01)
        self.toolbar01 = NavigationToolbar(self.canvas01, None)
        self.fig02 = plt.Figure()
        self.canvas02 = FigureCanvas(self.fig02)
        self.toolbar02 = NavigationToolbar(self.canvas02, None)
        self.fig03 = plt.Figure()
        self.canvas03 = FigureCanvas(self.fig03)
        self.toolbar03 = NavigationToolbar(self.canvas03, None)

        self.loGraph01.addWidget(self.canvas01)
        self.loGraph01.addWidget(self.toolbar01)
        self.loGraph02.addWidget(self.canvas02)
        self.loGraph02.addWidget(self.toolbar02)
        self.loGraph03.addWidget(self.canvas03)
        self.loGraph03.addWidget(self.toolbar03)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbStart.setText(_translate("MainWindow", "KOTRA Start"))
        self.pbGraph.setText(_translate("MainWindow", "Graph for 10 min"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "시간"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temp (oC)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hum (%)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TVOC (ppb)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CO2 (ppm)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PM 1.0 (microg/m3)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "PM 2.5 (microg/m3)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PM 10 (microg/m3)"))


    def pbStartClicked(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', "", "url File(*.txt)", '/home')

        if fname[0]:
            # 기존 url 주소 및 status 창 지우기
            self.textAdd.clear()

            i = 0  # 테이블 입력을 위한 위치값

            # txt 파일 첫줄 읽고, http 아니면 메시지 띄우기
            # txt_url 에 파일 경로 표시
            fname = str(fname[0])
            self.textAdd.setText(fname)

            # 선택 파일 경로 정하기
            self.filepath = fname
            self.path = str(os.getcwd())

            self.pbStartClickedFollow()

        else:
            QMessageBox.about(None, "Warning", "파일을 선택하지 않았습니다.")

    def pbStartClickedFollow(self):

        Time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        macAdd = []
        urlAdd = []
        csvpath = ''

        macs = open(self.filepath, 'r')
        macs_lines = macs.readlines()
        for mac in macs_lines:
            macNum = mac.rstrip('\n')
            macAdd.append(macNum)
        num = len(macAdd) # mac 주소 갯수

        # 테이블 줄 수 정하기
        self.tableWidget.setRowCount(num)

        # 현재시간에서 텍스트로 10분전 시간 가져오기
        now = datetime.datetime.now()
        startTime_pre = now + datetime.timedelta(minutes=-10)
        stopTime_pre = now + datetime.timedelta(minutes=-9)
        startTime = startTime_pre.strftime('%Y-%m-%d-%H-%M') + '-00'
        startTimeMean = startTime_pre.strftime('%Y-%m-%d-%H-%M')
        stopTime = stopTime_pre.strftime('%Y-%m-%d-%H-%M') + '-00'
        startDay = startTime_pre.strftime('%Y-%m-%d')
        startDaypath = startTime_pre.strftime('%Y%m%d')

        try:
            if not os.path.exists(self.path + '\\' + startDaypath):
                os.makedirs(self.path + '\\' + startDaypath)
                csvpath = self.path + '\\' + startDaypath
            else:
                csvpath = self.path + '\\' + startDaypath
        except OSError:
            self.statusbar.showMessage(Time + "에 디렉토리 생성 중 에러가 발생했습니다.")


        # 불러 올 url 주소 만들기
        for i in range(0,num):
            urlAddLine = 'https://dashboard.toysmythiot.com/tsg-api/sensor?time=' + startTime + '&time=' + stopTime + '&mac=' + macAdd[i]
            urlAdd.append(urlAddLine)
            MacCsv_new = open(csvpath + '\\' + macAdd[i] + '_' + startTime + '.csv', 'w', encoding='utf-8', newline='')
            MacCsv_new.write(
                "Time,Temp(oC),Humidity(%),TVOC(ppb),CO2(ppm),PM1.0(ug/m3),PM2.5(ug/m3),PM10(ug/m3)\n")
            MacCsv_new.close()

        if True:
            try:
                # 각 url 주소에 따른 파일 만들기
                for i in range(0,num):

                    # json 파일에서 데이터 가져오기
                    url = urlAdd[i]
                    text_data = urllib.request.urlopen(url).read().decode('utf-8')
                    TSData = json.loads(text_data)

                    # 평균값 내기 위한 리스트 만들기
                    listTemp = []
                    listHum = []
                    listTVOC = []
                    listCO2 = []
                    listPM1 = []
                    listPM25 = []
                    listPM10 = []

                    n = 0 # 6개 모일때마다 데이터 저장
                    for data in list(reversed(TSData)): # 뒤에서부터 읽기
                        dataMac = str(data['mac'])  # 맥 주소 저장
                        dataType = str(data['sensortype'])
                        dataVal = str(data['data'])
                        if dataVal == '-32768':
                            dataVal = '0'
                        else:
                            pass
                        dataTime = str(data['time'])

                        # 데이터 저장하기
                        if dataType == '4':
                            dataTemp = dataVal

                        elif dataType == '8':
                            dataHum = dataVal

                        elif dataType == '3':
                            dataTVOC = dataVal

                        elif dataType == '16':
                            dataCO2 = dataVal

                        elif dataType == '20':
                            dataPM1 = dataVal

                        elif dataType == '1':
                            dataPM25 = dataVal

                        elif dataType == '2':
                            dataPM10 = dataVal

                        if n == 6:  # 수집한 데이터 갯수가 7개가 되면 파일에 써넣기
                            n = 0
                            dataRow = [dataTime, dataTemp, dataHum, dataTVOC, dataCO2, dataPM1, dataPM25, dataPM10]
                            # list 에 값 저장하기
                            listTemp.append(dataTemp)
                            listHum.append(dataHum)
                            listTVOC.append(dataTVOC)
                            listCO2.append(dataCO2)
                            listPM1.append(dataPM1)
                            listPM25.append(dataPM25)
                            listPM10.append(dataPM10)

                            csvOpen = open(csvpath + '\\' + macAdd[i] + '_' + startTime + '.csv', 'a', newline='')
                            csvAd = csv.writer(csvOpen)
                            csvAd.writerow(dataRow)
                            csvOpen.close()

                        else:
                            n = n + 1

                    listTemp_temp = list(map(float, list(filter('0'.__ne__, listTemp))))
                    listHum_temp = list(map(float, list(filter('0'.__ne__, listHum))))
                    listTVOC_temp = list(map(float, list(filter('0'.__ne__, listTVOC))))
                    listCO2_temp = list(map(float, list(filter('0'.__ne__, listCO2))))
                    listPM1_temp = list(map(float, list(filter('0'.__ne__, listPM1))))
                    listPM25_temp = list(map(float, list(filter('0'.__ne__, listPM25))))
                    listPM10_temp = list(map(float, list(filter('0'.__ne__, listPM10))))

                    listTemp_temp.remove(max(listTemp_temp))
                    listHum_temp.remove(min(listHum_temp))
                    listTVOC_temp.remove(max(listTVOC_temp))
                    listCO2_temp.remove(min(listCO2_temp))
                    listPM1_temp.remove(min(listPM1_temp))
                    listPM25_temp.remove(min(listPM25_temp))
                    listPM10_temp.remove(min(listPM10_temp))

                    meanTemp = round(np.mean(listTemp_temp), 2)
                    meanHum = round(np.mean(listHum_temp), 2)
                    meanTVOC = round(np.mean(listTVOC_temp), 2)
                    meanCO2 = round(np.mean(listCO2_temp), 2)
                    meanPM1 = round(np.mean(listPM1_temp), 2)
                    meanPM25 = round(np.mean(listPM25_temp), 2)
                    meanPM10 = round(np.mean(listPM10_temp), 2)

                    dataMeanRow = [startTimeMean, meanTemp, meanHum, meanTVOC, meanCO2, meanPM1, meanPM25, meanPM10]
                    csvDay = open(csvpath + '\\' + macAdd[i] + '_' + startDay + '.csv', 'a', newline='')
                    csvDayAd = csv.writer(csvDay)
                    csvDayAd.writerow(dataMeanRow)
                    csvDay.close()

                    # 테이블에 데이터 적기
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(macAdd[i])))
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(startTimeMean)))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(meanTemp)))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(meanHum)))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(meanTVOC)))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(meanCO2)))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(meanPM1)))
                    self.tableWidget.setItem(i, 7, QTableWidgetItem(str(meanPM25)))
                    self.tableWidget.setItem(i, 8, QTableWidgetItem(str(meanPM10)))

                    self.statusbar.showMessage(Time + "에 " + dataMac + "의 데이터가 저장되었습니다.")

            except:
                self.statusbar.showMessage(Time + "에 에러가 발생했습니다.")
                pass

        # 반복
        timer = threading.Timer(60, self.pbStartClickedFollow)
        timer.start()

    def pbGraphClicked(self):

        # 현재 시간에 해당하는 폴더명과 mac 주소 가져오기
        now = datetime.datetime.now()
        startTime_pre = now + datetime.timedelta(minutes=-10)
        startDay = startTime_pre.strftime('%Y-%m-%d')
        startDaypath = startTime_pre.strftime('%Y%m%d')

        macAdd = []
        datanum = 0

        # 그래프 준비
        self.fig01.clear()
        ax01 = self.fig01.add_subplot(111)
        self.fig02.clear()
        ax02 = self.fig02.add_subplot(111)
        self.fig03.clear()
        ax03 = self.fig03.add_subplot(111)

        ax01.set_ylabel('PM1.0 (microg/m3)')
        ax01.set_xlabel('Time')
        # ax01.set_ylim(bottom=0)  # Set Y-axis limits
        ax01.grid()

        ax02.set_ylabel('PM2.5 (microg/m3)')
        ax02.set_xlabel('Time')
        # ax02.set_ylim(bottom=0)  # Set Y-axis limits
        ax02.grid()

        ax03.set_ylabel('TVOCs (ppb)')
        ax03.set_xlabel('Time')
        # ax03.set_ylim(bottom=0)  # Set Y-axis limits
        ax03.grid()

        maxPM1 = []
        maxPM25 = []
        maxTVOC = []

        try:
            macs = open(self.filepath, 'r')
            macs_lines = macs.readlines()
            for mac in macs_lines:
                macNum = mac.rstrip('\n')
                macAdd.append(macNum)
            Num = len(macAdd) # mac 주소 갯수

            # 읽어 올 파일 존재하는 폴더
            csvpath = self.path + '\\' + startDaypath

            # 각 mac 주소마다 파일 읽어들이기
            for i in range(0, Num):
                csvfilepath = csvpath + '\\' + macAdd[i] + '_' + startDay + '.csv'
                TenminData = open(csvfilepath, 'r')
                tempLines = TenminData.readlines()
                LineNum = len(tempLines)
                # 데이터가 10이 안되면 그만큼만 출력, 10이 되면 다 출력
                if LineNum < 10:
                    datanum = LineNum
                else:
                    datanum = 10

                # 그래프 데이터들
                dataTime = []
                dataPM1 = []
                dataPM25 = []
                dataTVOC = []

                # 각 mac 주소의 마지막 10줄 or 마지막 전체 읽어오기
                for j in range(-1*datanum,0):

                        tempData = tempLines[j].rstrip('\n').split(',')

                        # 데이터 저장하기
                        xt = datetime.datetime.strptime(tempData[0], '%Y-%m-%d-%H-%M').time()
                        dataTime.append(xt)
                        TVOC = float(tempData[3])
                        dataTVOC.append(TVOC)
                        PM1 = float(tempData[5])
                        dataPM1.append(PM1)
                        PM25 = float(tempData[6])
                        dataPM25.append(PM25)

                maxPM1.append(max(dataPM1))
                maxPM25.append(max(dataPM25))
                maxTVOC.append(max(dataTVOC))

                ax01.plot(dataTime, dataPM1, '--o', label=macAdd[i])
                ax02.plot(dataTime, dataPM25, '--o', label=macAdd[i])
                ax03.plot(dataTime, dataTVOC, '--o', label=macAdd[i])

            ax01.set_ylim(0, max(maxPM1)*1.3)
            ax02.set_ylim(0, max(maxPM25)*1.3)
            ax03.set_ylim(0, max(maxTVOC)*1.3)

            ax01.legend(loc='upper center', fontsize = 7, bbox_to_anchor=(0.5, 1.1), ncol=3)
            ax02.legend(loc='upper center', fontsize = 7, bbox_to_anchor=(0.5, 1.1), ncol=3)
            ax03.legend(loc='upper center', fontsize = 7, bbox_to_anchor=(0.5, 1.1), ncol=3)

            self.canvas01.draw()
            self.canvas02.draw()
            self.canvas03.draw()

        except FileNotFoundError:
            self.statusbar.showMessage("그래프를 그릴 파일이 존재하지 않습니다.")
            pass

        except ValueError:
            self.statusbar.showMessage("그래프를 그릴 데이터를 읽어드리면서 에러가 발생했습니다.")
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
