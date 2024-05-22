import streamlit as st
import os

# Streamlit 페이지 제목 설정
st.set_page_config(page_title="덕이(AI)에게 물어보세요")

# 사이드바 제목
st.sidebar.title("메뉴")

# 페이지 파일 경로
PAGES_DIR = "pages"

# 페이지 파일 목록 가져오기
pages = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith('.py')])

# 페이지 이름 딕셔너리 생성
page_names = {
    "1_생각.py": "생각AI",
    "2_이미지_생성.py": "이미지 생성",
    "3_배우고_싶은_점.py": "배우고 싶은 점",
    "4_짧은_문장.py": "짧은 문장",
    "5_노래_만들기.py": "노래 만들기"
}

# 사이드바에 페이지 이름 표시
for page in pages:
    st.sidebar.markdown(f"[{page_names[page]}]({page})", unsafe_allow_html=True)

# 현재 선택된 페이지 파일
selected_file = st.sidebar.radio("페이지를 선택하세요", pages, format_func=lambda x: page_names[x])

# 선택된 페이지 파일 실행
exec(open(os.path.join(PAGES_DIR, selected_file)).read())
