import streamlit as st
from PIL import Image
import base64

# 이미지 로드 함수
def load_image(img_path):
    try:
        image = Image.open(img_path)
        return image
    except FileNotFoundError:
        st.error(f"해당 파일을 찾을 수 없습니다: {img_path}")
        return None

# 이미지 Base64 인코딩 함수
def get_image_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

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

# 컬럼으로 레이아웃 구성
# 1행
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    link = "https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%83%9D%EA%B0%81AI"
    img_path = 'images/생각이.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#ADD8E6; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">덕목의 의미    <br>도덕적 상황</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    link = "https://example.com/생각+"
    img_path = 'images/상황생각하기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#F08080; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">아는 힘, 생각하는 힘, <br>마음의 힘, 행동의 힘</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    link = "https://example.com/이미지생성"
    img_path = 'images/이미지생성.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#90EE90; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">이미지 생성    <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

# 2행
col4, col5, col6, col7 = st.columns([1, 1, 1, 1])

with col4:
    link = "https://example.com/마음AI"
    img_path = 'images/마음이.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#FFB6C1; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">나라면 어떻게?, 공감하는 방법, 고민해결</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    link = "https://example.com/마음+"
    img_path = 'images/반성하기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#FFD700; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">배우고 싶은 점과  <br>부족한 점</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    link = "https://example.com/마음문장만들기"
    img_path = 'images/마음문장만들기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#87CEFA; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">짧은 문장 만들기 <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    link = "https://example.com/가사추천하기"
    img_path = 'images/가사추천하기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#FFA07A; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">노래 만들기    <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

# 3행
col8, col9, col10 = st.columns([1, 1, 1])

with col8:
    link = "https://example.com/실천AI"
    img_path = 'images/실천이.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#98FB98; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천AI</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">나라면 어떻게?, <br>공감하는 방법 알기</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col9:
    link = "https://example.com/실천계획세우기"
    img_path = 'images/실천계획세우기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#E6E6FA; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">실천 계획  <br>세우기</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

with col10:
    link = "https://example.com/실천의지키우기"
    img_path = 'images/실천의지키우기.png'
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<a href="{link}" target="_blank"><img src="data:image/png;base64,{img_base64}" width="100%"></a>', unsafe_allow_html=True)
    st.markdown('<div style="background-color:#F0E68C; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천+</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">실천 의지    <br>키우기</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


