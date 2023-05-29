# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_infoMainWindow(object):
    def setupUi(self, infoMainWindow):
        if not infoMainWindow.objectName():
            infoMainWindow.setObjectName(u"infoMainWindow")
        infoMainWindow.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(infoMainWindow.sizePolicy().hasHeightForWidth())
        infoMainWindow.setSizePolicy(sizePolicy)
        self.mainWidget = QWidget(infoMainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.mainWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(12)
        self.headerFrame.setFont(font)
        self.headerFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #EDEDE9;\n"
"	color: black;\n"
"}\n"
"QPushButton {\n"
"	border-radius: 6px;\n"
"	background-color: #9a8c98;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #FEFAE0;\n"
"	color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #22333B;\n"
"	color: #EAE0D5\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.headerLbl = QLabel(self.headerFrame)
        self.headerLbl.setObjectName(u"headerLbl")
        font1 = QFont()
        font1.setFamilies([u"Raleway"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.headerLbl.setFont(font1)
        self.headerLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.headerLbl.setWordWrap(False)

        self.horizontalLayout.addWidget(self.headerLbl)

        self.homeBtn = QPushButton(self.headerFrame)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy1.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Raleway"])
        font2.setPointSize(12)
        self.homeBtn.setFont(font2)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.homeBtn)

        self.cpuBtn = QPushButton(self.headerFrame)
        self.cpuBtn.setObjectName(u"cpuBtn")
        sizePolicy1.setHeightForWidth(self.cpuBtn.sizePolicy().hasHeightForWidth())
        self.cpuBtn.setSizePolicy(sizePolicy1)
        self.cpuBtn.setFont(font2)
        self.cpuBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cpuBtn)

        self.gpuBtn = QPushButton(self.headerFrame)
        self.gpuBtn.setObjectName(u"gpuBtn")
        sizePolicy1.setHeightForWidth(self.gpuBtn.sizePolicy().hasHeightForWidth())
        self.gpuBtn.setSizePolicy(sizePolicy1)
        self.gpuBtn.setFont(font2)
        self.gpuBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.gpuBtn)

        self.memBtn = QPushButton(self.headerFrame)
        self.memBtn.setObjectName(u"memBtn")
        sizePolicy1.setHeightForWidth(self.memBtn.sizePolicy().hasHeightForWidth())
        self.memBtn.setSizePolicy(sizePolicy1)
        self.memBtn.setFont(font2)
        self.memBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.memBtn)


        self.verticalLayout.addWidget(self.headerFrame)

        self.infoFrame = QFrame(self.mainWidget)
        self.infoFrame.setObjectName(u"infoFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Raleway"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.infoFrame.setFont(font3)
        self.infoFrame.setStyleSheet(u"QFrame, QWidget {\n"
"	background-color: #4a4e69;\n"
"	color: white;\n"
"}")
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.infoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoWidget = QStackedWidget(self.infoFrame)
        self.infoWidget.setObjectName(u"infoWidget")
        self.systemPage = QWidget()
        self.systemPage.setObjectName(u"systemPage")
        self.verticalLayout_3 = QVBoxLayout(self.systemPage)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.systemMainFrame = QFrame(self.systemPage)
        self.systemMainFrame.setObjectName(u"systemMainFrame")
        self.systemMainFrame.setFrameShape(QFrame.NoFrame)
        self.systemMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.systemMainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.systemHeaderFrame = QFrame(self.systemMainFrame)
        self.systemHeaderFrame.setObjectName(u"systemHeaderFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.systemHeaderFrame.sizePolicy().hasHeightForWidth())
        self.systemHeaderFrame.setSizePolicy(sizePolicy3)
        self.systemHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.systemHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.systemHeaderFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.systemHeadingLbl = QLabel(self.systemHeaderFrame)
        self.systemHeadingLbl.setObjectName(u"systemHeadingLbl")
        sizePolicy3.setHeightForWidth(self.systemHeadingLbl.sizePolicy().hasHeightForWidth())
        self.systemHeadingLbl.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Raleway"])
        font4.setPointSize(28)
        font4.setBold(True)
        self.systemHeadingLbl.setFont(font4)

        self.horizontalLayout_2.addWidget(self.systemHeadingLbl)

        self.computerNameLbl = QLabel(self.systemHeaderFrame)
        self.computerNameLbl.setObjectName(u"computerNameLbl")
        sizePolicy1.setHeightForWidth(self.computerNameLbl.sizePolicy().hasHeightForWidth())
        self.computerNameLbl.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Raleway"])
        font5.setPointSize(24)
        self.computerNameLbl.setFont(font5)
        self.computerNameLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.computerNameLbl)


        self.verticalLayout_4.addWidget(self.systemHeaderFrame)

        self.systemInfoFrame = QFrame(self.systemMainFrame)
        self.systemInfoFrame.setObjectName(u"systemInfoFrame")
        sizePolicy.setHeightForWidth(self.systemInfoFrame.sizePolicy().hasHeightForWidth())
        self.systemInfoFrame.setSizePolicy(sizePolicy)
        self.systemInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #22223b;\n"
"	border-radius: 12px;\n"
"}")
        self.systemInfoFrame.setFrameShape(QFrame.NoFrame)
        self.systemInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.systemInfoFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dateTimeLbl = QLabel(self.systemInfoFrame)
        self.dateTimeLbl.setObjectName(u"dateTimeLbl")
        font6 = QFont()
        font6.setFamilies([u"Raleway"])
        font6.setPointSize(16)
        self.dateTimeLbl.setFont(font6)

        self.verticalLayout_5.addWidget(self.dateTimeLbl)

        self.osLbl = QLabel(self.systemInfoFrame)
        self.osLbl.setObjectName(u"osLbl")
        self.osLbl.setFont(font6)

        self.verticalLayout_5.addWidget(self.osLbl)

        self.langLbl = QLabel(self.systemInfoFrame)
        self.langLbl.setObjectName(u"langLbl")
        self.langLbl.setFont(font6)

        self.verticalLayout_5.addWidget(self.langLbl)

        self.sysModelLbl = QLabel(self.systemInfoFrame)
        self.sysModelLbl.setObjectName(u"sysModelLbl")
        self.sysModelLbl.setFont(font6)

        self.verticalLayout_5.addWidget(self.sysModelLbl)

        self.biosLbl = QLabel(self.systemInfoFrame)
        self.biosLbl.setObjectName(u"biosLbl")
        self.biosLbl.setFont(font6)

        self.verticalLayout_5.addWidget(self.biosLbl)


        self.verticalLayout_4.addWidget(self.systemInfoFrame)


        self.verticalLayout_3.addWidget(self.systemMainFrame)

        self.infoWidget.addWidget(self.systemPage)
        self.cpuPage = QWidget()
        self.cpuPage.setObjectName(u"cpuPage")
        self.verticalLayout_9 = QVBoxLayout(self.cpuPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cpuMainFrame = QFrame(self.cpuPage)
        self.cpuMainFrame.setObjectName(u"cpuMainFrame")
        self.cpuMainFrame.setFrameShape(QFrame.NoFrame)
        self.cpuMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.cpuMainFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cpuHeaderFrame = QFrame(self.cpuMainFrame)
        self.cpuHeaderFrame.setObjectName(u"cpuHeaderFrame")
        self.cpuHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.cpuHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.cpuHeaderFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cpuHeadingLbl = QLabel(self.cpuHeaderFrame)
        self.cpuHeadingLbl.setObjectName(u"cpuHeadingLbl")
        sizePolicy3.setHeightForWidth(self.cpuHeadingLbl.sizePolicy().hasHeightForWidth())
        self.cpuHeadingLbl.setSizePolicy(sizePolicy3)
        self.cpuHeadingLbl.setFont(font4)

        self.horizontalLayout_4.addWidget(self.cpuHeadingLbl)

        self.cpuInfoHeadingLbl = QLabel(self.cpuHeaderFrame)
        self.cpuInfoHeadingLbl.setObjectName(u"cpuInfoHeadingLbl")
        sizePolicy1.setHeightForWidth(self.cpuInfoHeadingLbl.sizePolicy().hasHeightForWidth())
        self.cpuInfoHeadingLbl.setSizePolicy(sizePolicy1)
        self.cpuInfoHeadingLbl.setFont(font5)
        self.cpuInfoHeadingLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.cpuInfoHeadingLbl)


        self.verticalLayout_10.addWidget(self.cpuHeaderFrame)

        self.cpuInfoFrame = QFrame(self.cpuMainFrame)
        self.cpuInfoFrame.setObjectName(u"cpuInfoFrame")
        sizePolicy.setHeightForWidth(self.cpuInfoFrame.sizePolicy().hasHeightForWidth())
        self.cpuInfoFrame.setSizePolicy(sizePolicy)
        self.cpuInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #22223b;\n"
