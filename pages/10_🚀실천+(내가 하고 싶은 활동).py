from openai import OpenAI
import streamlit as st
import time
import random
from io import BytesIO  # 파일 다운로드를 위해 필요
import os

# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# # 페이지 제목 설정
# st.set_page_config(page_title="실천+ 내가 하고 싶은 활동")


# # 제목을 가운데 정렬
# st.markdown("<h1 style='text-align: center;'>실천+내가 하고 싶은 활동</h1>", unsafe_allow_html=True)
# st.markdown("<h3 style='text-align: center;'>덕이를 활용하여 내가 하고 싶은 인성활동을 해보세요.</h3>", unsafe_allow_html=True)


# # 1, 2, 3번 항목을 나란히 배치
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#         <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
#             <h3 style="margin: 0;">예시 1) 인성 동화책 만들기</h3>
#             <p>- 생각 더하기 이미지 생성 활용</p>
#         </div>
#     """, unsafe_allow_html=True)


# with col1:
#     st.markdown("""
#         <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
#             <h3 style="margin: 0;font size=15px">예시1) 인성 동화책 만들기</h3>
#             <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EF%B8%8F%EC%83%9D%EA%B0%81+(%EC%9D%B4%EB%AF%B8%EC%A7%80_%EC%83%9D%EC%84%B1)" target="_blank">생각 더하기 이미지 생성 활용</a></p>
#         </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#         <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
#             <h3 style="margin: 0;">예시 2) 인성 동요 만들기</h3>
#               <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EB%A7%88%EC%9D%8C+(%EB%85%B8%EB%9E%98_%EB%A7%8C%EB%93%A4%EA%B8%B0)" target="_blank">- 마음+ 노래 만들기 활용</p>
#         </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#         <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 10px; border-radius: 10px; height: 200px;">
#             <h3 style="margin: 0;">예시 3) 인성 퀴즈 만들기</h3>
#               <p>- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EC%8B%A4%EC%B2%9CAI" target="_blank">- 실천AI 활용</p>
#         </div>
#     """, unsafe_allow_html=True)


st.set_page_config(page_title="실천+내가 하고 싶은 활동", layout="wide")

# 제목을 가운데 정렬
st.markdown("<h1 style='text-align: center;'>실천+내가 하고 싶은 활동</h1>", unsafe_allow_html=True)

# 부제목을 가운데 정렬
st.markdown("<h3 style='text-align: center;'>덕이를 활용하여 내가 하고 싶은 인성활동을 해보세요.</h3>", unsafe_allow_html=True)

# 1, 2, 3번 항목을 나란히 배치
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 20px; border-radius: 10px; width: 100%;">
            <h3 style="margin: 0; font-size: 18px;">예시 1) 인성 동화책 만들기</h3>
            <p style="font-size: 14px;">- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EF%B8%8F%EC%83%9D%EA%B0%81+(%EC%9D%B4%EB%AF%B8%EC%A7%80_%EC%83%9D%EC%84%B1)" target="_blank">생각 더하기 이미지 생성 활용</a></p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 20px; border-radius: 10px; width: 100%;">
            <h3 style="margin: 0; font-size: 18px;">예시 2) 인성 동요 만들기</h3>
            <p style="font-size: 14px;">- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EB%A7%88%EC%9D%8C+(%EB%85%B8%EB%9E%98_%EB%A7%8C%EB%93%A4%EA%B8%B0)" target="_blank">마음+ 노래 만들기 활용</a></p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="background-color: #f8f8f8; padding: 20px; margin-bottom: 20px; border-radius: 10px; width: 100%;">
            <h3 style="margin: 0; font-size: 18px;">예시 3) 인성 퀴즈 만들기</h3>
            <p style="font-size: 14px;">- <a href="https://mtde7t3hvcz7afhxqgnnct.streamlit.app/%EC%8B%A4%EC%B2%9CAI" target="_blank">실천AI 활용</a></p>
        </div>
    """, unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center;font-size: 18px'>예시4) 인성 광고 영상 만들기</h3>", unsafe_allow_html=True)


# 덕목 드롭다운
virtues = ["예절", "효", "정직", "책임", "존중", "배려", "소통", "협동"]
virtue = st.selectbox("가치덕목", virtues)

# 인성 스토리 입력 창
story = st.text_area("인성을 주제로 한 스토리를 입력하세요")

@st.cache_data  # st.experimental_memo 대신 st.cache_data 사용
def generate_story(virtue, story):
    persona = f'''
    이 프롬프트는 사용자로부터 제공된 가치덕목과 인성 스토리를 바탕으로 인성 광고 영상 스토리를 제작하는 GPT 모델입니다. 스토리를 입력하면 동영상에 대한 묘사를 해주세요. 아주 짧은 형식의 광고영상을 만들겁니다. 사용자가 제공한 내용이 현실에 맞지 않거나 사실에 맞느 않은 경우 gtp가 수정해서 작성합니다. 인성광고스토리를 작성한 다음 https://lumalabs.ai/dream-machine
 사이트를 이용하도록 링크를 걸어주세요.
    다음은 사용자가 제공한 내용입니다:
    가치덕목: {virtue}
    인성 스토리: {story}
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": "위 내용을 바탕으로 인성 광고 영상 스토리를 작성해 주세요."}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    return response.choices[0].message.content

# 결과 분석 및 피드백
if st.button("인성 광고 영상 스토리 생성"):
    if virtue and story:
        generated_story = generate_story(virtue, story)
        st.markdown("## 인성 광고 영상 스토리")
        st.write(generated_story)
    else:
        st.error("가치덕목과 인성 스토리를 모두 입력해 주세요.")
