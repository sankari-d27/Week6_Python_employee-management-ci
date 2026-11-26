from employee_management.employee import EmployeeManager


def main():
    manager = EmployeeManager()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Employee Name: ")
                email = input("Email: ")
                department = input("Department: ")
                salary = float(input("Salary: "))

                employee_id = manager.add_employee(
                    name, email, department, salary
                )

                print("Employee added successfully!")
                print("Employee ID:", employee_id)

            elif choice == "2":
                employees = manager.get_all_employees()

                for employee in employees:
                    print(employee)

                if not employees:
                    print("No employees found.")

            elif choice == "3":
                employee_id = int(input("Enter Employee ID: "))
                employee = manager.get_employee(employee_id)

                if employee:
                    print(employee)
                else:
                    print("Employee not found.")

            elif choice == "4":
                employee_id = int(input("Enter Employee ID: "))

                if manager.delete_employee(employee_id):
                    print("Employee deleted successfully!")
                else:
                    print("Employee not found.")

            elif choice == "5":
                print("Thank you!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Error:", error)
        except Exception as error:
            print("Operation failed:", error)


if __name__ == "__main__":
    main()
