# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jugador.ui'
#
# Created: Fri Apr  6 14:05:36 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form_altas(object):
    def setupUi(self, Form_altas):
        Form_altas.setObjectName(_fromUtf8("Form_altas"))
        Form_altas.resize(244, 174)
        self.verticalLayout = QtGui.QVBoxLayout(Form_altas)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(Form_altas)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.le_id = QtGui.QLineEdit(Form_altas)
        self.le_id.setEnabled(False)
        self.le_id.setObjectName(_fromUtf8("le_id"))
        self.gridLayout.addWidget(self.le_id, 0, 1, 1, 1)
        self.label = QtGui.QLabel(Form_altas)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.le_nombre = QtGui.QLineEdit(Form_altas)
        self.le_nombre.setObjectName(_fromUtf8("le_nombre"))
        self.gridLayout.addWidget(self.le_nombre, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form_altas)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.le_nick = QtGui.QLineEdit(Form_altas)
        self.le_nick.setObjectName(_fromUtf8("le_nick"))
        self.gridLayout.addWidget(self.le_nick, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form_altas)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.le_edad = QtGui.QLineEdit(Form_altas)
        self.le_edad.setObjectName(_fromUtf8("le_edad"))
        self.gridLayout.addWidget(self.le_edad, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form_altas)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.le_rating = QtGui.QLineEdit(Form_altas)
        self.le_rating.setObjectName(_fromUtf8("le_rating"))
        self.gridLayout.addWidget(self.le_rating, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.pb_aceptar = QtGui.QPushButton(Form_altas)
        self.pb_aceptar.setObjectName(_fromUtf8("pb_aceptar"))
        self.gridLayout_2.addWidget(self.pb_aceptar, 1, 0, 1, 1)
        self.pb_cancelar = QtGui.QPushButton(Form_altas)
        self.pb_cancelar.setObjectName(_fromUtf8("pb_cancelar"))
        self.gridLayout_2.addWidget(self.pb_cancelar, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Form_altas)
        QtCore.QMetaObject.connectSlotsByName(Form_altas)

    def retranslateUi(self, Form_altas):
        Form_altas.setWindowTitle(QtGui.QApplication.translate("Form_altas", "Jugador", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form_altas", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form_altas", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form_altas", "Nick", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form_altas", "Edad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form_altas", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_aceptar.setText(QtGui.QApplication.translate("Form_altas", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_cancelar.setText(QtGui.QApplication.translate("Form_altas", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

