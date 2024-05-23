import streamlit as st
from PIL import Image
import os

# 이미지 로드 함수
def load_image(img_path):
    try:
        image = Image.open(img_path)
        return image
    except FileNotFoundError:
        st.error(f"해당 파일을 찾을 수 없습니다: {img_path}")
        return None

# HTML을 사용하여 이미지에 링크를 추가하는 함수
def image_with_link(image_path, link):
    st.markdown(f'<a href="?page={link}" target="_self"><img src="{image_path}" width="100%"></a>', unsafe_allow_html=True)

# 페이지 네비게이션 함수
def navigate_to(page_name):
    st.experimental_set_query_params(page=page_name)
    st.experimental_rerun()

# 스타일 추가 함수
def add_divider(color):
    st.markdown(f"<hr style='border: 3px solid {color};' />", unsafe_allow_html=True)

# 타이틀과 이미지를 나란히 배치
col1, col2 = st.columns([1, 5])

with col1:
    img_title = load_image('images/덕이.png')  # 타이틀 옆에 삽입할 이미지 경로를 지정하세요.
    if img_title:
        st.image(img_title, width=100)

with col2:
    st.title('덕이(AI)에게 물어보세요')

# 애플리케이션 소개
st.markdown("""
    ## 🌟초등학생들의 도덕학습을 위해 제작된 챗봇입니다. 
""")

# 현재 페이지 파라미터 가져오기
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["home"])[0]

# 컬럼으로 레이아웃 구성
# 1행
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("생각AI"):
        navigate_to("1_생각AI")
    st.markdown('<div style="background-color:#ADD8E6; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">덕목의 의미    <br>도덕적 상황</p>', unsafe_allow_html=True)
    image_with_link('images/생각이.png', "1_생각AI")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("생각+"):
        navigate_to("2_생각+(생각의 힘)")
    st.markdown('<div style="background-color:#F08080; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">아는 힘, 생각하는 힘, <br>마음의 힘, 행동의 힘</p>', unsafe_allow_html=True)
    image_with_link('images/상황생각하기.png', "2_생각+(생각의 힘)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    if st.button("생각+ 이미지 생성"):
        navigate_to("3_생각+(이미지 생성)")
    st.markdown('<div style="background-color:#90EE90; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">이미지 생성    <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    image_with_link('images/이미지생성.png', "3_생각+(이미지 생성)")
    st.markdown('</div>', unsafe_allow_html=True)

# 2행
col4, col5, col6, col7 = st.columns([1, 1, 1, 1])

with col4:
    if st.button("마음AI"):
        navigate_to("4_마음AI")
    st.markdown('<div style="background-color:#FFB6C1; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">나라면 어떻게?, 공감하는 방법, 고민해결</p>', unsafe_allow_html=True)
    image_with_link('images/마음이.png', "4_마음AI")
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    if st.button("마음+ 배우고 싶은 점"):
        navigate_to("5_마음+(배우고 싶은점)")
    st.markdown('<div style="background-color:#FFD700; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">배우고 싶은 점과  <br>부족한 점</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    image_with_link('images/반성하기.png', "5_마음+(배우고 싶은점)")
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    if st.button("마음+ 짧은 문장"):
        navigate_to("6_마음+(짧은문장)")
    st.markdown('<div style="background-color:#87CEFA; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">짧은 문장 만들기 <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)
    image_with_link('images/마음문장만들기.png', "6_마음+(짧은문장)")
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    if st.button("마음+ 노래 만들기"):
        navigate_to("7_마음+(노래 만들기)")
    st.markdown('<div style="background-color:#FFA07A; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">노래 만들기    <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    image_with_link('images/가사추천하기.png', "7_마음+(노래 만들기)")
    st.markdown('</div>', unsafe_allow_html=True)

# 3행
col8, col9, col10 = st.columns([1, 1, 1])

with col8:
    if st.button("실천AI"):
        navigate_to("9_실천AI")
    st.markdown('<div style="background-color:#98FB98; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">나라면 어떻게?, <br>공감하는 방법 알기</p>', unsafe_allow_html=True)
    image_with_link('images/실천이.png', "9_실천AI")
    st.markdown('</div>', unsafe.allow_html=True)

with col9:
    if st.button("실천+ 계획 세우기"):
        navigate_to("8_실천+(계획세우기)")
    st.markdown('<div style="background-color:#E6E6FA; padding: 10px; border-radius: 10px; text.align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text.align:center;">실천+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text.align:center;">실천 계획  <br>세우기</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    image_with_link('images/실천계획세우기.png', "8_실천+(계획세우기)")
    st.markdown('</div>', unsafe.allow_html=True)

with col10:
    if st.button("실천+ 의지 키우기"):
        navigate_to("8_실천+(계획세우기)")
    st.markdown('<div style="background-color:#F0E68C; padding: 10px; border-radius: 10px; text.align:center;">', unsafe.allow_html=True)
    st.markdown('<h3 style="text.align:center;">실천+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text.align:center;">실천 의지    <br>키우기</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    image_with_link('images/실천의지키우기.png', "8_실천+(계획세우기)")
    st.markdown('</div>', unsafe.allow_html=True)

# 현재 페이지 로드
if current_page != "home":
    page_path = os.path.join("pages", f"{current_page}.py")
    if os.path.exists(page_path):
        exec(open(page_path).read())
    else:
        st.error(f"Page '{current_page}' not found.")


