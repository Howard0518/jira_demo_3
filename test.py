import streamlit as st
import pandas as pd
import requests
from io import StringIO

github_csv_url = 'https://raw.githubusercontent.com/Howard0518/jira_demo_2/main/pet_owners.csv'
token = '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'
headers = {'Authorization': f'token {token}'}

response = requests.get(github_csv_url, headers=headers)

csv_data = response.content.decode('utf-8')
df = pd.read_csv(StringIO(csv_data))

st.write(df)
