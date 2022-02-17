from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from pyqt_min_max_close_buttons_widget import MinMaxCloseButtonsWidget


class MacMinMaxCloseButtonsWidget(MinMaxCloseButtonsWidget):
    def __init__(self, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint):
        super().__init__()
        self.__initVal()
        self.__initUi(hint)

    def __initVal(self):
        self.__size = 20
        self.__border_width = self.__size // 20
        self.__border_radius = self.__size // 2
        self.__macBtnStyle = ''

    def __initUi(self, hint):
        self.layout().setSpacing(0)

        btns = [self._closeBtn, self._minimizeBtn, self._maximizeBtn]
        colors = ['#DD0000', '#AA8800', '#008800']
        for i in range(len(btns)):
            btn = btns[i]
            btn.setFixedSize(self.__size, self.__size)
            self.setStyleForEachButton(btn, colors[i])

    def setStyleForEachButton(self, btn, color):
        border_color = QColor(color)
        border_color_name = border_color.name()
        background_color_name = border_color.lighter().name()

        self.__macBtnStyle = f'''
                             QToolButton
                             {{ 
                             background-color: {background_color_name};
                             border: {self.__border_width} solid {border_color_name};
                             border-radius: {self.__border_radius};
                             }}
                             '''

        btn.setStyleSheet(self.__macBtnStyle)