# Import PySide classes
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *
import sys
import string
import math

class simpleCalc(QMainWindow, Ui_MainWindow):
    curnum=0
    prenum=0
    numString=''
    op = ''
    ans=0

    def __init__(self,parent = None):
        super(simpleCalc, self).__init__(parent)
        self.setupUi(self)
        self.buttons = [self.bt1, self.bt2, self.bt3,self.bt4,self.bt5,self.bt6,self.bt7,self.bt8,self.bt9,self.bt0,self.btdot]
        self.sign = [self.btplus,self.btminus,self.btmult,self.btdiv]
        for button in self.sign:
            button.clicked.connect(self.opButton)
        self.btpushed = 0
        self.btclear.clicked.connect(self.clrButton)
        for button in self.buttons:
            button.clicked.connect(self.numButton)
        self.bteq.clicked.connect(self.eqClick)
        self.prenum = 0
        self.curnum = 0
        self.numString = ''
        self.ans = 0
        self.op = ''

    def numButton(self):
        self.numString = self.numString + self.sender().text()
        self.lineEdit.setText(self.numString)
        self.curnum = float(self.numString)

    def clrButton(self):
        self.numString = ''
        self.lineEdit.setText('0')
        self.curnum = 0
        self.prenum = 0


    def display(self,value):
        self.numString = str(value)
        if self.checkbox.isChecked:
            num = self.numString.split('.')
            newString = ''
            [d,m]=divmod(len(num[0]),3)
            if d > 1:
                for n in range(len(num)):
                    if d > 1 and (len(num)-n)%3 == 0:
                        newString += str(num[n-1]) + ','
                    else:
                        newString += str(num[n-1])
            self.numString = newString
        self.lineEdit.setText(self.numString)

    def opButton(self):
        self.btpushed = 0
        self.prenum = self.curnum
        self.curnum = 0
        self.numString = ''
        self.op = self.sender().objectName()

    def eqClick(self):
        if self.op == 'btplus':
            self.ans = self.prenum + self.curnum
        if self.op == 'btminus':
            self.ans = self.prenum - self.curnum
        if self.op == 'btmul':
            self.ans = self.prenum * self.curnum
        if self.op == 'btdiv':
            self.ans = self.prenum / self.curnum
        self.curnum = self.ans
        self.numString = ''
        self.display(self.ans)


if __name__ == "__main__":
    currentApp = QApplication([])
    currentForm = simpleCalc()

    currentForm.show()
    currentApp.exec_()