"	border-radius: 12px;\n"
"}")
        self.cpuInfoFrame.setFrameShape(QFrame.NoFrame)
        self.cpuInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.cpuInfoFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.cpuNumsLbl = QLabel(self.cpuInfoFrame)
        self.cpuNumsLbl.setObjectName(u"cpuNumsLbl")
        self.cpuNumsLbl.setFont(font6)

        self.verticalLayout_11.addWidget(self.cpuNumsLbl)

        self.cpuManufacturerLbl = QLabel(self.cpuInfoFrame)
        self.cpuManufacturerLbl.setObjectName(u"cpuManufacturerLbl")
        self.cpuManufacturerLbl.setFont(font6)

        self.verticalLayout_11.addWidget(self.cpuManufacturerLbl)

        self.cpuArchLbl = QLabel(self.cpuInfoFrame)
        self.cpuArchLbl.setObjectName(u"cpuArchLbl")
        self.cpuArchLbl.setFont(font6)

        self.verticalLayout_11.addWidget(self.cpuArchLbl)

        self.cpuMinHzLbl = QLabel(self.cpuInfoFrame)
        self.cpuMinHzLbl.setObjectName(u"cpuMinHzLbl")
        self.cpuMinHzLbl.setFont(font6)

        self.verticalLayout_11.addWidget(self.cpuMinHzLbl)

        self.cpuMaxHzLbl = QLabel(self.cpuInfoFrame)
        self.cpuMaxHzLbl.setObjectName(u"cpuMaxHzLbl")
        self.cpuMaxHzLbl.setFont(font6)

        self.verticalLayout_11.addWidget(self.cpuMaxHzLbl)


        self.verticalLayout_10.addWidget(self.cpuInfoFrame)

        self.cpuFlagsHeaderFrame = QFrame(self.cpuMainFrame)
        self.cpuFlagsHeaderFrame.setObjectName(u"cpuFlagsHeaderFrame")
        self.cpuFlagsHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.cpuFlagsHeaderFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.cpuFlagsHeaderFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cpuFlagsHeadingLbl = QLabel(self.cpuFlagsHeaderFrame)
        self.cpuFlagsHeadingLbl.setObjectName(u"cpuFlagsHeadingLbl")
        self.cpuFlagsHeadingLbl.setFont(font4)

        self.verticalLayout_12.addWidget(self.cpuFlagsHeadingLbl)


        self.verticalLayout_10.addWidget(self.cpuFlagsHeaderFrame)

        self.cpuFlagsInfoFrame = QFrame(self.cpuMainFrame)
        self.cpuFlagsInfoFrame.setObjectName(u"cpuFlagsInfoFrame")
        sizePolicy.setHeightForWidth(self.cpuFlagsInfoFrame.sizePolicy().hasHeightForWidth())
        self.cpuFlagsInfoFrame.setSizePolicy(sizePolicy)
        self.cpuFlagsInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #22223b;\n"
"	border-radius: 12px;\n"
"}\n"
"QCheckBox {\n"
"	padding: 4px 4px 4px 4px;\n"
"	border-radius: 6px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 12px;\n"
"}")
        self.cpuFlagsInfoFrame.setFrameShape(QFrame.NoFrame)
        self.cpuFlagsInfoFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.cpuFlagsInfoFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.intelFlagsFrame = QFrame(self.cpuFlagsInfoFrame)
        self.intelFlagsFrame.setObjectName(u"intelFlagsFrame")
        self.intelFlagsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #006EC3;\n"
