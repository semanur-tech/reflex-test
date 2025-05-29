# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"")
        self.labelInfo = QLabel(Widget)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setGeometry(QRect(40, 160, 381, 91))
        font = QFont()
        font.setFamilies([u"Showcard Gothic"])
        self.labelInfo.setFont(font)
        self.btnStart = QPushButton(Widget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(240, 340, 221, 81))
        self.btnStart.setFont(font)
        self.labelResult = QLabel(Widget)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setGeometry(QRect(450, 170, 291, 81))
        self.labelResult.setFont(font)
        self.btnRetry = QPushButton(Widget)
        self.btnRetry.setObjectName(u"btnRetry")
        self.btnRetry.setGeometry(QRect(290, 460, 121, 31))
        self.btnRetry.setFont(font)
        self.labelDot = QLabel(Widget)
        self.labelDot.setObjectName(u"labelDot")
        self.labelDot.setGeometry(QRect(130, 99, 461, 431))
        self.lineEditName = QLineEdit(Widget)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(350, 280, 291, 31))
        self.lineEditName.setFont(font)
        self.labelNameInfo = QLabel(Widget)
        self.labelNameInfo.setObjectName(u"labelNameInfo")
        self.labelNameInfo.setGeometry(QRect(80, 240, 211, 101))
        self.labelNameInfo.setFont(font)
        self.labelLog = QLabel(Widget)
        self.labelLog.setObjectName(u"labelLog")
        self.labelLog.setGeometry(QRect(600, 340, 171, 201))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.labelInfo.setText(QCoreApplication.translate("Widget", u"          \"Haz\u0131r  oldugunda  Basla'ya  bas !\"", None))
        self.btnStart.setText(QCoreApplication.translate("Widget", u"\"Basla\"", None))
        self.labelResult.setText(QCoreApplication.translate("Widget", u"        \"Time : \" ", None))
        self.btnRetry.setText(QCoreApplication.translate("Widget", u"\"Yeniden Dene \"", None))
        self.labelDot.setText(QCoreApplication.translate("Widget", u"\"  \"", None))
        self.lineEditName.setText("")
        self.labelNameInfo.setText(QCoreApplication.translate("Widget", u"\"kullan\u0131c\u0131 ad\u0131n\u0131z\u0131 giriniz : \"", None))
        self.labelLog.setText(QCoreApplication.translate("Widget", u"\" \"", None))
    # retranslateUi

