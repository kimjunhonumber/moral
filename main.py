# main.py
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
    "1_생각.py": "1. 생각AI",
    "1.1_생각+(생각의_힘).py": "1.1 생각+(생각의 힘)",
    "1.2_생각+(이미지_생성).py": "1.2 생각+(이미지 생성)",
    "2.1_마음+(배우고_싶은_점).py": "2.1 마음+(배우고 싶은 점)",
    "2.2_마음+(짧은_문장).py": "2.2 마음+(짧은 문장)",
    "2.3_마음+(노래).py": "2.3 마음+(노래)",
    "3_마음AI.py": "3. 마음AI",
    "3_실천AI.py": "3. 실천AI",
    "3.1_실천+(계획세우기).py": "3.1 실천+(계획세우기)"
}

# 사이드바에 페이지 이름 표시
for page in sorted(page_names.keys()):
    st.sidebar.write(f"[{page_names[page]}](?page={page})")

# 쿼리 스트링에서 페이지 정보 가져오기
query_params = st.experimental_get_query_params()
selected_page = query_params.get("page", ["1_생각.py"])[0]

# 선택된 페이지 파일 실행
if selected_page in pages:
    exec(open(os.path.join(PAGES_DIR, selected_page), encoding="utf-8").read())
else:
    st.write("페이지를 찾을 수 없습니다.")

