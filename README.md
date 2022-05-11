# pyqt-mac-min-max-close-buttons-widget
PyQt macOS style of min/max/close buttons widget 

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git --upgrade```

## Included Package
* <a href="https://github.com/yjg30737/pyqt-titlebar-buttons-widget.git">pyqt-titlebar-buttons-widget</a> - Parent widget

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

![image](https://user-images.githubusercontent.com/55078043/154260566-706ae34f-37c5-42db-ab8d-90d0d58341db.png)
