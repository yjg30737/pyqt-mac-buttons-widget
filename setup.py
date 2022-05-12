from setuptools import setup, find_packages

setup(
    name='pyqt-mac-buttons-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt macOS style of titlebar buttons (e.g. min/max/close) widget',
    url='https://github.com/yjg30737/pyqt-mac-buttons-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-titlebar-buttons-widget>=0.0.1'
    ]
)