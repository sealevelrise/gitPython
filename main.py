# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import sys,os
import PySide6
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import sys, math
from PySide6.QtCore import QDateTime, Qt, QTimer, QPointF
from PySide6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis, QScatterSeries

from PySide6.QtWidgets  import QMainWindow ,QApplication

from untitled_ui import Ui_MainWindow
from PySide6.QtGui import *

#
def ethernet(name):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    host = socket.gethostname()
    port = 8080
    s.connect((host,port))
    print("Send:",len(name))
    s.send(name.encode('utf-8'))
    msg = s.recv(200)
    s.close
    print("Recv:",len(msg),'\n',msg.decode('utf-8'))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')



class main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chart = QChart()  # Create Chart
        self.chart.setTitle("Data curve")
        self.graphicsView.setChart(self.chart)


        self.axisX = QValueAxis()
        self.axisX.setRange(200, 500)  # Setup
        self.axisX.setLabelFormat("%d")  # Flag
        self.axisX.setTickCount(5)  # Main
        #axisX.setMinorTickCount(4)
        self.axisX.setTitleText("x")  # Title
        # axisX.setGridLineVisible(True)
        self.axisX.setMinorGridLineVisible(False)

        self.axisY = QValueAxis()
        self.axisY.setRange(50, 200)
        self.axisY.setLabelFormat("%d")  # Tag
        self.axisY.setTickCount(4)
        #axisY.setMinorTickCount(4)
        self.axisY.setTitleText("y")
        # axisY.setGridLineVisible(True)
        self.axisY.setMinorGridLineVisible(False)

        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)

        self.seriesS = QScatterSeries()
        self.seriesL = QLineSeries()
        self.seriesS.setName("Coordinate points")
        self.seriesL.setName("fitting line")
        self.chart.addSeries(self.seriesS)
        self.chart.addSeries(self.seriesL)
        self.chart.setAxisX(self.axisX, self.seriesS)  # 
        self.chart.setAxisY(self.axisY, self.seriesS)

        self.chart.setAxisX(self.axisX, self.seriesL)  # 
        self.chart.setAxisY(self.axisY, self.seriesL)

    def jisuan(self):
        self.seriesS.clear()
        self.seriesL.clear()

        x = [250, 300, 350, 400, 450]
        y = [86, 100, 114, 128, 142]

        for i in range(5):
            point = QPointF(x[i], y[i])
            self.seriesS.append(point)

        t = 250
        for i in range(11):
            y = 0.2 * t + 12
            self.seriesL.append(t, y)
            t += 20

    def qingchu(self):
        self.seriesS.clear()
        self.seriesL.clear()
        self.chart.addSeries(self.seriesS)
        self.chart.addSeries(self.seriesL)
        self.lineEdit.setText('0')

    #@QtCore.Slot()#
    def slot1(self):
        print_hi('Draw Chart')
        self.label.setText('Draw Chart')
        self.jisuan()
        num = float(self.lineEdit.text())
        print("%f",num)
        self.lineEdit.setText(f"{num}")
        #wind.close()
    
    def slot2(self):
        print_hi('windows quit')
        sys.exit(app.exec_())
    
    def slot3(self):
        print_hi('about')
        ethernet('about')
    
    def slot4(self):
        print_hi('Clear')
        self.label.setText('Cleared')
        self.qingchu()

    
if __name__ == "__main__":
    print_hi('windows open')
    app = QApplication(sys.argv)
    wind = main()
    wind.setWindowTitle("pyside6 test")
    wind.show()
    print_hi('windows exit')
    sys.exit(app.exec_())
