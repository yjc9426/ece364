import sys,re

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.Clear)
        self.saveToTargetButton.clicked.connect(self.Save)
        self.loadButton.clicked.connect(self.loadData)
        self.txt=[self.firstNameLineEdit,self.lastNameLineEdit,self.addressLineEdit,self.cityLineEdit,self.stateLineEdit,self.zipLineEdit,self.emailLineEdit]
        for i in self.txt:
            i.textChanged.connect(self.LoadSave)


    def LoadSave(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)

    def Clear(self):
        for i in self.txt:
            i.setText("")
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)
        self.errorInfoLabel.setText("")

    def Save(self):
        self.errorInfoLabel.clear()
        for i in self.txt:
            if i.text() == "":
                self.errorInfoLabel.setText('Error: All entries must be populated.')
                return
        if self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText('Error: State is not valid!')
            return
        n=re.match("[0-9]{5}",self.zipLineEdit.text())
        if n is None:
            self.errorInfoLabel.setText('Error: Zip code is not valid!')
            return
        m = re.search(r'(\w+@\w+\.\w+)', self.emailLineEdit.text())
        if m is None:
            self.errorInfoLabel.setText('Error: Email is not valid!')
            return
        f = open('target.xml', 'w')
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<user>\n')
        f.write('\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n')
        f.write('\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n')
        f.write('\t<Address>' + self.addressLineEdit.text() + '</Address>\n')
        f.write('\t<City>' + self.cityLineEdit.text() + '</City>\n')
        f.write('\t<State>' + self.stateLineEdit.text() + '</State>\n')
        f.write('\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n')
        f.write('\t<Email>' + self.emailLineEdit.text() + '</Email>\n')
        f.write('</user>\n')



    def loadDataFromFile(self, filePath):
        file = open(filePath,'r')
        all_lines=file.readlines()[2:]
        for lines in all_lines:
            lines=lines.strip()
            if 'FirstName' in lines:
                self.firstNameLineEdit.setText(lines[11:-12])
            if 'LastName' in lines:
                self.lastNameLineEdit.setText(lines[10:-11])
            if 'Address' in lines:
                self.addressLineEdit.setText(lines[9:-10])
            if 'City' in lines:
                self.cityLineEdit.setText(lines[6:-7])
            if 'State' in lines:
                self.stateLineEdit.setText(lines[7:-8])
            if 'ZIP' in lines:
                self.zipLineEdit.setText(lines[5:-6])
            if 'Email' in lines:
                self.emailLineEdit.setText(lines[7:-8])


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
