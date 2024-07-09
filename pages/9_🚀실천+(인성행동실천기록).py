import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Streamlit 페이지 설정
st.set_page_config(page_title="인성 행동 실천 기록")

# Google Sheets API 인증
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    st.secrets["connections"]["gsheets"], scopes=scope)
client = gspread.authorize(credentials)

# Google Sheets URL 또는 ID
SPREADSHEET_URL = st.secrets["connections"]["gsheets"]["spreadsheet"]

# Google Sheets 열기
spreadsheet = client.open_by_url(SPREADSHEET_URL)
worksheet = spreadsheet.sheet1

# Streamlit 애플리케이션
st.title("인성 행동 실천 기록")

name = st.text_input("이름")
date = st.date_input("날짜")
grade = st.selectbox("학년", options=[f"{i}학년" for i in range(1, 7)])
virtues = ["예", "존중", "배려", "정직", "효", "소통", "책임", "협동"]
virtue = st.selectbox("덕목", options=virtues)action = st.text_area("실천한 일")
thought = st.text_area("느낀 점")

if st.button("제출"):
    worksheet.append_row([str(date), name, grade, virtue, action, thought])
    st.success("데이터가 성공적으로 제출되었습니다!")