"	color: white;\n"
"}")
        self.intelFlagsFrame.setFrameShape(QFrame.NoFrame)
        self.intelFlagsFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.intelFlagsFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.intelHeaderFrame = QFrame(self.intelFlagsFrame)
        self.intelHeaderFrame.setObjectName(u"intelHeaderFrame")
        self.intelHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.intelHeaderFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.intelHeaderFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.intelHeadingLbl = QLabel(self.intelHeaderFrame)
        self.intelHeadingLbl.setObjectName(u"intelHeadingLbl")
        sizePolicy3.setHeightForWidth(self.intelHeadingLbl.sizePolicy().hasHeightForWidth())
        self.intelHeadingLbl.setSizePolicy(sizePolicy3)
        self.intelHeadingLbl.setFont(font4)

        self.verticalLayout_14.addWidget(self.intelHeadingLbl)


        self.verticalLayout_13.addWidget(self.intelHeaderFrame)

        self.intelInfoFrame = QFrame(self.intelFlagsFrame)
        self.intelInfoFrame.setObjectName(u"intelInfoFrame")
        sizePolicy.setHeightForWidth(self.intelInfoFrame.sizePolicy().hasHeightForWidth())
        self.intelInfoFrame.setSizePolicy(sizePolicy)
        self.intelInfoFrame.setStyleSheet(u"")
        self.intelInfoFrame.setFrameShape(QFrame.NoFrame)
        self.intelInfoFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.intelInfoFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lmCheck = QCheckBox(self.intelInfoFrame)
        self.lmCheck.setObjectName(u"lmCheck")
        sizePolicy1.setHeightForWidth(self.lmCheck.sizePolicy().hasHeightForWidth())
        self.lmCheck.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Raleway"])
        font7.setPointSize(8)
        self.lmCheck.setFont(font7)
        self.lmCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.lmCheck.setCheckable(True)
        self.lmCheck.setChecked(False)

        self.gridLayout.addWidget(self.lmCheck, 3, 0, 1, 1)

        self.vmxCheck = QCheckBox(self.intelInfoFrame)
        self.vmxCheck.setObjectName(u"vmxCheck")
        sizePolicy1.setHeightForWidth(self.vmxCheck.sizePolicy().hasHeightForWidth())
        self.vmxCheck.setSizePolicy(sizePolicy1)
        self.vmxCheck.setFont(font7)
        self.vmxCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.vmxCheck.setCheckable(True)
        self.vmxCheck.setChecked(False)

        self.gridLayout.addWidget(self.vmxCheck, 4, 0, 1, 1)

        self.smxCheck = QCheckBox(self.intelInfoFrame)
        self.smxCheck.setObjectName(u"smxCheck")
        sizePolicy1.setHeightForWidth(self.smxCheck.sizePolicy().hasHeightForWidth())
        self.smxCheck.setSizePolicy(sizePolicy1)
        self.smxCheck.setFont(font7)
        self.smxCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.smxCheck.setCheckable(True)
        self.smxCheck.setChecked(False)

        self.gridLayout.addWidget(self.smxCheck, 0, 1, 1, 1)

        self.sse3Check = QCheckBox(self.intelInfoFrame)
        self.sse3Check.setObjectName(u"sse3Check")
        sizePolicy1.setHeightForWidth(self.sse3Check.sizePolicy().hasHeightForWidth())
        self.sse3Check.setSizePolicy(sizePolicy1)
        self.sse3Check.setFont(font7)
        self.sse3Check.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sse3Check.setCheckable(True)
        self.sse3Check.setChecked(False)

        self.gridLayout.addWidget(self.sse3Check, 2, 2, 1, 1)

        self.pnCheck = QCheckBox(self.intelInfoFrame)
        self.pnCheck.setObjectName(u"pnCheck")
        sizePolicy1.setHeightForWidth(self.pnCheck.sizePolicy().hasHeightForWidth())
        self.pnCheck.setSizePolicy(sizePolicy1)
        self.pnCheck.setFont(font7)
        self.pnCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pnCheck.setCheckable(True)
        self.pnCheck.setChecked(False)

        self.gridLayout.addWidget(self.pnCheck, 4, 2, 1, 1)

        self.paeCheck = QCheckBox(self.intelInfoFrame)
        self.paeCheck.setObjectName(u"paeCheck")
        sizePolicy1.setHeightForWidth(self.paeCheck.sizePolicy().hasHeightForWidth())
        self.paeCheck.setSizePolicy(sizePolicy1)
        self.paeCheck.setFont(font7)
        self.paeCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.paeCheck.setCheckable(True)
        self.paeCheck.setChecked(False)

        self.gridLayout.addWidget(self.paeCheck, 3, 2, 1, 1)

        self.htCheck = QCheckBox(self.intelInfoFrame)
        self.htCheck.setObjectName(u"htCheck")
        sizePolicy1.setHeightForWidth(self.htCheck.sizePolicy().hasHeightForWidth())
        self.htCheck.setSizePolicy(sizePolicy1)
        self.htCheck.setFont(font7)
        self.htCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.htCheck.setCheckable(True)
        self.htCheck.setChecked(False)

        self.gridLayout.addWidget(self.htCheck, 4, 1, 1, 1)

        self.acpiCheck = QCheckBox(self.intelInfoFrame)
        self.acpiCheck.setObjectName(u"acpiCheck")
        sizePolicy1.setHeightForWidth(self.acpiCheck.sizePolicy().hasHeightForWidth())
        self.acpiCheck.setSizePolicy(sizePolicy1)
        self.acpiCheck.setFont(font7)
        self.acpiCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.acpiCheck.setCheckable(True)
        self.acpiCheck.setChecked(False)

        self.gridLayout.addWidget(self.acpiCheck, 0, 2, 1, 1)

        self.sseCheck = QCheckBox(self.intelInfoFrame)
        self.sseCheck.setObjectName(u"sseCheck")
        sizePolicy1.setHeightForWidth(self.sseCheck.sizePolicy().hasHeightForWidth())
        self.sseCheck.setSizePolicy(sizePolicy1)
        self.sseCheck.setFont(font7)
        self.sseCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sseCheck.setCheckable(True)
        self.sseCheck.setChecked(False)

        self.gridLayout.addWidget(self.sseCheck, 2, 0, 1, 1)

        self.sse2Check = QCheckBox(self.intelInfoFrame)
        self.sse2Check.setObjectName(u"sse2Check")
        sizePolicy1.setHeightForWidth(self.sse2Check.sizePolicy().hasHeightForWidth())
        self.sse2Check.setSizePolicy(sizePolicy1)
        self.sse2Check.setFont(font7)
        self.sse2Check.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sse2Check.setCheckable(True)
        self.sse2Check.setChecked(False)

        self.gridLayout.addWidget(self.sse2Check, 2, 1, 1, 1)

        self.hypervisorCheck = QCheckBox(self.intelInfoFrame)
        self.hypervisorCheck.setObjectName(u"hypervisorCheck")
        sizePolicy1.setHeightForWidth(self.hypervisorCheck.sizePolicy().hasHeightForWidth())
        self.hypervisorCheck.setSizePolicy(sizePolicy1)
        self.hypervisorCheck.setFont(font7)
        self.hypervisorCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.hypervisorCheck.setCheckable(True)
        self.hypervisorCheck.setChecked(False)

        self.gridLayout.addWidget(self.hypervisorCheck, 1, 0, 1, 1)

        self.pdcmCheck = QCheckBox(self.intelInfoFrame)
        self.pdcmCheck.setObjectName(u"pdcmCheck")
        sizePolicy1.setHeightForWidth(self.pdcmCheck.sizePolicy().hasHeightForWidth())
        self.pdcmCheck.setSizePolicy(sizePolicy1)
        self.pdcmCheck.setFont(font7)
        self.pdcmCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pdcmCheck.setCheckable(True)
        self.pdcmCheck.setChecked(False)

        self.gridLayout.addWidget(self.pdcmCheck, 3, 1, 1, 1)

        self.tmCheck = QCheckBox(self.intelInfoFrame)
        self.tmCheck.setObjectName(u"tmCheck")
        sizePolicy1.setHeightForWidth(self.tmCheck.sizePolicy().hasHeightForWidth())
        self.tmCheck.setSizePolicy(sizePolicy1)
        self.tmCheck.setFont(font7)
        self.tmCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.tmCheck.setCheckable(True)
        self.tmCheck.setChecked(False)

        self.gridLayout.addWidget(self.tmCheck, 0, 0, 1, 1)

        self.sse4_1Check = QCheckBox(self.intelInfoFrame)
        self.sse4_1Check.setObjectName(u"sse4_1Check")
        sizePolicy1.setHeightForWidth(self.sse4_1Check.sizePolicy().hasHeightForWidth())
        self.sse4_1Check.setSizePolicy(sizePolicy1)
        self.sse4_1Check.setFont(font7)
        self.sse4_1Check.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sse4_1Check.setCheckable(True)
        self.sse4_1Check.setChecked(False)

        self.gridLayout.addWidget(self.sse4_1Check, 1, 2, 1, 1)

        self.sse4_2Check = QCheckBox(self.intelInfoFrame)
        self.sse4_2Check.setObjectName(u"sse4_2Check")
        sizePolicy1.setHeightForWidth(self.sse4_2Check.sizePolicy().hasHeightForWidth())
        self.sse4_2Check.setSizePolicy(sizePolicy1)
        self.sse4_2Check.setFont(font7)
        self.sse4_2Check.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sse4_2Check.setCheckable(True)
        self.sse4_2Check.setChecked(False)

        self.gridLayout.addWidget(self.sse4_2Check, 1, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.intelInfoFrame)


        self.horizontalLayout_5.addWidget(self.intelFlagsFrame)

        self.amdFlagsFrame = QFrame(self.cpuFlagsInfoFrame)
        self.amdFlagsFrame.setObjectName(u"amdFlagsFrame")
        self.amdFlagsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(214,8,49);\n"
