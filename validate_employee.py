import csv

with open('data/employee.csv', newline='') as file:
    data = csv.DictReader(file)

    for row_number, row in enumerate(data, start = 2):
        # print(row_number, row)
        employee_id = row['id']
        salary = row['salary']

        if not employee_id:
            raise ValueError('employee_id is missing at row ', row_number)

# in csv file by default datatype is string / dictionary so salary < 0 will throw an error

        if float(salary) < 0: 
            raise ValueError('Salary is negative at row ', row_number)

    print('Validated')