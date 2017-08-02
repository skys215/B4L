# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import main
class Communicate(QtCore.QObject):
    showDialog = QtCore.pyqtSignal(QApplication,QDialog)

class DoingList(QtWidgets.QListWidget):
    def focusInEvent(self, event):
        cur = self.currentRow()
        if cur == -1:
            self.setCurrentRow(0)

        self.setFocus()
        super(DoingList, self).focusInEvent(event)


    def keyPressEvent(self, event):
        if     event.key() == QtCore.Qt.Key_Delete  or event.key() == QtCore.Qt.Key_Enter:
            self.takeItem( self.currentRow() )
            return
        super(DoingList, self).keyPressEvent(event)

class DoingListItemDelegate(QtWidgets.QItemDelegate):
    def editorEvent( self, event, model, option, index):
        print('doinglist item delegate edit event')
        return False

class Ui_Dialog(QtCore.QObject):
    @QtCore.pyqtSlot(QApplication,QDialog)
    def showDialog(self, app, qdialog):
        if qdialog.windowState() == QtCore.Qt.WindowMinimized:
            qdialog.showNormal()
        if app.activeWindow() == None:
            app.setActiveWindow(qdialog)

        qdialog.show()
        self.lineEdit.setFocus()

    def setupUi(self, Dialog):
        Dialog.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint
            | QtCore.Qt.WindowMinimizeButtonHint
            | QtCore.Qt.MSWindowsFixedSizeDialogHint
            # | QtCore.Qt.WindowTitleHint
        )
        self.sig = Communicate()
        self.sig.showDialog.connect(self.showDialog)

        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 350)
        Dialog.setFixedSize(Dialog.size())
        Dialog.setWindowIcon(QtGui.QIcon(main.resource_path("logo.png")))

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 320))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.finishEditing)
        self.verticalLayout.addWidget(self.lineEdit)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.listWidget = DoingList(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidgetItem")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closeKeySeq = QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_W)
        closeKeyShortcut = QtWidgets.QShortcut(closeKeySeq, Dialog)
        closeKeyShortcut.activated.connect( Dialog.close )

        quitKeySeq = QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_Q)
        quitKeyShortcut = QtWidgets.QShortcut(quitKeySeq, Dialog)
        quitKeyShortcut.activated.connect( QApplication.instance().sig.quitApp )


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Doing list"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "I am doing..."))
        self.label.setText(_translate("Dialog", "I was doing:"))

    def finishEditing( self ):
        doing = self.lineEdit.text()
        if len(doing) == 0 :
            return
        self.lineEdit.clear()
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setText(doing)
        self.listWidget.insertItem(0, item)

