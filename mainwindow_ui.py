# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1404, 710)
        MainWindow.setStyleSheet("background-color:#FCF7F8;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 751, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addStudent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addStudent.setStyleSheet("background-color:rgb(85, 207, 8);\n"
"color: white;")
        self.addStudent.setObjectName("addStudent")
        self.horizontalLayout_2.addWidget(self.addStudent)
        self.editStudent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editStudent.setStyleSheet("background-color: rgb(255, 150, 30);\n"
"color: white")
        self.editStudent.setObjectName("editStudent")
        self.horizontalLayout_2.addWidget(self.editStudent)
        self.deleteStudent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteStudent.setStyleSheet("background-color:rgb(255, 80, 64);\n"
"color: white")
        self.deleteStudent.setObjectName("deleteStudent")
        self.horizontalLayout_2.addWidget(self.deleteStudent)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.studentTree = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.studentTree.setAutoFillBackground(False)
        self.studentTree.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.studentTree.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.studentTree.setObjectName("studentTree")
        self.studentTree.headerItem().setText(0, "ID Number")
        self.studentTree.header().setVisible(True)
        self.studentTree.header().setCascadingSectionResizes(False)
        self.verticalLayout_4.addWidget(self.studentTree)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(810, 110, 571, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addCourse = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addCourse.setStyleSheet("background-color: rgb(88, 95, 227);\n"
"color: white")
        self.addCourse.setObjectName("addCourse")
        self.horizontalLayout_3.addWidget(self.addCourse)
        self.editCourse = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.editCourse.setStyleSheet("background-color: rgb(255, 150, 30);\n"
"color: white")
        self.editCourse.setObjectName("editCourse")
        self.horizontalLayout_3.addWidget(self.editCourse)
        self.deleteCourse = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.deleteCourse.setStyleSheet("background-color:rgb(255, 80, 64);\n"
"color: white")
        self.deleteCourse.setObjectName("deleteCourse")
        self.horizontalLayout_3.addWidget(self.deleteCourse)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.courseTree = QtWidgets.QTreeWidget(self.verticalLayoutWidget_2)
        self.courseTree.setObjectName("courseTree")
        self.courseTree.headerItem().setText(0, "Course Code")
        self.verticalLayout_5.addWidget(self.courseTree)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 15pt \"Nirmala UI Semilight\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.searchStudentField = QtWidgets.QLineEdit(self.centralwidget)
        self.searchStudentField.setGeometry(QtCore.QRect(350, 70, 421, 31))
        self.searchStudentField.setPlaceholderText("")
        self.searchStudentField.setObjectName("searchStudentField")
        self.searchCourseField = QtWidgets.QLineEdit(self.centralwidget)
        self.searchCourseField.setGeometry(QtCore.QRect(920, 70, 451, 31))
        self.searchCourseField.setText("")
        self.searchCourseField.setObjectName("searchCourseField")
        self.reloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.reloadButton.setGeometry(QtCore.QRect(20, 660, 89, 27))
        self.reloadButton.setObjectName("reloadButton")
        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(145, 68, 191, 31))
        self.searchComboBox.setObjectName("searchComboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 75, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information System"))
        self.addStudent.setText(_translate("MainWindow", "Add Student"))
        self.editStudent.setText(_translate("MainWindow", "Edit Student"))
        self.deleteStudent.setText(_translate("MainWindow", "Delete Student"))
        self.label.setText(_translate("MainWindow", "Student List:"))
        self.studentTree.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.studentTree.headerItem().setText(2, _translate("MainWindow", "Age"))
        self.studentTree.headerItem().setText(3, _translate("MainWindow", "Gender"))
        self.studentTree.headerItem().setText(4, _translate("MainWindow", "Year Level"))
        self.studentTree.headerItem().setText(5, _translate("MainWindow", "Course"))
        self.addCourse.setText(_translate("MainWindow", "Add Course"))
        self.editCourse.setText(_translate("MainWindow", "Edit Course"))
        self.deleteCourse.setText(_translate("MainWindow", "Delete Course"))
        self.label_2.setText(_translate("MainWindow", "Courses:"))
        self.courseTree.headerItem().setText(1, _translate("MainWindow", "Course Name"))
        self.label_3.setText(_translate("MainWindow", "Student Information System"))
        self.searchCourseField.setPlaceholderText(_translate("MainWindow", "Enter Course Code or Name"))
        self.reloadButton.setText(_translate("MainWindow", "Reload"))
        self.label_4.setText(_translate("MainWindow", "Search student by:"))
        self.label_5.setText(_translate("MainWindow", "Search Course:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())