from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import*
from a import Ui_AntennaCalulator
import antennafunctions

class mwin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_AntennaCalulator()
        self.ui.setupUi(self)
        self.ui.Calculate.clicked.connect(self.calculator)
        self.ui.Quit.clicked.connect(QCoreApplication.instance().quit)
       #♣  self.ui.er.valueChanged.connect(self.er_v)
        xw =1235.433





    def calculator(self):
        er_v = self.ui.er.value()
        he_v = self.ui.he.value()
        fc_v = self.ui.fc.value()
        x =antennafunctions.weight_cal(er_v,fc_v)
        y =antennafunctions.height_cal(er_v,fc_v,he_v)
        self.ui.An_W.clear()
        self.ui.An_L.clear()
        self.ui.An_W.append(str(x))
        self.ui.An_L.append(str(y))



















uygulama = QApplication([])
window = mwin()
window.show()
uygulama.exec_()