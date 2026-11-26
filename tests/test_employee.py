import pytest

from employee_management.employee import EmployeeManager


@pytest.fixture
def manager(tmp_path):
    db_path = tmp_path / "test_employees.db"
    return EmployeeManager(str(db_path))


def test_add_employee(manager):
    employee_id = manager.add_employee(
        "John",
        "john@example.com",
        "IT",
        50000
    )

    assert employee_id > 0


def test_get_all_employees(manager):
    manager.add_employee(
        "John", "john@example.com", "IT", 50000
    )

    employees = manager.get_all_employees()

    assert len(employees) == 1
    assert employees[0][1] == "John"


def test_get_employee(manager):
    employee_id = manager.add_employee(
        "David", "david@example.com", "HR", 40000
    )

    employee = manager.get_employee(employee_id)

    assert employee is not None
    assert employee[1] == "David"


def test_update_employee(manager):
    employee_id = manager.add_employee(
        "John", "john@example.com", "IT", 50000
    )

    manager.update_employee(
        employee_id,
        "John Smith",
        "johnsmith@example.com",
        "Finance",
        60000
    )

    employee = manager.get_employee(employee_id)

    assert employee[1] == "John Smith"
    assert employee[3] == "Finance"
    assert employee[4] == 60000


def test_delete_employee(manager):
    employee_id = manager.add_employee(
        "John", "john@example.com", "IT", 50000
    )

    result = manager.delete_employee(employee_id)

    assert result is True
    assert manager.get_employee(employee_id) is None


def test_invalid_email(manager):
    with pytest.raises(ValueError):
        manager.add_employee(
            "John", "invalid-email", "IT", 50000
        )


def test_invalid_salary(manager):
    with pytest.raises(ValueError):
        manager.add_employee(
            "John", "john@example.com", "IT", -1000
        )


def test_empty_name(manager):
    with pytest.raises(ValueError):
        manager.add_employee(
            "", "john@example.com", "IT", 50000
        )


def test_duplicate_email(manager):
    manager.add_employee(
        "John", "john@example.com", "IT", 50000
    )

    with pytest.raises(Exception):
        manager.add_employee(
            "David", "john@example.com", "HR", 40000
        )


def test_employee_not_found(manager):
    employee = manager.get_employee(999)

    assert employee is None
