# NAME: ADAM TIOVA BUDHIHARJO
# CLASS: JCDSOL - 14 - 02

student = [
    {
        'Name': 'Mika',
        'StudentID': 111,
        'Test1': 88,
        'Test2': 65,
        'Assignment': 90,
        'Final': 60,
        'Examfee': True,
    },
    {
        'Name': 'Miki',
        'StudentID': 112,
        'Test1': 55,
        'Test2': 35,
        'Assignment': 100,
        'Final': 95,
        'Examfee': True,
    },
    {
        'Name': 'Miku',
        'StudentID': 113,
        'Test1': 88,
        'Test2': 65,
        'Assignment': 90,
        'Final': 60,
        'Examfee': True,
    }
]

def add(student):
    while True:
        try:
            print("\nAdd Student:")
            name = input("Enter student name (or 'exit' to return to main menu): ")
            if name.lower() == 'exit':
                break
            
            if any(data['Name'] == name for data in student):
                print(f"Student with the name '{name}' already exists.")
                continue

            student_id = input("Enter student ID: ")
            test1 = float(input("Enter Test 1 score: "))
            test2 = float(input("Enter Test 2 score: "))
            assignment = float(input("Enter Assignment score: "))
            final = float(input("Enter Final score: "))
            examfee = input("Enter Exam Fee status (paid/not paid): ").strip().lower() == 'paid'

            new_student = {
                "Name": name,
                "StudentID": student_id,
                "Test1": test1,
                "Test2": test2,
                "Assignment": assignment,
                "Final": final,
                "Examfee": examfee
            }

            print("Student to be added:", new_student)
            save = input("Save this student? (yes/no): ").lower()
            if save == 'yes':
                student.append(new_student)
                print("Student added.")
            else:
                print("Student not added.")

            return student
        except ValueError:
            print ('Input error. Please try again')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")

def read(student):
    if not student:
        print("No data available.")
        return

    while True:
        try:    
            print("""\nWelcome to the Read menu. Please press:
                1 to display all current data
                2 to display filtered data
                3 to display average of all students
                4 to exit to main menu \n""")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print("All data:")
                headers = ["Name", "StudentID", "Test1", "Test2", "Assignment", "Final", "Examfee"]
                print(f"{headers[0]:<10}{headers[1]:<10}{headers[2]:<6}{headers[3]:<6}{headers[4]:<11}{headers[5]:<6}{headers[6]:<8}")
                print("-" * 60)
                for item in student:
                    name = item.get('Name', 'N/A')
                    student_id = item.get('StudentID', 'N/A')
                    test1 = item.get('Test1', 'N/A')
                    test2 = item.get('Test2', 'N/A')
                    assignment = item.get('Assignment', 'N/A')
                    final = item.get('Final', 'N/A')
                    examfee = "Paid" if item.get('Examfee', False) else "Not Paid"
                    print(f"{name:<10}{student_id:<10}{test1:<6}{test2:<6}{assignment:<11}{final:<6}{examfee:<8}")
                print("\n")
                
                ask1 = input('Do you want to check another student data?')
                if ask1.lower() == 'no':
                    break

            elif choice == '2':
                key = input("Enter the key to filter (e.g., Name, StudentID, Test1, Test2, Assignment, Final, Examfee): ")
                operator = input('Enter comparison operator: (>, <, >=, <=, ==) (Press enter to skip if value is string)')
                if operator == '':
                    operator = "=="
                value = input(f"Enter the value for {key} to filter: ")
                print(f"Filtered data for {key} > {value}:")

                headers = ["Name", "StudentID", "Test1", "Test2", "Assignment", "Final", "Examfee"]
                print(f"{headers[0]:<10}{headers[1]:<10}{headers[2]:<6}{headers[3]:<6}{headers[4]:<11}{headers[5]:<6}{headers[6]:<8}")
                print("-" * 60)
                
                try:
                    if operator in ['>', '<', '>=', '<=',]:
                        filter_value = float(value)
                    else:
                        filter_value = value
                except ValueError:
                    filter_value = value

                for item in student:
                    try:
                        if key in item:
                            item_value = item[key]
                            if type(item_value) in [int, float] and type(filter_value) in [int, float]:
                                if eval(f"item_value {operator} filter_value"):
                                    print(f"{item['Name']:<10}{item['StudentID']:<10}{item['Test1']:<6}{item['Test2']:<6}{item['Assignment']:<11}{item['Final']:<6}{'Paid' if item['Examfee'] else 'Not Paid':<8}")
                            elif type(item_value) is str and type(filter_value) is str:
                                if eval(f"item_value.lower() {operator} filter_value.lower()"):
                                    print(f"{item['Name']:<10}{item['StudentID']:<10}{item['Test1']:<6}{item['Test2']:<6}{item['Assignment']:<11}{item['Final']:<6}{'Paid' if item['Examfee'] else 'Not Paid':<8}")
                    except (ValueError, TypeError):
                        continue
                print('\n')
                ask2 = input('Do you want to check another student data?')
                if ask2.lower() == 'no':
                    break

            elif choice == '3':
                print("Calculating..")
                headers = ["Test1", "Test2", "Assignment", "Final"]
                for key in headers:
                    values = []
                    for item in student:
                        if key in item:
                            try:
                                value = float(item[key])
                                values.append(value)
                            except ValueError:
                                pass
                    if values:
                        avg = sum(values) / len(values)
                        print(f"Average score for {key}: {avg:.2f}")
                    else:
                        print(f"No numeric values found for {key}")
                print("\n")

                ask3 = input('Do you want to check another student data?: ')
                if ask3.lower() == 'no':
                    break 

            elif choice == '4':
                print("\nExiting read menu\n.")
                break

            else:
                print("\nPlease enter a number from 1-4.\n")
        except ValueError:
            print ('Input type error. Please try again')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")