"	color: white;\n"
"}")
        self.amdFlagsFrame.setFrameShape(QFrame.NoFrame)
        self.amdFlagsFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.amdFlagsFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.amdHeaderFrame = QFrame(self.amdFlagsFrame)
        self.amdHeaderFrame.setObjectName(u"amdHeaderFrame")
        self.amdHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.amdHeaderFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_16 = QVBoxLayout(self.amdHeaderFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.amdHeadingLbl = QLabel(self.amdHeaderFrame)
        self.amdHeadingLbl.setObjectName(u"amdHeadingLbl")
        sizePolicy3.setHeightForWidth(self.amdHeadingLbl.sizePolicy().hasHeightForWidth())
        self.amdHeadingLbl.setSizePolicy(sizePolicy3)
        self.amdHeadingLbl.setFont(font4)

        self.verticalLayout_16.addWidget(self.amdHeadingLbl)


        self.verticalLayout_15.addWidget(self.amdHeaderFrame)

        self.amdInfoFrame = QFrame(self.amdFlagsFrame)
        self.amdInfoFrame.setObjectName(u"amdInfoFrame")
        sizePolicy.setHeightForWidth(self.amdInfoFrame.sizePolicy().hasHeightForWidth())
        self.amdInfoFrame.setSizePolicy(sizePolicy)
        self.amdInfoFrame.setFrameShape(QFrame.NoFrame)
        self.amdInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.amdInfoFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.svmCheck = QCheckBox(self.amdInfoFrame)
        self.svmCheck.setObjectName(u"svmCheck")
        sizePolicy1.setHeightForWidth(self.svmCheck.sizePolicy().hasHeightForWidth())
        self.svmCheck.setSizePolicy(sizePolicy1)
        self.svmCheck.setFont(font7)
        self.svmCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.svmCheck.setCheckable(True)
        self.svmCheck.setChecked(False)

        self.verticalLayout_19.addWidget(self.svmCheck)

        self.sse4aCheck = QCheckBox(self.amdInfoFrame)
        self.sse4aCheck.setObjectName(u"sse4aCheck")
        sizePolicy1.setHeightForWidth(self.sse4aCheck.sizePolicy().hasHeightForWidth())
        self.sse4aCheck.setSizePolicy(sizePolicy1)
        self.sse4aCheck.setFont(font7)
        self.sse4aCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.sse4aCheck.setCheckable(True)
        self.sse4aCheck.setChecked(False)

        self.verticalLayout_19.addWidget(self.sse4aCheck)

        self.mpCheck = QCheckBox(self.amdInfoFrame)
        self.mpCheck.setObjectName(u"mpCheck")
        sizePolicy1.setHeightForWidth(self.mpCheck.sizePolicy().hasHeightForWidth())
        self.mpCheck.setSizePolicy(sizePolicy1)
        self.mpCheck.setFont(font7)
        self.mpCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.mpCheck.setCheckable(True)
        self.mpCheck.setChecked(False)

        self.verticalLayout_19.addWidget(self.mpCheck)

        self.amdLMCheck = QCheckBox(self.amdInfoFrame)
        self.amdLMCheck.setObjectName(u"amdLMCheck")
        sizePolicy1.setHeightForWidth(self.amdLMCheck.sizePolicy().hasHeightForWidth())
        self.amdLMCheck.setSizePolicy(sizePolicy1)
        self.amdLMCheck.setFont(font7)
        self.amdLMCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.amdLMCheck.setCheckable(True)
        self.amdLMCheck.setChecked(False)

        self.verticalLayout_19.addWidget(self.amdLMCheck)

        self.abmCheck = QCheckBox(self.amdInfoFrame)
        self.abmCheck.setObjectName(u"abmCheck")
        sizePolicy1.setHeightForWidth(self.abmCheck.sizePolicy().hasHeightForWidth())
        self.abmCheck.setSizePolicy(sizePolicy1)
        self.abmCheck.setFont(font7)
        self.abmCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.abmCheck.setCheckable(True)
        self.abmCheck.setChecked(False)

        self.verticalLayout_19.addWidget(self.abmCheck)


        self.verticalLayout_15.addWidget(self.amdInfoFrame)


        self.horizontalLayout_5.addWidget(self.amdFlagsFrame)

        self.armFlagsFrame = QFrame(self.cpuFlagsInfoFrame)
        self.armFlagsFrame.setObjectName(u"armFlagsFrame")
        self.armFlagsFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #008BB9;\n"
"	color: white;\n"
"}")
        self.armFlagsFrame.setFrameShape(QFrame.NoFrame)
        self.armFlagsFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.armFlagsFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.armHeaderFrame = QFrame(self.armFlagsFrame)
        self.armHeaderFrame.setObjectName(u"armHeaderFrame")
        self.armHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.armHeaderFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_18 = QVBoxLayout(self.armHeaderFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.armHeadingLbl = QLabel(self.armHeaderFrame)
        self.armHeadingLbl.setObjectName(u"armHeadingLbl")
        sizePolicy3.setHeightForWidth(self.armHeadingLbl.sizePolicy().hasHeightForWidth())
        self.armHeadingLbl.setSizePolicy(sizePolicy3)
        self.armHeadingLbl.setFont(font4)

        self.verticalLayout_18.addWidget(self.armHeadingLbl)


        self.verticalLayout_17.addWidget(self.armHeaderFrame)

        self.armInfoFrame = QFrame(self.armFlagsFrame)
        self.armInfoFrame.setObjectName(u"armInfoFrame")
        sizePolicy.setHeightForWidth(self.armInfoFrame.sizePolicy().hasHeightForWidth())
        self.armInfoFrame.setSizePolicy(sizePolicy)
        self.armInfoFrame.setFrameShape(QFrame.NoFrame)
        self.armInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_20 = QVBoxLayout(self.armInfoFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.twoSixBitCheck = QCheckBox(self.armInfoFrame)
        self.twoSixBitCheck.setObjectName(u"twoSixBitCheck")
        sizePolicy1.setHeightForWidth(self.twoSixBitCheck.sizePolicy().hasHeightForWidth())
        self.twoSixBitCheck.setSizePolicy(sizePolicy1)
        self.twoSixBitCheck.setFont(font7)
        self.twoSixBitCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.twoSixBitCheck.setCheckable(True)
        self.twoSixBitCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.twoSixBitCheck)

        self.javaCheck = QCheckBox(self.armInfoFrame)
        self.javaCheck.setObjectName(u"javaCheck")
        sizePolicy1.setHeightForWidth(self.javaCheck.sizePolicy().hasHeightForWidth())
        self.javaCheck.setSizePolicy(sizePolicy1)
        self.javaCheck.setFont(font7)
        self.javaCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.javaCheck.setCheckable(True)
        self.javaCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.javaCheck)

        self.lpaeCheck = QCheckBox(self.armInfoFrame)
        self.lpaeCheck.setObjectName(u"lpaeCheck")
        sizePolicy1.setHeightForWidth(self.lpaeCheck.sizePolicy().hasHeightForWidth())
        self.lpaeCheck.setSizePolicy(sizePolicy1)
        self.lpaeCheck.setFont(font7)
        self.lpaeCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.lpaeCheck.setCheckable(True)
        self.lpaeCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.lpaeCheck)

        self.thumbCheck = QCheckBox(self.armInfoFrame)
        self.thumbCheck.setObjectName(u"thumbCheck")
        sizePolicy1.setHeightForWidth(self.thumbCheck.sizePolicy().hasHeightForWidth())
        self.thumbCheck.setSizePolicy(sizePolicy1)
        self.thumbCheck.setFont(font7)
        self.thumbCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.thumbCheck.setCheckable(True)
        self.thumbCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.thumbCheck)

        self.neonCheck = QCheckBox(self.armInfoFrame)
        self.neonCheck.setObjectName(u"neonCheck")
        sizePolicy1.setHeightForWidth(self.neonCheck.sizePolicy().hasHeightForWidth())
        self.neonCheck.setSizePolicy(sizePolicy1)
        self.neonCheck.setFont(font7)
        self.neonCheck.setCursor(QCursor(Qt.ForbiddenCursor))
        self.neonCheck.setCheckable(True)
        self.neonCheck.setChecked(False)

        self.verticalLayout_20.addWidget(self.neonCheck)


        self.verticalLayout_17.addWidget(self.armInfoFrame)


        self.horizontalLayout_5.addWidget(self.armFlagsFrame)


        self.verticalLayout_10.addWidget(self.cpuFlagsInfoFrame)


        self.verticalLayout_9.addWidget(self.cpuMainFrame)

        self.infoWidget.addWidget(self.cpuPage)
        self.displayPage = QWidget()
        self.displayPage.setObjectName(u"displayPage")
        self.verticalLayout_6 = QVBoxLayout(self.displayPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.displayMainFrame = QFrame(self.displayPage)
        self.displayMainFrame.setObjectName(u"displayMainFrame")
        self.displayMainFrame.setFrameShape(QFrame.NoFrame)
        self.displayMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.displayMainFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayHeaderFrame = QFrame(self.displayMainFrame)
        self.displayHeaderFrame.setObjectName(u"displayHeaderFrame")
        self.displayHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.displayHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.displayHeaderFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gpuHeadingLbl = QLabel(self.displayHeaderFrame)
        self.gpuHeadingLbl.setObjectName(u"gpuHeadingLbl")
        sizePolicy3.setHeightForWidth(self.gpuHeadingLbl.sizePolicy().hasHeightForWidth())
        self.gpuHeadingLbl.setSizePolicy(sizePolicy3)
        self.gpuHeadingLbl.setFont(font4)

        self.horizontalLayout_3.addWidget(self.gpuHeadingLbl)

        self.gpuInfoHeadingLbl = QLabel(self.displayHeaderFrame)
        self.gpuInfoHeadingLbl.setObjectName(u"gpuInfoHeadingLbl")
        sizePolicy1.setHeightForWidth(self.gpuInfoHeadingLbl.sizePolicy().hasHeightForWidth())
        self.gpuInfoHeadingLbl.setSizePolicy(sizePolicy1)
        self.gpuInfoHeadingLbl.setFont(font5)
        self.gpuInfoHeadingLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.gpuInfoHeadingLbl)


        self.verticalLayout_7.addWidget(self.displayHeaderFrame)

        self.displayInfoFrame = QFrame(self.displayMainFrame)
        self.displayInfoFrame.setObjectName(u"displayInfoFrame")
        sizePolicy.setHeightForWidth(self.displayInfoFrame.sizePolicy().hasHeightForWidth())
        self.displayInfoFrame.setSizePolicy(sizePolicy)
        self.displayInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #22223b;\n"
