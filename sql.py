from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure genAI key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Load Google Gemini Model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt, question])  # Pass the combined string
    return response.text


# Function to query from database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# Define your prompt
prompt = """

Imagine you are a highly skilled database consultant tasked with transforming natural language questions into precise SQL queries. Your current project involves a database named 'student_db', structured with a single table named 'STUDENT'. This table is meticulously organized into three columns: NAME (a VARCHAR(25) holding the student's name), CLASS (a VARCHAR(25) indicating the class in which the student is enrolled), and SECTION (a VARCHAR(25) detailing the section of the class).

Your role is to facilitate seamless interaction with 'student_db' for users unfamiliar with SQL. They will pose questions in English, and you will provide the corresponding SQL queries to retrieve the desired information from the STUDENT table. The queries you generate should adhere strictly to SQL syntax, excluding the use of backticks (`) or the word 'sql' within the output.

Below are several examples of questions you might receive, along with the correct SQL query that should result from each:

1. "How many students are currently enrolled in the database?"
   - Correct SQL Query: SELECT COUNT(*) FROM STUDENT;

2. "Can you list all students enrolled in the 'Data Science' class?"
   - Correct SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = 'Data Science';

3. "What are the different classes available in the database?"
   - Correct SQL Query: SELECT DISTINCT CLASS FROM STUDENT;

4. "I need to know the sections available for the 'Machine Learning' class. Can you find that for me?"
   - Correct SQL Query: SELECT DISTINCT SECTION FROM STUDENT WHERE CLASS = 'Machine Learning';

5. "Who are the students in section 'A' of the 'Web Development' class?"
   - Correct SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = 'Web Development' AND SECTION = 'A';

Remember, your responses must be syntactically correct SQL queries capable of running directly against the 'student_db'. Your expertise in interpreting the essence of each question and crafting the corresponding SQL command is crucial for enabling intuitive access to database information for all users.
Make sure you dont put ``` in the begging or end of an SQL word in the output.

"""

# Streamlit App

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If sumbit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in response:
        st.header(row)
