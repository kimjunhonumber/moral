import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 제목 설정
st.set_page_config(page_title="인성 행동 실천 기록")

# 제목
st.title("인성 행동 실천 기록")

# 데이터 입력 양식
st.markdown("## 내가 실천한 오늘의 바른 인성 행동을 기록하세요.")

# 사용자 이름 입력
name = st.text_input("이름")

# 데이터 입력
date = st.date_input("날짜")

# 덕목 드롭다운
virtues = ["예절", "효", "정직", "책임", "존중", "배려", "소통", "협동"]
virtue = st.selectbox("가치덕목", virtues)

action = st.text_area("실천한 일")
thought = st.text_area("실천하며 느낀 점")

# 입력 데이터를 저장할 데이터프레임 초기화
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['이름', '날짜', '덕목', '한 일', '느낀 점'])

# 입력 버튼 클릭 시 데이터 저장
if st.button("입력"):
    if name and virtue and action and thought:
        new_data = pd.DataFrame({'이름': [name], '날짜': [date], '덕목': [virtue], '한 일': [action], '느낀 점': [thought]})
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.write("데이터가 저장되었습니다.")
    else:
        st.write("모든 필드를 입력해 주세요.")

# 저장된 데이터 표시
st.markdown("## 저장된 도덕 활동 기록")
st.write(st.session_state.data)

# 덕목별 데이터 개수를 막대그래프로 표시
if not st.session_state.data.empty:
    count_data = st.session_state.data['덕목'].value_counts().reset_index()
    count_data.columns = ['덕목', '횟수']

    # 색상 팔레트 정의
    colors = ["#FF9999", "#FFCC99", "#FFD700", "#ADFF2F", "#90EE90", "#87CEEB", "#4682B4", "#6A5ACD"]

    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(x='덕목', y='횟수', data=count_data, palette=colors)

    # 막대 위에 값 표시
    for i in range(len(count_data)):
        barplot.text(i, count_data['횟수'][i] + 0.5, count_data['횟수'][i], color='black', ha="center")

    plt.title("인성실천 활동기록")
    plt.xlabel("덕목")
    plt.ylabel("횟수")
    plt.ylim(0, count_data['횟수'].max() + 10)  # 상단 여백 추가

    st.pyplot(plt)

