import streamlit as st
import pandas as pd
from datetime import datetime
import openpyxl
import io  # io 모듈 임포트

# 엑셀 파일 경로 설정
EXCEL_FILE = 'moral_actions.xlsx'

# 기존 데이터 불러오기
def load_data():
    try:
        return pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Moral Action"])

# 데이터 저장하기
def save_data(df):
    df.to_excel(EXCEL_FILE, index=False)

# 데이터 추가하기
def add_data(date, action):
    df = load_data()
    new_data = pd.DataFrame({"Date": [date], "Moral Action": [action]})
    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df)
    return df

# 기존 데이터 불러오기
data = load_data()

# Streamlit UI 구성
st.title('나의 도덕 실천 놀이터')

st.write("오늘 내가 한 도덕 실천은?")
action = st.text_area("도덕 실천 내용", "")

if st.button("기록"):
    if action:
        current_date = datetime.now().strftime("%Y-%m-%d")
        data = add_data(current_date, action)
        st.success("기록이 저장되었습니다.")
    else:
        st.error("도덕 실천 내용을 입력하세요.")

# 기록된 데이터 표시하기
st.write("기록된 도덕 행위들:")
st.dataframe(data)

# 엑셀 파일 다운로드 링크 제공하기
def to_excel(df):
    output = io.BytesIO()  # io.BytesIO() 사용
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()  # writer.save() 대신 writer.close() 사용
    processed_data = output.getvalue()
    return processed_data

st.download_button(
    label="엑셀 파일로 다운로드",
    data=to_excel(data),
    file_name='moral_actions.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)