def edit(student):
    while True:
        try:
            name = input("Enter the name of the student to edit (or 'exit' to return to the main menu): ")
            if name.lower() == 'exit':
                break

            normalized_name = name.capitalize()
            matching_students = []

            for stu in student:
                if stu['Name'].lower() == normalized_name.lower():
                    matching_students.append(stu)

            if not matching_students:
                print(f"Student with the name '{name}' not found.")
                continue

            if len(matching_students) > 1:
                print("Multiple students found with that name:")
                for i, stu in enumerate(matching_students):
                    print(f"{i + 1}. Name: {stu['Name']}, StudentID: {stu['StudentID']}")
                choice = int(input("Enter the number corresponding to the student you want to edit: ")) - 1
                student_to_edit = matching_students[choice]
            else:
                student_to_edit = matching_students[0]

            student_to_edit_index = student.index(student_to_edit)
            print("Current data:", student_to_edit)

            for key in ['Name', 'StudentID', 'Test1', 'Test2', 'Assignment', 'Final', 'Examfee']:
                change_value = input(f"Do you want to change {key}? (yes/no): ").lower()
                if change_value == 'yes':
                    new_value = input(f"Enter new value for {key}: ")
                    if new_value:
                        if key in ['Test1', 'Test2', 'Assignment', 'Final']:
                            student_to_edit[key] = float(new_value)
                        elif key == 'Name':
                            student_to_edit[key] = new_value.capitalize()
                        elif key == 'Examfee':
                            student_to_edit[key] = new_value.lower() in ['true', 'yes', '1']
                        else:
                            student_to_edit[key] = int(new_value) if key == 'StudentID' else new_value

            save = input("Save changes? (yes/no): ").lower()
            if save == 'yes':
                student[student_to_edit_index] = student_to_edit
                print("=" * 10 + "\nChanges saved.\n" + "=" * 10)
            else:
                print("Changes discarded. No updates made.")
        except ValueError:
            print('Input type error. Please enter a valid number.')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")