"	border-radius: 12px;\n"
"}")
        self.displayInfoFrame.setFrameShape(QFrame.NoFrame)
        self.displayInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.displayInfoFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gpuNameLbl = QLabel(self.displayInfoFrame)
        self.gpuNameLbl.setObjectName(u"gpuNameLbl")
        self.gpuNameLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuNameLbl)

        self.gpuDriverVerLbl = QLabel(self.displayInfoFrame)
        self.gpuDriverVerLbl.setObjectName(u"gpuDriverVerLbl")
        self.gpuDriverVerLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuDriverVerLbl)

        self.gpuProcessorLbl = QLabel(self.displayInfoFrame)
        self.gpuProcessorLbl.setObjectName(u"gpuProcessorLbl")
        self.gpuProcessorLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuProcessorLbl)

        self.gpuDACLbl = QLabel(self.displayInfoFrame)
        self.gpuDACLbl.setObjectName(u"gpuDACLbl")
        self.gpuDACLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuDACLbl)

        self.gpuCompatLbl = QLabel(self.displayInfoFrame)
        self.gpuCompatLbl.setObjectName(u"gpuCompatLbl")
        self.gpuCompatLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuCompatLbl)

        self.gpuMinHzLbl = QLabel(self.displayInfoFrame)
        self.gpuMinHzLbl.setObjectName(u"gpuMinHzLbl")
        self.gpuMinHzLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuMinHzLbl)

        self.gpuMaxHzLbl = QLabel(self.displayInfoFrame)
        self.gpuMaxHzLbl.setObjectName(u"gpuMaxHzLbl")
        self.gpuMaxHzLbl.setFont(font6)

        self.verticalLayout_8.addWidget(self.gpuMaxHzLbl)


        self.verticalLayout_7.addWidget(self.displayInfoFrame)


        self.verticalLayout_6.addWidget(self.displayMainFrame)

        self.infoWidget.addWidget(self.displayPage)
        self.memoryPage = QWidget()
        self.memoryPage.setObjectName(u"memoryPage")
        self.verticalLayout_21 = QVBoxLayout(self.memoryPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.memoryMainFrame = QFrame(self.memoryPage)
        self.memoryMainFrame.setObjectName(u"memoryMainFrame")
        self.memoryMainFrame.setFrameShape(QFrame.NoFrame)
        self.memoryMainFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.memoryMainFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.memoryHeaderFrame = QFrame(self.memoryMainFrame)
        self.memoryHeaderFrame.setObjectName(u"memoryHeaderFrame")
        self.memoryHeaderFrame.setFrameShape(QFrame.NoFrame)
        self.memoryHeaderFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.memoryHeaderFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.memHeadingLbl = QLabel(self.memoryHeaderFrame)
        self.memHeadingLbl.setObjectName(u"memHeadingLbl")
        sizePolicy3.setHeightForWidth(self.memHeadingLbl.sizePolicy().hasHeightForWidth())
        self.memHeadingLbl.setSizePolicy(sizePolicy3)
        self.memHeadingLbl.setFont(font4)

        self.horizontalLayout_6.addWidget(self.memHeadingLbl)

        self.memHeadingInfoLbl = QLabel(self.memoryHeaderFrame)
        self.memHeadingInfoLbl.setObjectName(u"memHeadingInfoLbl")
        sizePolicy1.setHeightForWidth(self.memHeadingInfoLbl.sizePolicy().hasHeightForWidth())
        self.memHeadingInfoLbl.setSizePolicy(sizePolicy1)
        self.memHeadingInfoLbl.setFont(font5)
        self.memHeadingInfoLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.memHeadingInfoLbl)


        self.verticalLayout_22.addWidget(self.memoryHeaderFrame)

        self.memoryInfoFrame = QFrame(self.memoryMainFrame)
        self.memoryInfoFrame.setObjectName(u"memoryInfoFrame")
        sizePolicy.setHeightForWidth(self.memoryInfoFrame.sizePolicy().hasHeightForWidth())
        self.memoryInfoFrame.setSizePolicy(sizePolicy)
        self.memoryInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #22223b;\n"
