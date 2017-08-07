# -*- coding: utf-8 -*-
# pyuic5 -o firstPyQt5.py firstPyQt5.ui
#  pyinstaller --onefile --noconsole --paths="C:\Users\skys215\AppData\Local\Programs\Python\Python35\Lib\site-packages\PyQt5\Qt\bin" -r E:\SourceCodes\DesktopApp\testQ t\testPyQt\logo.png -i E:\SourceCodes\DesktopApp\testQt\testPyQt\logo.ico main2.py
# https://github.com/Xcelled/shortyQt
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QDialog, QDesktopWidget

# from maindialog import *
from systray import *
from mainWindow import *
import keyboard

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

class Communicate(QtCore.QObject):
    quitApp = QtCore.pyqtSignal()
    activateApp = QtCore.pyqtSignal()

if __name__ == '__main__':
    '''
    主函数
    '''
    def closeEvent():
        quit_msg = "你确定要退出吗？"
        activateEvent()
        reply = QtWidgets.QMessageBox.question(mainDialog, 'Message',
                         quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()

    def activateEvent():
        ui.sig.showDialog.emit(app,mainDialog)

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    app.sig = Communicate()
    app.sig.quitApp.connect(closeEvent)
    app.sig.activateApp.connect(activateEvent)


    if (not QSystemTrayIcon.isSystemTrayAvailable()):
        QMessageBox.critical(None, QObject.tr("系统托盘"), QObject.tr("不支持系统托盘"))
        sys.exit(1)

    mainDialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(mainDialog)
    # mainDialog.show()

    mainWidget = QDesktopWidget()
    wid = Ui_SysTray()
    wid.setupUi( mainWidget, app )
    #mainWidget.show()

    QApplication.setQuitOnLastWindowClosed(False)

    keyboard.add_hotkey('ctrl+alt+d', activateEvent)

    sys.exit(app.exec_())

