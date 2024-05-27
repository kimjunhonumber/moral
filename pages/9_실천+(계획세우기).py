import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 제목 설정
st.set_page_config(page_title="도덕성 활동 기록")

# 제목
st.title("도덕성 활동 기록")

# 데이터 입력 양식
st.markdown("## 오늘의 도덕 활동을 기록하세요")

# 데이터 입력
date = st.date_input("날짜")
virtue = st.text_input("덕목")
action = st.text_area("한 일")
thought = st.text_area("느낀 점")

# 입력 데이터를 저장할 데이터프레임 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['날짜', '덕목', '한 일', '느낀 점'])

# 입력 버튼 클릭 시 데이터 저장
if st.button("입력"):
    new_data = {'날짜': date, '덕목': virtue, '한 일': action, '느낀 점': thought}
    st.session_state.data = st.session_state.data.append(new_data, ignore_index=True)
    st.write("데이터가 저장되었습니다.")

# 저장된 데이터 표시
st.markdown("## 저장된 도덕 활동 기록")
st.write(st.session_state.data)

# 덕목별 데이터 개수를 막대그래프로 표시
if not st.session_state.data.empty:
    count_data = st.session_state.data['덕목'].value_counts()

    fig, ax = plt.subplots()
    count_data.plot(kind='bar', ax=ax)
    ax.set_title("덕목별 도덕 활동 횟수")
    ax.set_xlabel("덕목")
    ax.set_ylabel("횟수")

    st.pyplot(fig)

