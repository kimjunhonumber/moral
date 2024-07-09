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
    st.secrets["gsheets"], scopes=scope)
client = gspread.authorize(credentials)

# Google Sheets URL 또는 ID
SPREADSHEET_URL = st.secrets["spreadsheet_url"]

# Google Sheets 열기
spreadsheet = client.open_by_url(SPREADSHEET_URL)
worksheet = spreadsheet.sheet1

# Streamlit 애플리케이션
st.title("인성 행동 실천 기록")

name = st.text_input("이름")
date = st.date_input("날짜")
age = st.number_input("나이", min_value=0, max_value=120)
virtues = ["예절", "효", "정직", "책임", "존중", "배려", "소통", "협동"]
virtue = st.selectbox("가치덕목", virtues)
action = st.text_area("실천한 일")
thought = st.text_area("실천하며 느낀 점")

if st.button("제출"):
    if name and date and virtue and action and thought:
        # 입력된 데이터를 Google Sheets에 추가
        worksheet.append_row([str(date), name, age, virtue, action, thought])
        st.success("데이터가 성공적으로 제출되었습니다!")
    else:
        st.error("모든 필드를 입력해 주세요.")

