import streamlit as st
from streamlit_gsheets impoort GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt


import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('42607245e2b05134620d324153b73346587af820', scope)
client = gspread.authorize(creds)

# Google Sheets 문서 열기
spreadsheet = client.open("인성 행동 실천 기록")
worksheet = spreadsheet.sheet1

# 페이지 제목 설정
st.set_page_config(page_title="인성 행동 실천 기록")

# 데이터 입력 양식
st.markdown("## 내가 실천한 오늘의 바른 인성 행동을 기록하세요.")

# 사용자 이름 입력
name = st.text_input("이름")

# 데이터 입력
date = st.date_input("날짜")

# 덕목 드롭다운
virtues = ["예절", "효", "정직", "책임", "존중", "배려", "소통", "협동"]
virtue = st.selectbox("가치덕목", virtues)

# 실천한 일 입력
action = st.text_area("실천한 일")

# 실천하며 느낀 점 입력
thought = st.text_area("실천하며 느낀 점")

# 입력 데이터를 저장할 데이터프레임 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['이름', '날짜', '덕목', '한 일', '느낀 점'])

# 데이터 저장 함수
def save_data(name, date, virtue, action, thought):
    new_data = pd.DataFrame({'이름': [name], '날짜': [date], '덕목': [virtue], '한 일': [action], '느낀 점': [thought]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)

    # Google Sheets에 데이터 추가
    worksheet.append_row([name, str(date), virtue, action, thought])

# 데이터 저장 버튼
if st.button("저장"):
    save_data(name, date, virtue, action, thought)
    st.success("데이터가 성공적으로 저장되었습니다.")

# 저장된 데이터 표시
st.markdown("### 저장된 데이터")
st.dataframe(st.session_state.data)
