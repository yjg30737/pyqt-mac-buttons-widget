from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class MacMinMaxCloseButtonsWidget(QWidget):
    def __init__(self, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self.__size = 20
        self.__border_width = self.__size // 20
        self.__border_radius = self.__size // 2
        self.__macBtnStyle = ''

        self.__closeBtn = QPushButton()
        self.__minimizeBtn = QPushButton()
        self.__maximizeBtn = QPushButton()

    def __initUi(self, hint):
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(2)

        btns = [self.__closeBtn, self.__minimizeBtn, self.__maximizeBtn]
        colors = ['#DD0000', '#AA8800', '#008800']
        for i in range(len(btns)):
            btn = btns[i]
            btn.setFixedSize(self.__size, self.__size)
            self.setStyleForEachButton(btn, colors[i])

        if hint == Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self.__minimizeBtn)
            lay.addWidget(self.__maximizeBtn)
            lay.addWidget(self.__closeBtn)
        elif hint == Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint:
            lay.addWidget(self.__minimizeBtn)
            lay.addWidget(self.__closeBtn)
        elif hint == Qt.WindowCloseButtonHint:
            lay.addWidget(self.__closeBtn)
        else:
            # todo for another type of flags
            pass

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

    def getMinimizedBtn(self):
        return self.__minimizeBtn

    def getMaximizedBtn(self):
        return self.__maximizeBtn

    def getCloseBtn(self):
        return self.__closeBtn