

employee = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

new_dict = {'name': employee['name'], 'salary': employee['salary']}

del employee['name']
del employee['salary']

print(employee)
print(new_dict)