import sqlite3
import random

# Connect to SQLITE
connection = sqlite3.connect("student.db")

# Create a cursor object to insert recort and crate table
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Insert records
# For scalable use, we can use panda to import .csv files 
# and process the data into the database

classes = ['Ai', 'Data Science', 'Math', 'Algorithms']
sections = ['A', 'B', 'C', 'D']

first_names = ["Dinuk", "Daniel", "Sonny", "Hadii", "Alex", "Jamie", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Reese", "Quinn", "Skyler", "Rowan", "Dakota", "Peyton", "Drew"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris"]

random_names = [random.choice(first_names) + " " + random.choice(last_names) for _ in range(50)]

for i in range(0, 50):

    name = random_names[i]
    selected_class = random.choice(classes)
    selected_section = random.choice(sections)

    sql = f"INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('{name}', '{selected_class}', '{selected_section}')"
    cursor.execute(sql)


print("The inserted records are")

data = cursor.execute('''Select * from STUDENT ''')
for row in data:
    print(row)

connection.commit()
connection.close()