def delete(student):
    while True:
        try:    
            name = input("Enter the name of the student to delete (or 'exit' to return to the main menu): ")
            if name.lower() == 'exit':
                break

            student_to_delete = None
            for item in student:
                if item['Name'].lower() == name.lower():
                    student_to_delete = item
                    break

            if student_to_delete:
                confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").lower()
                if confirm == 'yes':
                    student.remove(student_to_delete)
                    print(f"Student {name} has been deleted.")
                else:
                    print("Delete operation cancelled.")
            else:
                print(f"Student with the name '{name}' not found.")

            return student
        except ValueError:
            print ('Input type error. Please try again.')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")

def finalscore(student):
    while True:
        try:
            print("Calculating...\n")
            headers = ["Name", "StudentID", "Test1", "Test2", "Assignment", "Final", "Examfee", "Grade", "Letter Grade", "Pass/Fail", "Paid/Not Paid", "Eligibility"]
            print(f"{headers[0]:<10}{headers[1]:<10}{headers[2]:<6}{headers[3]:<6}{headers[4]:<11}{headers[5]:<6}{headers[6]:<8}{headers[7]:<6}{headers[8]:<15}{headers[9]:<10}{headers[10]:<15}{headers[11]:<12}")
            print("=" * 135)
            for item in student:
                name = item.get('Name', 'N/A')
                student_id = item.get('StudentID', 'N/A')
                test1 = item.get('Test1', 0)
                test2 = item.get('Test2', 0)
                assignment = item.get('Assignment', 0)
                final = item.get('Final', 0)
                examfee = "Paid" if item.get('Examfee', False) else "Not Paid"
                total_score = 0.15 * test1 + 0.15 * test2 + 0.30 * assignment + 0.40 * final
                grade_score = round(total_score)
                if grade_score < 50:
                    letter_grade = 'F'
                    pass_fail = 'Fail'
                elif 50 <= grade_score < 60:
                    letter_grade = 'D'
                    pass_fail = 'Fail'
                elif 60 <= grade_score < 70:
                    letter_grade = 'C'
                    pass_fail = 'Fail'
                elif 70 <= grade_score < 80:
                    letter_grade = 'B'
                    pass_fail = 'Pass'
                elif 80 <= grade_score < 90:
                    letter_grade = 'A'
                    pass_fail = 'Pass'
                else:
                    letter_grade = 'A+'
                    pass_fail = 'Pass'
                eligibility = 'Eligible' if pass_fail == 'Pass' and examfee == 'Paid' else 'Not Eligible'
                
                print(f"{name:<10}{student_id:<10}{test1:<6}{test2:<6}{assignment:<11}{final:<6}{examfee:<8}{grade_score:<6}{letter_grade:<15}{pass_fail:<10}{examfee:<15}{eligibility:<12}")
            print("\n")
            askf = input('Press 1/exit/e to exit to main menu: ')
            if askf == '1' or askf.lower() == 'exit' or askf.lower() == 'e':
                break
        except ValueError:
            print ('Input type error. Please try again')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")

def main_menu():
    while True:
        try:    
            print("\nWelcome to the Student Management System. Please select an option:")
            print("1. Add a student")
            print("2. Read student data")
            print("3. Edit student data")
            print("4. Delete a student")
            print("5. Calculate final scores and eligibility")
            print("6. Exit")
            
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == '1':
                add(student)
            elif choice == '2':
                read(student)
            elif choice == '3':
                edit(student)
            elif choice == '4':
                delete(student)
            elif choice == '5':
                finalscore(student)
            elif choice == '6':
                print("Exiting the Student Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
        except ValueError:
            print("Input type error. Please select a number from 1 to 6.")
            print('To exit, plese press 6.')
        except Exception as e:
            print(f"Input error: {e}. Please try again.")
            print('To exit, plese press 6.')

main_menu()
