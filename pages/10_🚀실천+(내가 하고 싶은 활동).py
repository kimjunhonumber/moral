from openai import OpenAI
import streamlit as st
import time
import random
from io import BytesIO  # 파일 다운로드를 위해 필요
import os

# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

import streamlit as st

import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="실천+ 내가 하고 싶은 활동")


# 제목을 가운데 정렬
st.markdown("<h1 style='text-align: center;'>실천+내가 하고 싶은 활동</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>덕이를 활용하여 내가 하고 싶은 인성활동을 해보세요.</h3>", unsafe_allow_html=True)


# 1, 2, 3번 항목을 나란히 배치
col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#         <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
#             <h3 style="margin: 0;">예시 1) 인성 동화책 만들기</h3>
#             <p>- 생각 더하기 이미지 생성 활용</p>
#         </div>
#     """, unsafe_allow_html=True)


with col1:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
            <h3 style="margin: 0;font size=15px">예시1) 인성 동화책 만들기</h3>
            <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EF%B8%8F%EC%83%9D%EA%B0%81+(%EC%9D%B4%EB%AF%B8%EC%A7%80_%EC%83%9D%EC%84%B1)" target="_blank">생각 더하기 이미지 생성 활용</a></p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
            <h3 style="margin: 0;">예시 2) 인성 동요 만들기</h3>
              <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EB%A7%88%EC%9D%8C+(%EB%85%B8%EB%9E%98_%EB%A7%8C%EB%93%A4%EA%B8%B0)" target="_blank">- 마음+ 노래 만들기 활용</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
            <h3 style="margin: 0;">예시 3) 인성 퀴즈 만들기</h3>
              <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EC%8B%A4%EC%B2%9CAI" target="_blank">- 실천AI 활용</p>
        </div>
    """, unsafe_allow_html=True)

# 4번 항목을 따로 배치
st.markdown("""
    <div style="background-color: #f8f8f8; padding: 20px; margin-top: 20px; border-radius: 10px;">
        <h3 style="margin: 0;">예시 4) 인성 광고 영상 만들기</h3>
    </div>
""", unsafe_allow_html=True)
