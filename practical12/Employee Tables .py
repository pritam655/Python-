import pandas as pd

# Employee Table
emp = pd.DataFrame({
    "EMPNO": ["E101", "E102", "E103", "E105", "E106"],
    "EMP_NAME": ["Vivek", "Vishal", "Priyal", "Shrushti", "Pranay"],
    "DEPT_NAME": ["R&D", "Marketing", "Product Development", "Product Development", "Product Development"],
    "SALARY": [145000, 90000, 120000, 80000, 100000],
    "DOJ": ["2019-06-11", "2012-03-15", "2018-07-20", "2019-09-19", "2018-10-22"],
    "BRANCH": ["Nagpur", "Pune", "Bangalore", "Nagpur", "Mumbai"]
})

# Designation Table
designation = pd.DataFrame({
    "EMPNO": ["E101", "E102", "E103", "E105", "E106"],
    "DESIGNATION": ["Project Manager", "Sales Manager", "Design Architect", "Software Developer", "Project Lead"]
})

# Merge both tables
emp_data = pd.merge(emp, designation, on="EMPNO")

print("\nMerged Employee Table:")
print(emp_data)

# Operations
print("\nEmployees from Product Development:")
print(emp_data[emp_data["DEPT_NAME"] == "Product Development"])

print("\nEmployees with salary > 100000:")
print(emp_data[emp_data["SALARY"] > 100000])