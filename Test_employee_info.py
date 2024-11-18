import employee_info

def test_get_employees_by_age_range():
    # Define a sample range and calculate expected results manually
    age_lower_limit = 25
    age_upper_limit = 35
    expected_employees = [
        item for item in employee_info.employee_data 
        if age_lower_limit < item["age"] < age_upper_limit
    ]
    assert employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit) == expected_employees


def test_calculate_average_salary():
    total_salary= sum(item['salary'] for item in employee_info.employee_data)
    test_average= total_salary/ len(employee_info.employee_data)

    assert test_average== employee_info.calculate_average_salary()


def test_get_employees_by_dept():
    # Test with department "Marketing"
    department = "Marketing"
    expected_employees = [
        item for item in employee_info.employee_data 
        if item["department"].lower() == department.lower()
    ]
    assert employee_info.get_employees_by_dept(department) == expected_employees




