import mysql.connector

class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "root"
        self._password = "FGBelvis11200204"
        self._database = "db_studentinfo"
        self.con = None
        self.cursor = None

    def connect_db(self):
        # establish a database connection
        self.con = mysql.connector.connect(
            host = self._host,
            port = self._port,
            database = self._database,
            user = self._user,
            password = self._password
        )

        # create a cursor for executing SQL queries
        self.cursor = self.con.cursor(dictionary = True)

    def add_info(self, student_id,name,age,gender,course,year):
        try:
            # Establish database connection
            self.connect_db()

            # Execute SQL query to insert student information
            sql = "INSERT INTO db_studentinfo.students_info (id_number, name, age, gender, course, year_level) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (student_id, name, age, gender, course, year)
            self.cursor.execute(sql, values)
            self.con.commit()
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # Close database connection
            if self.con:
                self.con.close()

    def add_course(self, course_code, course_name):
        try:
            # Establish database connection
            self.connect_db()

            # Execute SQL query to insert student information
            sql = "INSERT INTO db_studentinfo.courses_info (course_code, courses_name) VALUES (%s, %s)"
            values = (course_code,course_name)
            self.cursor.execute(sql, values)
            self.con.commit()
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # Close database connection
            if self.con:
                self.con.close()
                

    def update_info(self, student_id, name, age, gender,course, year):
        try:
            # Connect to the database
            self.connect_db()

            # Construct SQL query for updating information
            sql = """
                UPDATE students_info
                SET name = %s, age = %s, gender = %s, course = %s, year_level = %s
                WHERE id_number = %s
            """

            # Execute the SQL query
            self.cursor.execute(sql, (name, age, gender, course, year, student_id))
            self.con.commit()
            print("Student information updated successfully")
    
        except mysql.connector.Error as error:
            print("Failed to update student information:", error)
            # Rollback in case of error
            self.con.rollback()

        finally:
            # Close the database connection
            if self.con:
                self.con.close()

    def update_course(self, course_code, new_course_name, new_course_code):
        try:
            # Connect to the database
            self.connect_db()

            # Construct SQL query for updating information
            sql = """
                UPDATE courses_info
                SET course_code = %s, courses_name = %s
                WHERE course_code = %s
            """

            # Execute the SQL query
            self.cursor.execute(sql, (new_course_code, new_course_name, course_code))
            self.con.commit()
            print("Course Information updated successfully")
    
        except mysql.connector.Error as error:
            print("Failed to update Course information:", error)
            # Rollback in case of error
            self.con.rollback()

        finally:
            # Close the database connection
            if self.con:
                self.con.close()


    def delete_student(self, student_id):
        try:
            # Establish database connection
            self.connect_db()

            # Execute the DELETE query
            query = "DELETE FROM students_info WHERE id_number = %s"
            self.cursor.execute(query, (student_id,))  
            # Commit the changes
            self.con.commit()
            print("Student deleted successfully")
        except mysql.connector.Error as error:
            print("Failed to delete student:", error)
            # Rollback in case of error
            self.con.rollback()
        finally:
            # Close the database connection
            if self.con:
                self.con.close()
    
    def delete_course(self, course_code):
        try:
            # Establish database connection
            self.connect_db()
            
            # Delete the course
            delete_query = "DELETE FROM courses_info WHERE course_code = %s"
            self.cursor.execute(delete_query, (course_code,))
            self.con.commit()
        
        except mysql.connector.Error as error:
            # Rollback in case of error
            self.con.rollback()
        finally:
            # Close the database connection
            if self.con:
                self.con.close()

    def search_student_info(self, student_id=None, name=None, age=None, gender=None, course=None, year=None):
        try:
            # Connect to the database
            self.connect_db()

            condition = ""
            if student_id:
                condition += f"id_number LIKE '%{student_id}%'"
            else:
                if name:
                    if condition:
                        condition += f" and name LIKE '%{name}%'"
                    else:
                        condition += f"name LIKE '%{name}%'"

                if age:
                    if condition:
                        condition += f" and age={age}"
                    else:
                        condition += f"age={age}"

                if gender:
                    if condition:
                        condition += f" and gender='{gender}'"
                    else:
                        condition += f"gender='{gender}'"

                if course:
                    if condition:
                        condition += f" and course LIKE '%{course}%'"
                    else:
                        condition += f"course LIKE '%{course}%'"
                if year:
                    if condition:
                        condition += f" and year_level={year}"
                    else:
                        condition += f"year_level={year}"

            if condition:
                # Construct SQL query for searching information with conditions
                sql = f"""
                    SELECT * FROM students_info WHERE {condition};
                """
            else:
                # Construct SQL query for searching all information
                sql = f"""
                    SELECT * FROM students_info;
                """

            # Execute the SQL query for searching information
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except mysql.connector.Error as error:
            print("Failed to search for student information:", error)
            return []

        finally:
            # Close the database connection
            if self.con:
                self.con.close()

    def search_course_info(self, course_code=None, course_name=None):
        # Connect to the database
        self.connect_db()

        condition = ""
        if course_code:
            condition += f"course_code LIKE '%{course_code}%'"
        else:
            if course_name:
                if condition:
                    condition += f" and courses_name LIKE '%{course_name}%'"
                else:
                    condition += f"courses_name LIKE '%{course_name}%'"

        if condition:
            # Construct SQL query for searching information with conditions
            sql = f"""
                SELECT * FROM courses_info WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            sql = f"""
                SELECT * FROM courses_info;
            """

        try:
            # Execute the SQL query for searching information
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as e:
            print("Error occurred in search_course_info:", e)
            return []

        finally:
            # Close the database connection
            self.con.close()