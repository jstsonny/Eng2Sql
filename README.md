# Eng2Sql
Gen AI to translate English to SQL Query

This model can be used in any context, changing variable names, creating new tables manually or by processing data files e.g. .csv, and the model can be further developed by writing more prompts.

If you havent already, install anaconda on your device https://www.anaconda.com/download
Open your IDE. Create an environment. In terminal, run command: 
  conda create -p venv python==<any version 3.10 or later> -y

Run Command: 
  conda activate venv/

Create .env file
Go to https://makersuite.google.com/app/apikey
Generate an API Key and paste GOOGLE_API_KEY="<apiKey>" into the .env file          

Run Command:
  python sqlite.py

Run Command:
  streamlit run sql.py

Using the localhost link, you can now ask the model any questions about the data, using keywords[
  Names,
  Classes ('Ai', 'Data Science', 'Math', 'Algorithms'),
  Sections ('A', 'B', 'C', 'D')
]

