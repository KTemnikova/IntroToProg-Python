# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Kseniia Temnikova>,<08/28/2024>, <Activity>
# ------------------------------------------------------------------------------------------ #

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.strip().split(',')
        student_dictionary={'First name':student_data[0], 'Last name':student_data[1], 'Course':student_data[2]}
        # Load it into our collection (list of lists)
        students.append(student_dictionary)
    file.close()
except Exception as e:
    print("There is an error while reading document, please fix that")
    print(e, e.__doc__)

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Name may consist of only alphabetic characters.")
        except Exception as e:
            print("There is an error during entering of first name, please fix that")
            print(e, e.__doc__)
            continue
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Name may consist of only alphabetic characters.")
        except Exception as e:
            print("There is an error during entering of last name, please fix that")
            print(e, e.__doc__)
            continue
        course_name = input("Please enter the name of the course: ")
        student_data = {'First name':student_first_name, 'Last name':student_last_name, 'Course':course_name}
        students.append(student_data)
        for student in students:
            print(f"You have registered {student['First name']} {student['Last name']} for {student['Course']}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['First name']} {student['Last name']} is enrolled in {student['Course']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            csv_data = ''
            for student in students:
                csv_data += f"{student['First name']},{student['Last name']},{student['Course']}\n"
            file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['First name']} {student['Last name']} is enrolled in {student['Course']}")
        except Exception as e:
            print("There is an error when the dictionary rows are written to the file, please fix that")
            print(e, e.__doc__)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
