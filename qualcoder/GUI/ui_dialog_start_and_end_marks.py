# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_start_and_end_marks.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_StartAndEndMarks(object):
    def setupUi(self, Dialog_StartAndEndMarks):
        Dialog_StartAndEndMarks.setObjectName("Dialog_StartAndEndMarks")
        Dialog_StartAndEndMarks.resize(598, 287)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_StartAndEndMarks)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_StartAndEndMarks)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 551, 51))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_endmark = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_endmark.setGeometry(QtCore.QRect(150, 120, 221, 27))
        self.lineEdit_endmark.setObjectName("lineEdit_endmark")
        self.lineEdit_startmark = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_startmark.setGeometry(QtCore.QRect(150, 80, 221, 27))
        self.lineEdit_startmark.setObjectName("lineEdit_startmark")
        self.label_title = QtWidgets.QLabel(self.groupBox)
        self.label_title.setGeometry(QtCore.QRect(10, 47, 381, 20))
        self.label_title.setObjectName("label_title")
        self.label_startmark = QtWidgets.QLabel(self.groupBox)
        self.label_startmark.setGeometry(QtCore.QRect(10, 80, 131, 17))
        self.label_startmark.setObjectName("label_startmark")
        self.label_endmark = QtWidgets.QLabel(self.groupBox)
        self.label_endmark.setGeometry(QtCore.QRect(10, 120, 131, 17))
        self.label_endmark.setObjectName("label_endmark")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(360, 220, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_files = QtWidgets.QLabel(self.groupBox)
        self.label_files.setGeometry(QtCore.QRect(10, 159, 551, 51))
        self.label_files.setWordWrap(True)
        self.label_files.setObjectName("label_files")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog_StartAndEndMarks)
        self.buttonBox.accepted.connect(Dialog_StartAndEndMarks.accept)
        self.buttonBox.rejected.connect(Dialog_StartAndEndMarks.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_StartAndEndMarks)
        Dialog_StartAndEndMarks.setTabOrder(self.lineEdit_startmark, self.lineEdit_endmark)
        Dialog_StartAndEndMarks.setTabOrder(self.lineEdit_endmark, self.buttonBox)

    def retranslateUi(self, Dialog_StartAndEndMarks):
        _translate = QtCore.QCoreApplication.translate
        Dialog_StartAndEndMarks.setWindowTitle(_translate("Dialog_StartAndEndMarks", "Define start and end marks for auto assigning"))
        self.label_2.setText(_translate("Dialog_StartAndEndMarks", "Define the start and end text marks."))
        self.label_title.setText(_translate("Dialog_StartAndEndMarks", "."))
        self.label_startmark.setText(_translate("Dialog_StartAndEndMarks", "Start mark"))
        self.label_endmark.setText(_translate("Dialog_StartAndEndMarks", "End mark"))
        self.label_files.setText(_translate("Dialog_StartAndEndMarks", "File(s):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_StartAndEndMarks = QtWidgets.QDialog()
    ui = Ui_Dialog_StartAndEndMarks()
    ui.setupUi(Dialog_StartAndEndMarks)
    Dialog_StartAndEndMarks.show()
    sys.exit(app.exec_())
