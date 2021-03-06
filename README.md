# pyqt-mac-buttons-widget
PyQt macOS style of titlebar buttons (e.g. min/max/close) widget 

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-mac-buttons-widget`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-titlebar-buttons-widget.git">pyqt-titlebar-buttons-widget</a> - Parent widget

## Method Overview
* `MacButtonsWidget(base_widget=None, hint=['min', 'max', 'close']))` - Constructor.
* `getMinimizedBtn()`, `getMaximizedBtn()`, `getCloseBtn()`. I belive these three methods are quite self-explanatory.
* This module is used for <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>'s macOS style button. You can see the example of this module's usage on the documentation at the link above.. later.

## Example
This example is just to show how it looks.

```python
from PyQt5.QtWidgets import QApplication
from pyqt_mac_buttons_widget import MacButtonsWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MacButtonsWidget()
    widget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/154260566-706ae34f-37c5-42db-ab8d-90d0d58341db.png)
