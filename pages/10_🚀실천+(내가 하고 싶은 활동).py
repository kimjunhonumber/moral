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

# 페이지 제목 설정
st.set_page_config(page_title="인성 교육 예시")

# 제목을 가운데 정렬
st.markdown("<h1 style='text-align: center;'>인성 교육 예시</h1>", unsafe_allow_html=True)

# 예시 1
st.markdown("""
    <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px;">
        <h3 style="margin: 0;">예시 1) 인성 동화책 만들기</h3>
        <p>- 생각 더하기 이미지 생성 활용</p>
    </div>
""", unsafe_allow_html=True)

# 예시 2
st.markdown("""
    <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px;">
        <h3 style="margin: 0;">예시 2) 인성 동요 만들기</h3>
        <p>- 마음+ 노래 만들기 활용</p>
    </div>
""", unsafe_allow_html=True)

# 예시 3
st.markdown("""
    <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px;">
        <h3 style="margin: 0;">예시 3) 인성 퀴즈 만들기</h3>
        <p>- 실천AI 활용</p>
    </div>
""", unsafe_allow_html=True)

# 예시 4
st.markdown("""
    <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px;">
        <h3 style="margin: 0;">예시 4) 인성 광고 영상 만들기</h3>
    </div>
""", unsafe_allow_html=True)
