from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication


class MacMinMaxCloseButtonsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__size = 20
        self.__border_width = self.__size // 20
        self.__border_radius = self.__size // 2

    def __initUi(self):

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)
        minimizeBtn = QPushButton()
        minimizeBtn.clicked.connect(self.showMinimized)
        maximizeBtn = QPushButton()
        maximizeBtn.clicked.connect(self.showMaximized)

        lay = QHBoxLayout()

        btns = [closeBtn, minimizeBtn, maximizeBtn]
        colors = ['#DD0000', '#AA8800', '#008800']
        for i in range(len(btns)):
            btn = btns[i]
            btn.setFixedSize(self.__size, self.__size)
            self.setStyleForEachButton(btn, colors[i])
            lay.addWidget(btn)
        self.setLayout(lay)

    def setStyleForEachButton(self, btn, color):
        border_color = QColor(color)
        border_color_name = border_color.name()
        background_color_name = border_color.lighter().name()

        self.__macBtnStyle = f'''
                             QPushButton
                             {{ 
                             background-color: {background_color_name};
                             border: {self.__border_width} solid {border_color_name};
                             border-radius: {self.__border_radius};
                             }}
                             '''

        btn.setStyleSheet(self.__macBtnStyle)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MacMinMaxCloseButtonsWidget()
    ex.show()
    app.exec_()
