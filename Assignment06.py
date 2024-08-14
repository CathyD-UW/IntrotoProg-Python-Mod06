# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions and classes
# with structured error handling
# Change Log: (Who, When, What)
# CDuPuis,8/14/2024,Completed Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"


class FileProcessor:
    """Processes data to and from a file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from a JSON file into a list of dictionary rows """
        file = None
        try:
            file = open(file_name, "r")
            student_data.clear()
            student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages(f"File '{file_name}' must exist before running this script.\n")
            IO.output_error_messages("Technical error message:")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            IO.output_error_messages("Non-specific error occurred.")
            IO.output_error_messages("Technical error message:")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file and not file.closed:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ Writes data from a list of dictionary rows to a JSON file """
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=4)
        except Exception as e:
            IO.output_error_messages("An error occurred while saving data to the file.")
            IO.output_error_messages("Technical error message:")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file and not file.closed:
                file.close()


class IO:
    """Handles Input and Output operations"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Outputs error messages to the user """
        print(f"Error: {message}")
        if error:
            print(f"Exception: {error}")

    @staticmethod
    def output_menu(menu: str):
        """ Outputs the main menu """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ Gets the user's menu choice """
        return input("Please enter your choice: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        """ Outputs the current list of registered students """
        if not student_data:
            print("No students are currently registered.")
        else:
            print("Current Student Data:")
            for student in student_data:
                print(f"{student['First Name']} {student['Last Name']} is registered for {student['Course']}")

    @staticmethod
    def input_student_data(student_data: list):
        """ Inputs a new student's data """
        while True:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                IO.output_error_messages("First name must contain only alphabetic characters. Please try again.")
                continue

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                IO.output_error_messages("Last name must contain only alphabetic characters. Please try again.")
                continue

            course_name = input("Enter the course name: ").strip()
            break

        # Add the student to the list
        student_data.append({"First Name": student_first_name, "Last Name": student_last_name, "Course": course_name})
        print(f"Student {student_first_name} {student_last_name} has been registered for the course '{course_name}'.")


def main():
    """ Main program logic """
    students = []
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == '1':
            IO.input_student_data(students)
        elif menu_choice == '2':
            IO.output_student_courses(students)
        elif menu_choice == '3':
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            IO.output_error_messages("Invalid choice, please select from the menu options.")


if __name__ == "__main__":
    main()
