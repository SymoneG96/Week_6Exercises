def update_employee_list(hr_list):
    """Update the employee list with specified changes"""
    updated_list = []
    
    for emp in hr_list:
        emp_id, dept, name, salary = emp
        
        # Handle Mark's name change
        if name == 'Mark Blick':
            name = 'Mark Blick-Hawley'
            
        # Handle Jim's department and salary change
        if name == 'Jim Smith':
            dept = 'CS'
            salary = '60000'
            
        updated_list.append((emp_id, dept, name, salary))
    
    return updated_list

def display_employee_records(employee_list):
    """Display employee records in the specified format"""
    # Print header
    print("Employee# | DeptCode | Name | Salary")
    print("-" * 50)
    
    # Print each employee record
    for emp in employee_list:
        emp_id, dept, name, salary = emp
        # Convert salary to integer then format with comma
        formatted_salary = "{:,}".format(int(salary))
        print(f"{emp_id} | {dept} | {name} | {formatted_salary}")

# Original list
hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]

# Update and display the list
updated_list = update_employee_list(hr_list)
display_employee_records(updated_list)

