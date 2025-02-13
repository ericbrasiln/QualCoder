# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_speech_to_text.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSpeechToText(object):
    def setupUi(self, DialogSpeechToText):
        DialogSpeechToText.setObjectName("DialogSpeechToText")
        DialogSpeechToText.resize(734, 431)
        DialogSpeechToText.setMinimumSize(QtCore.QSize(734, 431))
        DialogSpeechToText.setMaximumSize(QtCore.QSize(734, 431))
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSpeechToText)
        self.buttonBox.setGeometry(QtCore.QRect(500, 380, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox_service = QtWidgets.QComboBox(DialogSpeechToText)
        self.comboBox_service.setGeometry(QtCore.QRect(30, 40, 281, 25))
        self.comboBox_service.setObjectName("comboBox_service")
        self.comboBox_service.addItem("")
        self.comboBox_service.addItem("")
        self.comboBox_service.addItem("")
        self.comboBox_service.addItem("")
        self.comboBox_service.addItem("")
        self.label_service = QtWidgets.QLabel(DialogSpeechToText)
        self.label_service.setGeometry(QtCore.QRect(30, 10, 461, 17))
        self.label_service.setObjectName("label_service")
        self.label_ffmpeg_info = QtWidgets.QLabel(DialogSpeechToText)
        self.label_ffmpeg_info.setGeometry(QtCore.QRect(30, 140, 281, 61))
        self.label_ffmpeg_info.setWordWrap(True)
        self.label_ffmpeg_info.setObjectName("label_ffmpeg_info")
        self.textEdit_notes = QtWidgets.QTextEdit(DialogSpeechToText)
        self.textEdit_notes.setGeometry(QtCore.QRect(330, 40, 381, 191))
        self.textEdit_notes.setReadOnly(True)
        self.textEdit_notes.setObjectName("textEdit_notes")
        self.label_language = QtWidgets.QLabel(DialogSpeechToText)
        self.label_language.setGeometry(QtCore.QRect(160, 80, 141, 17))
        self.label_language.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_language.setObjectName("label_language")
        self.lineEdit_language = QtWidgets.QLineEdit(DialogSpeechToText)
        self.lineEdit_language.setGeometry(QtCore.QRect(220, 100, 91, 25))
        self.lineEdit_language.setObjectName("lineEdit_language")
        self.label_id = QtWidgets.QLabel(DialogSpeechToText)
        self.label_id.setEnabled(False)
        self.label_id.setGeometry(QtCore.QRect(30, 240, 291, 17))
        self.label_id.setObjectName("label_id")
        self.lineEdit_id = QtWidgets.QLineEdit(DialogSpeechToText)
        self.lineEdit_id.setEnabled(False)
        self.lineEdit_id.setGeometry(QtCore.QRect(20, 260, 681, 25))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_key = QtWidgets.QLabel(DialogSpeechToText)
        self.label_key.setEnabled(False)
        self.label_key.setGeometry(QtCore.QRect(30, 287, 291, 20))
        self.label_key.setObjectName("label_key")
        self.lineEdit_key = QtWidgets.QLineEdit(DialogSpeechToText)
        self.lineEdit_key.setEnabled(False)
        self.lineEdit_key.setGeometry(QtCore.QRect(20, 310, 681, 25))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.progressBar = QtWidgets.QProgressBar(DialogSpeechToText)
        self.progressBar.setGeometry(QtCore.QRect(64, 385, 411, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_start = QtWidgets.QPushButton(DialogSpeechToText)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 380, 32, 32))
        self.pushButton_start.setText("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_2 = QtWidgets.QLabel(DialogSpeechToText)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_chunksize = QtWidgets.QComboBox(DialogSpeechToText)
        self.comboBox_chunksize.setGeometry(QtCore.QRect(30, 100, 141, 25))
        self.comboBox_chunksize.setObjectName("comboBox_chunksize")
        self.comboBox_chunksize.addItem("")
        self.comboBox_chunksize.addItem("")
        self.label_process = QtWidgets.QLabel(DialogSpeechToText)
        self.label_process.setGeometry(QtCore.QRect(20, 350, 661, 17))
        self.label_process.setObjectName("label_process")

        self.retranslateUi(DialogSpeechToText)
        self.buttonBox.accepted.connect(DialogSpeechToText.accept)
        self.buttonBox.rejected.connect(DialogSpeechToText.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSpeechToText)

    def retranslateUi(self, DialogSpeechToText):
        _translate = QtCore.QCoreApplication.translate
        DialogSpeechToText.setWindowTitle(_translate("DialogSpeechToText", "Speech to text"))
        self.comboBox_service.setItemText(0, _translate("DialogSpeechToText", "Google"))
        self.comboBox_service.setItemText(1, _translate("DialogSpeechToText", "Microsoft Bing Voice Recognition"))
        self.comboBox_service.setItemText(2, _translate("DialogSpeechToText", "Wit.ai"))
        self.comboBox_service.setItemText(3, _translate("DialogSpeechToText", "Houndify"))
        self.comboBox_service.setItemText(4, _translate("DialogSpeechToText", "IBM Speech"))
        self.label_service.setText(_translate("DialogSpeechToText", "Select online speech to text service"))
        self.label_ffmpeg_info.setText(_translate("DialogSpeechToText", "Speech to text requires installed software: ffmpeg"))
        self.label_language.setToolTip(_translate("DialogSpeechToText", "Please select language in the format prefered by the service.\n"
" IBM an RFC5646 language tag\n"
" Bing BCP-47 language tag\n"
" Google IETF language tag\n"
"\n"
"Examples:\n"
"en-US \n"
"en-UK \n"
"en-AU"))
        self.label_language.setText(_translate("DialogSpeechToText", "Language"))
        self.lineEdit_language.setToolTip(_translate("DialogSpeechToText", "Please select language in the format prefered by the service.\n"
" IBM an RFC5646 language tag\n"
" Bing BCP-47 language tag\n"
" Google IETF language tag\n"
"\n"
"Examples:\n"
"en-US \n"
"en-UK \n"
"en-AU"))
        self.label_id.setText(_translate("DialogSpeechToText", "Service ID or username"))
        self.label_key.setText(_translate("DialogSpeechToText", "Service key or password"))
        self.pushButton_start.setToolTip(_translate("DialogSpeechToText", "Start speech to text conversion"))
        self.label_2.setToolTip(_translate("DialogSpeechToText", "Convert sections of the A/V file  insmall chunks of 30 or 60 seconds."))
        self.label_2.setText(_translate("DialogSpeechToText", "Chunk size"))
        self.comboBox_chunksize.setItemText(0, _translate("DialogSpeechToText", "60 seconds"))
        self.comboBox_chunksize.setItemText(1, _translate("DialogSpeechToText", "30 seconds"))
        self.label_process.setText(_translate("DialogSpeechToText", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSpeechToText = QtWidgets.QDialog()
    ui = Ui_DialogSpeechToText()
    ui.setupUi(DialogSpeechToText)
    DialogSpeechToText.show()
    sys.exit(app.exec_())
