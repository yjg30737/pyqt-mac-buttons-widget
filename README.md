# pyqt-mac-min-max-close-buttons-widget
PyQt macOS style of min/max/close buttons widget 

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git --upgrade```

## Usage
* ```MacMinMaxCloseButtonsWidget(hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)``` - Constructor.
* ```getMinimizedBtn()```, ```getMaximizedBtn()```, ```getCloseBtn()```. I belive these three methods are quite self-explanatory.
* This module is used for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s macOS style button. You can see the example of this module's usage on the documentation at the link above.. later.

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_mac_min_max_close_buttons_widget import MacMinMaxCloseButtonsWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MacMinMaxCloseButtonsWidget()
    widget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/153992019-de4b5e29-2674-4dd0-9253-82d63daad647.png)
