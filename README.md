# pyqt-mac-min-max-close-buttons-widget
PyQt macOS style of min/max/close buttons widget 

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git --upgrade```

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
