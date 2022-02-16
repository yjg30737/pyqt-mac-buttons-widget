from setuptools import setup, find_packages

setup(
    name='pyqt-mac-min-max-close-buttons-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Mac min/max/close buttons widget',
    url='https://github.com/yjg30737/pyqt-mac-min-max-close-buttons-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-min-max-close-buttons-widget @ git+https://git@github.com/yjg30737/pyqt-min-max-close-buttons-widget.git@main'
    ]
)