"	border-radius: 12px;\n"
"}")
        self.memoryInfoFrame.setFrameShape(QFrame.NoFrame)
        self.memoryInfoFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.memoryInfoFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mem1Frame = QFrame(self.memoryInfoFrame)
        self.mem1Frame.setObjectName(u"mem1Frame")
        self.mem1Frame.setStyleSheet(u"QFrame {\n"
"	background-color: #9a8c98;\n"
"	color: white;\n"
"}")
        self.mem1Frame.setFrameShape(QFrame.NoFrame)
        self.mem1Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_23 = QVBoxLayout(self.mem1Frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.memNameLbl_0 = QLabel(self.mem1Frame)
        self.memNameLbl_0.setObjectName(u"memNameLbl_0")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.memNameLbl_0.sizePolicy().hasHeightForWidth())
        self.memNameLbl_0.setSizePolicy(sizePolicy4)
        font8 = QFont()
        font8.setFamilies([u"Raleway"])
        font8.setPointSize(16)
        font8.setBold(True)
        self.memNameLbl_0.setFont(font8)
        self.memNameLbl_0.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.memNameLbl_0)

        self.memClockSpeedLbl_0 = QLabel(self.mem1Frame)
        self.memClockSpeedLbl_0.setObjectName(u"memClockSpeedLbl_0")
        font9 = QFont()
        font9.setFamilies([u"Raleway"])
        font9.setPointSize(12)
        font9.setBold(False)
        self.memClockSpeedLbl_0.setFont(font9)
        self.memClockSpeedLbl_0.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.memClockSpeedLbl_0)

        self.memVoltageLbl_0 = QLabel(self.mem1Frame)
        self.memVoltageLbl_0.setObjectName(u"memVoltageLbl_0")
        self.memVoltageLbl_0.setFont(font9)
        self.memVoltageLbl_0.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.memVoltageLbl_0)

        self.memDataWidthLbl_0 = QLabel(self.mem1Frame)
        self.memDataWidthLbl_0.setObjectName(u"memDataWidthLbl_0")
        self.memDataWidthLbl_0.setFont(font9)
        self.memDataWidthLbl_0.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.memDataWidthLbl_0)

        self.memSerialNoLbl_0 = QLabel(self.mem1Frame)
        self.memSerialNoLbl_0.setObjectName(u"memSerialNoLbl_0")
        self.memSerialNoLbl_0.setFont(font9)
        self.memSerialNoLbl_0.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.memSerialNoLbl_0)

        self.memCapacityLbl_0 = QLabel(self.mem1Frame)
        self.memCapacityLbl_0.setObjectName(u"memCapacityLbl_0")
        self.memCapacityLbl_0.setFont(font9)
        self.memCapacityLbl_0.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.memCapacityLbl_0)


        self.horizontalLayout_7.addWidget(self.mem1Frame)

        self.mem2Frame = QFrame(self.memoryInfoFrame)
        self.mem2Frame.setObjectName(u"mem2Frame")
        self.mem2Frame.setFrameShape(QFrame.NoFrame)
        self.mem2Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.mem2Frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.memNameLbl_1 = QLabel(self.mem2Frame)
        self.memNameLbl_1.setObjectName(u"memNameLbl_1")
        sizePolicy4.setHeightForWidth(self.memNameLbl_1.sizePolicy().hasHeightForWidth())
        self.memNameLbl_1.setSizePolicy(sizePolicy4)
        self.memNameLbl_1.setFont(font8)
        self.memNameLbl_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.memNameLbl_1)

        self.memClockSpeedLbl_1 = QLabel(self.mem2Frame)
        self.memClockSpeedLbl_1.setObjectName(u"memClockSpeedLbl_1")
        self.memClockSpeedLbl_1.setFont(font9)
        self.memClockSpeedLbl_1.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.memClockSpeedLbl_1)

        self.memVoltageLbl_1 = QLabel(self.mem2Frame)
        self.memVoltageLbl_1.setObjectName(u"memVoltageLbl_1")
        self.memVoltageLbl_1.setFont(font9)
        self.memVoltageLbl_1.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.memVoltageLbl_1)

        self.memDataWidthLbl_1 = QLabel(self.mem2Frame)
        self.memDataWidthLbl_1.setObjectName(u"memDataWidthLbl_1")
        self.memDataWidthLbl_1.setFont(font9)
        self.memDataWidthLbl_1.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.memDataWidthLbl_1)

        self.memSerialNoLbl_1 = QLabel(self.mem2Frame)
        self.memSerialNoLbl_1.setObjectName(u"memSerialNoLbl_1")
        self.memSerialNoLbl_1.setFont(font9)
        self.memSerialNoLbl_1.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.memSerialNoLbl_1)

        self.memCapacityLbl_1 = QLabel(self.mem2Frame)
        self.memCapacityLbl_1.setObjectName(u"memCapacityLbl_1")
        self.memCapacityLbl_1.setFont(font9)
        self.memCapacityLbl_1.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.memCapacityLbl_1)


        self.horizontalLayout_7.addWidget(self.mem2Frame)

        self.mem3Frame = QFrame(self.memoryInfoFrame)
        self.mem3Frame.setObjectName(u"mem3Frame")
        self.mem3Frame.setFrameShape(QFrame.NoFrame)
        self.mem3Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_25 = QVBoxLayout(self.mem3Frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.memNameLbl_2 = QLabel(self.mem3Frame)
        self.memNameLbl_2.setObjectName(u"memNameLbl_2")
        sizePolicy4.setHeightForWidth(self.memNameLbl_2.sizePolicy().hasHeightForWidth())
        self.memNameLbl_2.setSizePolicy(sizePolicy4)
        self.memNameLbl_2.setFont(font8)
        self.memNameLbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.memNameLbl_2)

        self.memClockSpeedLbl_2 = QLabel(self.mem3Frame)
        self.memClockSpeedLbl_2.setObjectName(u"memClockSpeedLbl_2")
        self.memClockSpeedLbl_2.setFont(font9)
        self.memClockSpeedLbl_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.memClockSpeedLbl_2)

        self.memVoltageLbl_2 = QLabel(self.mem3Frame)
        self.memVoltageLbl_2.setObjectName(u"memVoltageLbl_2")
        self.memVoltageLbl_2.setFont(font9)
        self.memVoltageLbl_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.memVoltageLbl_2)

        self.memDataWidthLbl_2 = QLabel(self.mem3Frame)
        self.memDataWidthLbl_2.setObjectName(u"memDataWidthLbl_2")
        self.memDataWidthLbl_2.setFont(font9)
        self.memDataWidthLbl_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.memDataWidthLbl_2)

        self.memSerialNoLbl_2 = QLabel(self.mem3Frame)
        self.memSerialNoLbl_2.setObjectName(u"memSerialNoLbl_2")
        self.memSerialNoLbl_2.setFont(font9)
        self.memSerialNoLbl_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.memSerialNoLbl_2)

        self.memCapacityLbl_2 = QLabel(self.mem3Frame)
        self.memCapacityLbl_2.setObjectName(u"memCapacityLbl_2")
        self.memCapacityLbl_2.setFont(font9)
        self.memCapacityLbl_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.memCapacityLbl_2)


        self.horizontalLayout_7.addWidget(self.mem3Frame)

        self.mem4Frame = QFrame(self.memoryInfoFrame)
        self.mem4Frame.setObjectName(u"mem4Frame")
        self.mem4Frame.setFrameShape(QFrame.NoFrame)
        self.mem4Frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_26 = QVBoxLayout(self.mem4Frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.memNameLbl_3 = QLabel(self.mem4Frame)
        self.memNameLbl_3.setObjectName(u"memNameLbl_3")
        sizePolicy4.setHeightForWidth(self.memNameLbl_3.sizePolicy().hasHeightForWidth())
        self.memNameLbl_3.setSizePolicy(sizePolicy4)
        self.memNameLbl_3.setFont(font8)
        self.memNameLbl_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.memNameLbl_3)

        self.memClockSpeedLbl_3 = QLabel(self.mem4Frame)
        self.memClockSpeedLbl_3.setObjectName(u"memClockSpeedLbl_3")
        self.memClockSpeedLbl_3.setFont(font9)
        self.memClockSpeedLbl_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.memClockSpeedLbl_3)

        self.memVoltageLbl_3 = QLabel(self.mem4Frame)
        self.memVoltageLbl_3.setObjectName(u"memVoltageLbl_3")
        self.memVoltageLbl_3.setFont(font9)
        self.memVoltageLbl_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.memVoltageLbl_3)

        self.memDataWidthLbl_3 = QLabel(self.mem4Frame)
        self.memDataWidthLbl_3.setObjectName(u"memDataWidthLbl_3")
        self.memDataWidthLbl_3.setFont(font9)
        self.memDataWidthLbl_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.memDataWidthLbl_3)

        self.memSerialNoLbl_3 = QLabel(self.mem4Frame)
        self.memSerialNoLbl_3.setObjectName(u"memSerialNoLbl_3")
        self.memSerialNoLbl_3.setFont(font9)
        self.memSerialNoLbl_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.memSerialNoLbl_3)

        self.memCapacityLbl_3 = QLabel(self.mem4Frame)
        self.memCapacityLbl_3.setObjectName(u"memCapacityLbl_3")
        self.memCapacityLbl_3.setFont(font9)
        self.memCapacityLbl_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.memCapacityLbl_3)


        self.horizontalLayout_7.addWidget(self.mem4Frame)


        self.verticalLayout_22.addWidget(self.memoryInfoFrame)


        self.verticalLayout_21.addWidget(self.memoryMainFrame)

        self.infoWidget.addWidget(self.memoryPage)

        self.verticalLayout_2.addWidget(self.infoWidget)


        self.verticalLayout.addWidget(self.infoFrame)

        infoMainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(infoMainWindow)

        self.infoWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(infoMainWindow)
    # setupUi

    def retranslateUi(self, infoMainWindow):
        infoMainWindow.setWindowTitle(QCoreApplication.translate("infoMainWindow", u"SYSTEM-Z", None))
        self.headerLbl.setText(QCoreApplication.translate("infoMainWindow", u"SYSTEM-Z", None))
        self.homeBtn.setText(QCoreApplication.translate("infoMainWindow", u"HOME", None))
        self.cpuBtn.setText(QCoreApplication.translate("infoMainWindow", u"CPU", None))
        self.gpuBtn.setText(QCoreApplication.translate("infoMainWindow", u"DISPLAY", None))
        self.memBtn.setText(QCoreApplication.translate("infoMainWindow", u"MEMORY", None))
        self.systemHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"System Information", None))
        self.computerNameLbl.setText(QCoreApplication.translate("infoMainWindow", u"[ COMPUTER NAME ]", None))
        self.dateTimeLbl.setText(QCoreApplication.translate("infoMainWindow", u"Current Date/Time: ", None))
        self.osLbl.setText(QCoreApplication.translate("infoMainWindow", u"Operating System: ", None))
        self.langLbl.setText(QCoreApplication.translate("infoMainWindow", u"Language: ", None))
        self.sysModelLbl.setText(QCoreApplication.translate("infoMainWindow", u"System Model: ", None))
        self.biosLbl.setText(QCoreApplication.translate("infoMainWindow", u"BIOS: ", None))
        self.cpuHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"CPU", None))
        self.cpuInfoHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"cpu name", None))
        self.cpuNumsLbl.setText(QCoreApplication.translate("infoMainWindow", u"Number of cores and threads: ", None))
        self.cpuManufacturerLbl.setText(QCoreApplication.translate("infoMainWindow", u"Manufacturer: ", None))
        self.cpuArchLbl.setText(QCoreApplication.translate("infoMainWindow", u"Architecture: ", None))
        self.cpuMinHzLbl.setText(QCoreApplication.translate("infoMainWindow", u"Minimum Clock Speed: ", None))
        self.cpuMaxHzLbl.setText(QCoreApplication.translate("infoMainWindow", u"Maximum Clock Speed:", None))
        self.cpuFlagsHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"Flags", None))
        self.intelHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"intel", None))
        self.lmCheck.setText(QCoreApplication.translate("infoMainWindow", u"lm", None))
        self.vmxCheck.setText(QCoreApplication.translate("infoMainWindow", u"vmx", None))
        self.smxCheck.setText(QCoreApplication.translate("infoMainWindow", u"smx", None))
        self.sse3Check.setText(QCoreApplication.translate("infoMainWindow", u"sse3", None))
        self.pnCheck.setText(QCoreApplication.translate("infoMainWindow", u"pn", None))
        self.paeCheck.setText(QCoreApplication.translate("infoMainWindow", u"pae", None))
        self.htCheck.setText(QCoreApplication.translate("infoMainWindow", u"ht", None))
        self.acpiCheck.setText(QCoreApplication.translate("infoMainWindow", u"acpi", None))
        self.sseCheck.setText(QCoreApplication.translate("infoMainWindow", u"sse", None))
        self.sse2Check.setText(QCoreApplication.translate("infoMainWindow", u"sse2", None))
        self.hypervisorCheck.setText(QCoreApplication.translate("infoMainWindow", u"hypervisor", None))
        self.pdcmCheck.setText(QCoreApplication.translate("infoMainWindow", u"pdcm", None))
        self.tmCheck.setText(QCoreApplication.translate("infoMainWindow", u"tm", None))
        self.sse4_1Check.setText(QCoreApplication.translate("infoMainWindow", u"sse4_1", None))
        self.sse4_2Check.setText(QCoreApplication.translate("infoMainWindow", u"sse4_2", None))
        self.amdHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"AMD", None))
        self.svmCheck.setText(QCoreApplication.translate("infoMainWindow", u"svm", None))
        self.sse4aCheck.setText(QCoreApplication.translate("infoMainWindow", u"sse4a", None))
        self.mpCheck.setText(QCoreApplication.translate("infoMainWindow", u"mp", None))
        self.amdLMCheck.setText(QCoreApplication.translate("infoMainWindow", u"lm", None))
        self.abmCheck.setText(QCoreApplication.translate("infoMainWindow", u"abm", None))
        self.armHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"arm", None))
        self.twoSixBitCheck.setText(QCoreApplication.translate("infoMainWindow", u"26bit", None))
        self.javaCheck.setText(QCoreApplication.translate("infoMainWindow", u"java", None))
        self.lpaeCheck.setText(QCoreApplication.translate("infoMainWindow", u"lpae", None))
        self.thumbCheck.setText(QCoreApplication.translate("infoMainWindow", u"thumb", None))
        self.neonCheck.setText(QCoreApplication.translate("infoMainWindow", u"neon", None))
        self.gpuHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"Display / GPU", None))
        self.gpuInfoHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"res | refresh rate (bit depth)", None))
        self.gpuNameLbl.setText(QCoreApplication.translate("infoMainWindow", u"Name:", None))
        self.gpuDriverVerLbl.setText(QCoreApplication.translate("infoMainWindow", u"Driver Version:", None))
        self.gpuProcessorLbl.setText(QCoreApplication.translate("infoMainWindow", u"Video Processor:", None))
        self.gpuDACLbl.setText(QCoreApplication.translate("infoMainWindow", u"Adapter DAC Type:", None))
        self.gpuCompatLbl.setText(QCoreApplication.translate("infoMainWindow", u"Adapter Compatibility:", None))
        self.gpuMinHzLbl.setText(QCoreApplication.translate("infoMainWindow", u"Minimum Refresh Rate", None))
        self.gpuMaxHzLbl.setText(QCoreApplication.translate("infoMainWindow", u"Maximum Refresh Rate:", None))
        self.memHeadingLbl.setText(QCoreApplication.translate("infoMainWindow", u"Memory", None))
        self.memHeadingInfoLbl.setText(QCoreApplication.translate("infoMainWindow", u"TOTAL MEMORY", None))
        self.memNameLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"MEMORY PART NAME", None))
        self.memClockSpeedLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"Clock Speed", None))
        self.memVoltageLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"Voltage", None))
        self.memDataWidthLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"Data Width", None))
        self.memSerialNoLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"Serial Number", None))
        self.memCapacityLbl_0.setText(QCoreApplication.translate("infoMainWindow", u"Capacity", None))
        self.memNameLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"MEMORY PART NAME", None))
        self.memClockSpeedLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"Clock Speed", None))
        self.memVoltageLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"Voltage", None))
        self.memDataWidthLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"Data Width", None))
        self.memSerialNoLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"Serial Number", None))
        self.memCapacityLbl_1.setText(QCoreApplication.translate("infoMainWindow", u"Capacity", None))
        self.memNameLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"MEMORY PART NAME", None))
        self.memClockSpeedLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"Clock Speed", None))
        self.memVoltageLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"Voltage", None))
        self.memDataWidthLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"Data Width", None))
        self.memSerialNoLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"Serial Number", None))
        self.memCapacityLbl_2.setText(QCoreApplication.translate("infoMainWindow", u"Capacity", None))
        self.memNameLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"MEMORY PART NAME", None))
        self.memClockSpeedLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"Clock Speed", None))
        self.memVoltageLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"Voltage", None))
        self.memDataWidthLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"Data Width", None))
        self.memSerialNoLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"Serial Number", None))
        self.memCapacityLbl_3.setText(QCoreApplication.translate("infoMainWindow", u"Capacity", None))
    # retranslateUi

