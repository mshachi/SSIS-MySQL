"""
File: py_student.py
Author: Febe Gwyn R. Belvis
Description: A Python program for a simple student information manager.
"""

import sys
from PyQt5 import QtWidgets
import mysql.connector

from mainwindow_ui import Ui_MainWindow
from connect_database import ConnectDatabase
from addstudent_ui import Ui_addStudentDialog
from editstudent_ui import Ui_editStudentDialog
from addcourse_ui import Ui_addCourseDialog
from editcourse_ui import Ui_editcourse

searchStudentBy = ['ID Number', 'Name', 'Year Level', 'Course']

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize the UI from a separate UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create a database connection object
        self.db = ConnectDatabase()

        # connect UI elements to class variables
        self.addStudent = self.ui.addStudent
        self.deleteStudent = self.ui.deleteStudent
        self.editStudent = self.ui.editStudent
        self.refreshButton = self.ui.reloadButton
        self.studentTree = self.ui.studentTree

        self.courseTree = self.ui.courseTree
        self.searchCourse = self.ui.searchCourseField
        self.addCourse = self.ui.addCourse
        self.editCourse = self.ui.editCourse
        self.deleteCourse = self.ui.deleteCourse

        self.searchComboBox = self.ui.searchComboBox
        self.searchStudent = self.ui.searchStudentField

        
        # initialize signal-slot connections
        self.init_signal_slot()

        #populate the initial data in the treeviews
        self.populate_student_tree()
        self.populate_course_tree()

    def init_signal_slot(self):
        # connect buttons to their respective functions
        self.addStudent.clicked.connect(self.open_add_student_dialog)
        self.searchComboBox.addItems(searchStudentBy)
        self.get_search_by()
        self.searchComboBox.currentTextChanged.connect(self.get_search_by)
        self.deleteStudent.clicked.connect(self.open_delete_student_dialog)
        self.deleteCourse.clicked.connect(self.open_delete_course_dialog)
        self.editStudent.clicked.connect(self.open_edit_student_dialog)
        self.refreshButton.clicked.connect(self.populate_student_tree)
        self.refreshButton.clicked.connect(self.populate_course_tree)
        self.studentTree.itemClicked.connect(self.clear_student_selection)
        self.courseTree.itemClicked.connect(self.clear_course_selection)
        self.searchStudent.textChanged.connect(self.filter_student_tree)
        self.searchCourse.textChanged.connect(self.filter_course_tree)
        self.addCourse.clicked.connect(self.open_add_course_dialog)
        self.editCourse.clicked.connect(self.open_edit_course_dialog)

    def get_search_by(self):
        searchBy = self.searchComboBox.currentText()
        if searchBy == "Course":
            self.searchStudent.setPlaceholderText(f"Enter {searchBy} code")
        else:
            self.searchStudent.setPlaceholderText(f"Enter {searchBy}")

    def filter_student_tree(self):
        search_text = self.searchStudent.text().strip()
        category = self.searchComboBox.currentText()
        if search_text and category:
            # Filter the student tree based on the selected category and entered text
            for i in range(self.studentTree.topLevelItemCount()):
                item = self.studentTree.topLevelItem(i)
                if not search_text.lower() in item.text(searchStudentBy.index(category)).lower():
                    item.setHidden(True)
                else:
                    item.setHidden(False)
        else:
            # If search text or category is empty, show all items
            for i in range(self.studentTree.topLevelItemCount()):
                self.studentTree.topLevelItem(i).setHidden(False)

    def filter_course_tree(self):
        search_text = self.searchCourse.text().strip().lower()  # Convert search text to lowercase for case-insensitive search
        if search_text:
            # Filter the course tree based on the entered text
            for i in range(self.courseTree.topLevelItemCount()):
                item = self.courseTree.topLevelItem(i)
                course_code = item.text(0).lower()
                course_name = item.text(1).lower()
                # Check if the search text is present in either course code or course name
                if search_text in course_code or search_text in course_name:
                    item.setHidden(False)
                else:
                    item.setHidden(True)
        else:
            # If search text is empty, show all items
            for i in range(self.courseTree.topLevelItemCount()):
                self.courseTree.topLevelItem(i).setHidden(False)

    # connect to add student dialog 
    def open_add_student_dialog(self):
        self.add_student_dialog = AddStudentDialog(parent=self, connection=self.db)
        self.add_student_dialog.accepted.connect(self.populate_student_tree) 
        self.add_student_dialog.exec_()
    
    def open_add_course_dialog(self):
        self.add_course_dialog = AddCourseDialog(parent=self, connection=self.db)
        self.add_course_dialog.accepted.connect(self.populate_course_tree)
        self.add_course_dialog.exec_()
        
    def open_edit_student_dialog(self):
        selected_item = self.studentTree.currentItem()
        if selected_item is not None:
            student_id = selected_item.text(0)
            self.edit_student_dialog = EditStudentDialog(parent=self, connection=self.db, student_id=student_id)
            self.edit_student_dialog.accepted.connect(self.populate_student_tree)
            self.edit_student_dialog.exec_()
        else:
            QtWidgets.QMessageBox.warning(self, 'No Student Selected', "Please select a student to edit.")

    def open_edit_course_dialog(self):
        course_selected_item = self.courseTree.currentItem()
        if course_selected_item is not None:
            course_code = course_selected_item.text(0)
            course_name = course_selected_item.text(1)
            self.edit_course_dialog = EditCourseDialog(parent=self, connection=self.db, course_code=course_code)
            self.edit_course_dialog.accepted.connect(self.populate_course_tree)
            self.edit_course_dialog.exec_()
        else:
            QtWidgets.QMessageBox.warning(self, 'No Course Selected', "Please select a Course to delete.")

    def populate_student_tree(self):
        self.studentTree.clear()
        student_info = self.db.search_student_info()

        for student in student_info:
            item = QtWidgets.QTreeWidgetItem(self.studentTree)
            item.setText(0, student['id_number'])
            item.setText(1, student['name'])
            item.setText(2, str(student['age']))
            item.setText(3, student['gender'])
            if student['course'] == None:
                item.setText(4, "N/A")
            else:
                item.setText(4, student['course'])
            item.setText(5, str(student['year_level']))

    def populate_course_tree(self):
        self.courseTree.clear()
        courses_info = self.db.search_course_info()

        for course in courses_info:
            item = QtWidgets.QTreeWidgetItem(self.courseTree)
            item.setText(0, course['course_code'])
            item.setText(1, course['courses_name'])
          
    def open_delete_student_dialog(self):
        student_selected_item = self.studentTree.currentItem()
        if student_selected_item is not None:
            student_id = student_selected_item.text(0)
            confirm = QtWidgets.QMessageBox.question(
                self, 'Confirm Deletion',
                f"Do you want to delete Student {student_id}?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if confirm == QtWidgets.QMessageBox.Yes:
               self.db.delete_student(student_id) 
               self.populate_student_tree()


        else:
            QtWidgets.QMessageBox.warning(self, 'No Student Selected', "Please select a student to delete.")
    
    def open_delete_course_dialog(self):
        course_selected_item = self.courseTree.currentItem()
        if course_selected_item is not None:
            course_code = course_selected_item.text(0)
            confirm = QtWidgets.QMessageBox.question(
                self, 'Confirm Deletion',
                f"Do you want to delete course {course_code}?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )

            if confirm == QtWidgets.QMessageBox.Yes:
               self.db.delete_course(course_code) 
               self.populate_course_tree()
               self.populate_student_tree()
        else:
            QtWidgets.QMessageBox.warning(self, 'No Course Selected', "Please select a course to delete.")

    def clear_student_selection(self, item):
        if not item:
            self.studentTree.clearSelection()

    def clear_course_selection(self, item):
        if not item:
            self.courseTree.clearSelection()

class AddStudentDialog(QtWidgets.QDialog):
    def __init__(self, parent, connection):
        super(AddStudentDialog, self).__init__(parent)

        self.setWindowTitle("Add Student")

        # Initialize the Add Student dialog UI
        self.ui = Ui_addStudentDialog()
        self.ui.setupUi(self)

        # Initialize the courseComboBox
        self.courseComboBox = self.ui.courseComboBox

        # Create database connection object
        self.connection = connection

        # Connect buttons to their respective functions
        self.ui.addStudent_confirm.clicked.connect(self.add_student)
        self.ui.cancelAdd.clicked.connect(self.close)

        # load courses into course combobox
        self.load_course_codes()


    def add_student(self):
        # Retrieve the information entered by the user
        name = self.ui.addNameField.text().strip()  # Strip whitespace from the name field
        
        # Check if the name field is empty
        if not name:
            QtWidgets.QMessageBox.warning(self, "Empty Name Field", "Please enter a name.")
            return
        
        # Retrieve valid ID Number
        id_year = self.ui.addIDNumField_Year.text()
        id_number = self.ui.addIDNumField_Number.text()
        if not (id_year.isdigit() and id_number.isdigit() and len(id_year) == 4 and len(id_number) == 4):
            QtWidgets.QMessageBox.warning(self, "Invalid ID Number", "Please enter a valid ID Number")
            return
    
        student_id = f"{id_year}-{id_number}"

        # Check if the student ID already exists in the database
        existing_student = self.connection.search_student_info(student_id)
        if existing_student:
            QtWidgets.QMessageBox.warning(self, "Duplicate Student ID", f"Student with ID {id_number} already exists.")
            return
        
        # Check if there is a selected gender
        if not (self.get_gender() == ""):
            gender = self.get_gender()
        else:
            QtWidgets.QMessageBox.warning(self, "No Gender Selected", "Please select student gender.")
            return

        year_level = self.ui.yearSpinBox.value()
        age = self.ui.ageSpinBox.value()
        course = str(self.get_course())
        

        # If the name field is not empty and the student ID is unique, proceed to add the student to the database
        # Add your logic to add the student to the database
        self.connection.add_info(student_id, name, age, gender, course, year_level)

        self.accept()
        
        # Close the dialog
        self.close()
    
    def get_gender(self):
        if self.ui.maleRadBut.isChecked():
            return "Male"
        elif self.ui.femaleRadBut.isChecked():
            return "Female"
        else:
            return ""
        
    def get_course(self):
        return self.courseComboBox.currentText()
        
    def load_course_codes(self):
            courses_info = self.connection.search_course_info()
            for course in courses_info:
                self.courseComboBox.addItem(course['course_code'])

class AddCourseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connection):
        super(AddCourseDialog, self).__init__(parent)

        self.ui = Ui_addCourseDialog()
        self.ui.setupUi(self)

        # Create database connection object
        self.connection = connection

        self.setWindowTitle("Add Course")

        self.ui.addCourseConfirm.clicked.connect(self.confirm_course)
        self.ui.cancelCourse.clicked.connect(self.reject)

    def confirm_course(self):
        course_code = self.ui.courseCodeField.text().strip()
        course_name = self.ui.courseNameField.text().strip()
        
        # Check if course code or course name is empty
        if not course_code or not course_name:
            QtWidgets.QMessageBox.warning(self, "Empty Fields", "Please enter both course code and course name.")
            return
        
        # Check if course code already exists in the database
        if self.connection.search_course_info(course_code):
            QtWidgets.QMessageBox.warning(self, "Duplicate Course Code", f"Course with code {course_code} already exists.")
            return

        # If the course code is unique, proceed to add the course to the database
        self.connection.add_course(course_code, course_name)
        self.accept()
        self.close()
        

        
class EditStudentDialog(QtWidgets.QDialog):
    def __init__(self, parent, connection, student_id):
        super(EditStudentDialog, self).__init__(parent)
        
        self.ui = Ui_editStudentDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Edit Student")

        # Initialize the courseComboBox
        self.courseComboBox = self.ui.courseComboBox

        # Initialize other attributes
        self.connection = connection
        self.student_id = student_id

        # Connect signals to slots
        self.ui.editStudent_confirm.clicked.connect(self.edit_student)
        self.ui.cancelAdd.clicked.connect(self.close)

        # Load student information
        self.load_student_info(student_id)
        # Load courses into course combobox
        self.load_course_codes()

    def load_student_info(self, student_id):
        try:
            student_info = self.connection.search_student_info(student_id)
            # Check if student_info is not empty
            if student_info:
                # Iterate over the list of dictionaries
                for student in student_info:
                    # Access the desired field, for example, 'name'
                    name = student['name']
                    age = student['age']
                    gender = student['gender']
                    course = student['course']
                    year_level = student['year_level']
                    
                    self.ui.addNameField.setText(name)
                    self.ui.ageSpinBox.setValue(age)
                    if gender == 'Female':
                        self.ui.femaleRadBut.setChecked(True)
                    elif gender == 'Male':
                        self.ui.maleRadBut.setChecked(True)
                    self.ui.courseComboBox.setCurrentText(course)
                    self.ui.yearSpinBox.setValue(year_level)
            else:
                print("No student found with the specified ID.")
        except Exception as e:
            print("An error occurred while loading student information:", e)


    def edit_student(self):
            try:
                # Retrieve the information entered by the user
                name = self.ui.addNameField.text().strip()  # Strip whitespace from the name field
                
                # Check if the name field is empty
                if not name:
                    QtWidgets.QMessageBox.warning(self, "Empty Name Field", "Please enter a name.")
                    return

                
                # Check if there is a selected gender
                if not (self.get_gender() == ""):
                    gender = self.get_gender()
                else:
                    QtWidgets.QMessageBox.warning(self, "No Gender Selected", "Please select student gender.")
                    return

                year_level = self.ui.yearSpinBox.value()
                age = self.ui.ageSpinBox.value()
                course = str(self.get_course())
                

                # If the name field is not empty and the student ID is unique, proceed to add the student to the database
                # Add your logic to add the student to the database
                self.connection.update_info(self.student_id, name, age, gender, course, year_level)

                self.accept()
                
                # Close the dialog
                self.close()
            except Exception as e:
                print("An error occurred:", e)

    def get_gender(self):
            if self.ui.maleRadBut.isChecked():
                return "Male"
            elif self.ui.femaleRadBut.isChecked():
                return "Female"
            else:
                return ""
        
    def get_course(self):
            return self.courseComboBox.currentText()
            
    def load_course_codes(self):
                courses_info = self.connection.search_course_info()
                for course in courses_info:
                    self.courseComboBox.addItem(course['course_code'])

class EditCourseDialog(QtWidgets.QDialog):
    def __init__(self, parent, connection, course_code):
        super(EditCourseDialog, self).__init__(parent)

        self.ui = Ui_editcourse()
        self.ui.setupUi(self)

        self.setWindowTitle("Edit Course")

        # Initialize other attributes
        self.connection = connection
        self.course_code = course_code

        # Connect signals to slots
        self.ui.editCourseConfirm.clicked.connect(self.edit_course)
        self.ui.cancelEditCourse.clicked.connect(self.close)

        self.load_course_info(course_code)

    def load_course_info(self, course_code):
        try:
            course_info = self.connection.search_course_info(course_code)
            if course_info:
                    # Iterate over the list of dictionaries
                    for course in course_info:
                        # Access the desired field, for example, 'name'
                        course_code = course['course_code']
                        course_name = course['courses_name']

                        self.ui.courseCodeField.setText(course_code)
                        self.ui.courseNameField.setText(course_name)
        except Exception as e:
            print("An error occurred while loading course information:", e)

    def edit_course(self):
        try:
            # Retrieve the information entered by the user
            new_course_code = self.ui.courseCodeField.text().strip()
            new_course_name = self.ui.courseNameField.text().strip()
            
            # Check if the fields are empty
            if not new_course_code or not new_course_name:
                QtWidgets.QMessageBox.warning(self, "Empty Fields", "Please enter both course code and course name.")
                return
            
            # If the course code is being changed, check if the new code already exists
            if new_course_code != self.course_code and self.connection.search_course_info(new_course_code):
                QtWidgets.QMessageBox.warning(self, "Duplicate Course Code", f"Course with code {new_course_code} already exists.")
                return

            # If everything is valid, proceed to update the course
            self.connection.update_course(self.course_code, new_course_name, new_course_code)
            self.accept()
            self.close()
        except Exception as e:
            print("An error occurred:", e)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
