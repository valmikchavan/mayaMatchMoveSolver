# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/share/Users/catte/dev/mayaMatchMoveSolver/python/mmSolver/tools/loadmarker/ui/loadmarker_layout.ui'
#
# Created: Sat Dec 22 10:02:21 2018
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 413)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.filepath_horizontalLayout = QtGui.QHBoxLayout()
        self.filepath_horizontalLayout.setObjectName("filepath_horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.filepath_horizontalLayout.addItem(spacerItem1)
        self.filepath_label = QtGui.QLabel(Form)
        self.filepath_label.setObjectName("filepath_label")
        self.filepath_horizontalLayout.addWidget(self.filepath_label)
        self.filepath_lineEdit = QtGui.QLineEdit(Form)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.filepath_horizontalLayout.addWidget(self.filepath_lineEdit)
        self.filepath_pushButton = QtGui.QPushButton(Form)
        self.filepath_pushButton.setObjectName("filepath_pushButton")
        self.filepath_horizontalLayout.addWidget(self.filepath_pushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.filepath_horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.filepath_horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.fileInfo_horizontalLayout = QtGui.QHBoxLayout()
        self.fileInfo_horizontalLayout.setObjectName("fileInfo_horizontalLayout")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.fileInfo_horizontalLayout.addItem(spacerItem4)
        self.fileInfo_plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.fileInfo_plainTextEdit.setObjectName("fileInfo_plainTextEdit")
        self.fileInfo_horizontalLayout.addWidget(self.fileInfo_plainTextEdit)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.fileInfo_horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.fileInfo_horizontalLayout)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.loadoptions_verticalLayout = QtGui.QVBoxLayout()
        self.loadoptions_verticalLayout.setSpacing(6)
        self.loadoptions_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadoptions_verticalLayout.setObjectName("loadoptions_verticalLayout")
        self.camera_horizontalLayout = QtGui.QHBoxLayout()
        self.camera_horizontalLayout.setObjectName("camera_horizontalLayout")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.camera_horizontalLayout.addItem(spacerItem7)
        self.camera_label = QtGui.QLabel(Form)
        self.camera_label.setObjectName("camera_label")
        self.camera_horizontalLayout.addWidget(self.camera_label)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.camera_horizontalLayout.addItem(spacerItem8)
        self.camera_comboBox = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_comboBox.sizePolicy().hasHeightForWidth())
        self.camera_comboBox.setSizePolicy(sizePolicy)
        self.camera_comboBox.setObjectName("camera_comboBox")
        self.camera_horizontalLayout.addWidget(self.camera_comboBox)
        self.cameraUpdate_pushButton = QtGui.QPushButton(Form)
        self.cameraUpdate_pushButton.setObjectName("cameraUpdate_pushButton")
        self.camera_horizontalLayout.addWidget(self.cameraUpdate_pushButton)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.camera_horizontalLayout.addItem(spacerItem9)
        self.loadoptions_verticalLayout.addLayout(self.camera_horizontalLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.loadoptions_verticalLayout.addWidget(self.line)
        self.imageRes_horizontalLayout = QtGui.QHBoxLayout()
        self.imageRes_horizontalLayout.setObjectName("imageRes_horizontalLayout")
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.imageRes_horizontalLayout.addItem(spacerItem10)
        self.imageResWidth_label = QtGui.QLabel(Form)
        self.imageResWidth_label.setObjectName("imageResWidth_label")
        self.imageRes_horizontalLayout.addWidget(self.imageResWidth_label)
        self.imageResWidth_spinBox = QtGui.QSpinBox(Form)
        self.imageResWidth_spinBox.setMaximum(99999)
        self.imageResWidth_spinBox.setObjectName("imageResWidth_spinBox")
        self.imageRes_horizontalLayout.addWidget(self.imageResWidth_spinBox)
        self.imageResHeight_spinBox = QtGui.QSpinBox(Form)
        self.imageResHeight_spinBox.setMaximum(99999)
        self.imageResHeight_spinBox.setObjectName("imageResHeight_spinBox")
        self.imageRes_horizontalLayout.addWidget(self.imageResHeight_spinBox)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.imageRes_horizontalLayout.addItem(spacerItem11)
        self.loadoptions_verticalLayout.addLayout(self.imageRes_horizontalLayout)
        self.verticalLayout_4.addLayout(self.loadoptions_verticalLayout)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.filepath_label.setText(QtGui.QApplication.translate("Form", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.filepath_pushButton.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.camera_label.setText(QtGui.QApplication.translate("Form", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraUpdate_pushButton.setText(QtGui.QApplication.translate("Form", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))
        self.imageResWidth_label.setText(QtGui.QApplication.translate("Form", "Image Resolution", None, QtGui.QApplication.UnicodeUTF8))
