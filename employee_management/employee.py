from employee_management.database import Database


class EmployeeManager:
    def __init__(self, db_name="employees.db"):
        self.db = Database(db_name)

    def add_employee(self, name, email, department, salary):
        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")

        if not department.strip():
            raise ValueError("Department cannot be empty.")

        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")

        query = """
            INSERT INTO employees
            (name, email, department, salary)
            VALUES (?, ?, ?, ?)
        """

        return self.db.execute_query(
            query, (name, email, department, salary)
        )

    def get_all_employees(self):
        query = "SELECT * FROM employees"
        return self.db.fetch_all(query)

    def get_employee(self, employee_id):
        query = "SELECT * FROM employees WHERE id = ?"
        result = self.db.fetch_all(query, (employee_id,))

        if not result:
            return None

        return result[0]

    def update_employee(
        self, employee_id, name, email, department, salary
    ):
        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")

        if not department.strip():
            raise ValueError("Department cannot be empty.")

        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")

        query = """
            UPDATE employees
            SET name = ?, email = ?, department = ?, salary = ?
            WHERE id = ?
        """

        self.db.execute_query(
            query,
            (name, email, department, salary, employee_id)
        )

        return self.db.fetch_all(
            "SELECT * FROM employees WHERE id = ?",
            (employee_id,)
        )

    def delete_employee(self, employee_id):
        query = "DELETE FROM employees WHERE id = ?"
        self.db.execute_query(query, (employee_id,))

        return self.db.fetch_all(
            "SELECT * FROM employees WHERE id = ?",
            (employee_id,)
        ) == []
