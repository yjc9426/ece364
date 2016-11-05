import sys,re

from PySide.QtGui import *
from SteganographyGUI import *
from Steganography import *
from PySide.QtCore import *


class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(SteganographyConsumer, self).__init__(parent)
        self.setupUi(self)
        self.pl = False
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
         if e.mimeData().hasFormat('text/plain'):
             print(e.mimeData().text())
             e.accept()
         else:
             e.ignore()

    def dropEvent(self, e):
        m = re.findall(r'test_images/[A-Za-z0-9]+.png',e.mimeData().text())
        file = m[0]
        print(file)
        #position = QPointF(e.scenePos())
        #print(position)
        self.loadPic(file)


    def loadPic(self,file):
        self.sc = QGraphicsScene()
        self.sc.addPixmap(QPixmap(file))
        self.viewPayload1.setScene(self.sc)
        self.viewPayload1.fitInView(self.sc.sceneRect())
        self.viewPayload1.setHidden(False)
        self.viewPayload1.setEnabled(True)
        self.pl = True
        img = imread(file)
        payload=Payload(img=img,compressionLevel=-1)
        siz = (payload.img & 1).size
        print(siz)
        self.txtPayloadSize.setText(str(payload.img.size))
        if self.chkApplyCompression.isChecked():
            pass



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()

    currentForm.show()
    currentApp.exec_()
