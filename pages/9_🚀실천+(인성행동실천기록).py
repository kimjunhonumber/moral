import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API 설정
credentials = Credentials.from_service_account_file(
    'path/to/your/service_account.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
gc = gspread.authorize(credentials)

# Google Sheets 문서 열기
sh = gc.open("Your Google Sheet Name")
worksheet = sh.sheet1

# Streamlit 애플리케이션
st.title('Google Sheets Database')

name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
date = st.date_input("Date")
virtue = st.selectbox("Virtue", ["Honesty", "Respect", "Responsibility", "Kindness", "Courage"])
thoughts = st.text_area("Thoughts")

if st.button("Submit"):
    worksheet.append_row([str(date), name, age, virtue, thoughts])
    st.success("Data submitted successfully!")

if st.button("Show Data"):
    data = worksheet.get_all_records()
    st.write(data)

