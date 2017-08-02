# -*- coding: utf-8 -*-
import sys
import main
from PyQt5.QtCore import QUrl, QObject
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QWidgetAction, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
class Ui_SysTray(QtCore.QObject):
    def setupUi(self, widget, app):
        systray = QSystemTrayIcon( QtGui.QIcon(main.resource_path("logo.png")), widget)
        systray.setToolTip("B4L")
        systray.activated.connect(lambda reason: self.iconTriggered(reason, app))

        tray_icon_menu = QMenu(None)
        openAction = tray_icon_menu.addAction('Open')
        openAction.triggered.connect(app.sig.activateApp.emit)
        exitAction = tray_icon_menu.addAction('Exit')
        exitAction.triggered.connect(app.sig.quitApp.emit)

        systray.setContextMenu(tray_icon_menu)
        systray.show()

    def iconTriggered(self, reason, app):
        if reason == QSystemTrayIcon.DoubleClick:
            app.sig.activateApp.emit()
