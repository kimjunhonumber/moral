import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# 이미지 로드 함수
def load_image(img_path):
    try:
        image = Image.open(img_path)
        return image
    except FileNotFoundError:
        st.error(f"해당 파일을 찾을 수 없습니다: {img_path}")
        return None

# 이미지 URL 변환 함수
def image_to_base64(img_path):
    image = Image.open(img_path)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def image_to_html(img_path, link):
    img_base64 = image_to_base64(img_path)
    img_html = f'<a href="{link}"><img src="data:image/png;base64,{img_base64}" width="100%"></a>'
    return img_html

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

# 컬럼으로 레이아웃 구성
# 1행
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # 파란색 막대 안에 글을 넣는 HTML 코드
html_code = """
<div style="background-color:#4169E1; padding: 10px; border-radius: 10px; text-align:center; color: white; width: 100%;">
    <h3 style="margin: 0;">생각AI</h3>
</div>
"""

# HTML 코드를 Streamlit에 표시
st.markdown(html_code, unsafe_allow_html=True)

    # st.markdown('<div style="background-color:#4169E1; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    # st.markdown('<h3 style="text-align:center;">생각AI</h3>', unsafe_allow_html=True)
    # img_html = image_to_html('images/생각이.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%83%9D%EA%B0%81AI')
    # st.markdown(img_html, unsafe_allow_html=True)
    # st.markdown('<p style="text-align:center;">덕목의 의미    <br>갈등 상황</p>', unsafe_allow_html=True)
    # st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background-color:#87CEEB; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/상황생각하기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%83%9D%EA%B0%81+(%EC%83%9D%EA%B0%81%EC%9D%98_%ED%9E%98)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;"> 아는 힘, 생각하는 힘,    <br> 마음의 힘, 행동의 힘</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div style="background-color:#87CEEB; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">생각+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/이미지생성.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%83%9D%EA%B0%81+(%EC%9D%B4%EB%AF%B8%EC%A7%80_%EC%83%9D%EC%84%B1)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">이야기에 어울리는  <br> 이미지 만들기 </span> </p>', unsafe_allow_html=True) 
    st.markdown('</div>', unsafe_allow_html=True)

# 2행
col4, col5, col6, col7 = st.columns([1, 1, 1, 1])

with col4:
    st.markdown('<div style="background-color:#DC143C ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음AI</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/마음이.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EB%A7%88%EC%9D%8CAI')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">나라면 어떻게?, 공감하는 방법, 고민해결 하기</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div style="background-color:#FA8072   ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/반성하기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EB%A7%88%EC%9D%8C+(%EB%B0%B0%EC%9A%B0%EA%B3%A0_%EC%8B%B6%EC%9D%80%EC%A0%90)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">배우고 싶은 점과  <br>부족한 점</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div style="background-color:#FA8072  ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/마음문장만들기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EB%A7%88%EC%9D%8C+(%EC%A7%A7%EC%9D%80%EB%AC%B8%EC%9E%A5)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">짧은 문장 만들기 <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col7:
    st.markdown('<div style="background-color:#FA8072  ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">마음+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/가사추천하기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EB%A7%88%EC%9D%8C+(%EB%85%B8%EB%9E%98_%EB%A7%8C%EB%93%A4%EA%B8%B0)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">노래 만들기    <br> <span style="color:rgba(0,0,0,0);"> 이미지 생성 </span> </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

# 3행
col8, col9, col10 = st.columns([1, 1, 1])

with col8:
    st.markdown('<div style="background-color:#32CD32 ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천AI</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/실천이.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%8B%A4%EC%B2%9CAI')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">덕목 실천방법, <br>실천의 좋은 점</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col9:
    st.markdown('<div style="background-color:#90EE90 ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/실천계획세우기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%8B%A4%EC%B2%9C+(%EA%B3%84%ED%9A%8D%EC%84%B8%EC%9A%B0%EA%B8%B0)')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">실천 <br> 놀이터 </p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

with col10:
    st.markdown('<div style="background-color:#90EE90 ; padding: 10px; border-radius: 10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;">실천+</h3>', unsafe_allow_html=True)
    img_html = image_to_html('images/실천의지키우기.png', 'https://2gaeyouhl8fwhqotlwa9uz.streamlit.app/%EC%8B%A4%EC%B2%9CAI')
    st.markdown(img_html, unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">실천 의지    <br>키우기</p>', unsafe_allow_html=True)  # 공백을 추가하여 두 줄로 표현
    st.markdown('</div>', unsafe_allow_html=True)

