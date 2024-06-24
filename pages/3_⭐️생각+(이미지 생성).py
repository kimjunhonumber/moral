from openai import OpenAI
import streamlit as st
import time
import random
import os

# # # secrets.toml에 저장된 API 키들을 리스트로 준비
# # api_keys = [
# #     st.secrets["api_key1"],
# #     st.secrets["api_key2"],
# #     st.secrets["api_key3"],
# #     st.secrets["api_key4"],
# #     st.secrets["api_key5"],
# #     st.secrets["api_key6"]
# # ]

# # 세션 상태에서 현재 API 키를 관리
# if 'api_key' not in st.session_state:
#     # API 키를 랜덤하게 선택하여 세션 상태에 저장
#     st.session_state.api_key = random.choice(api_keys)

# client = OpenAI(api_key=st.session_state.api_key)

# # 페이지 레이아웃 설정


# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.set_page_config(layout="wide")

st.title("생각+ 이미지 생성하기")

    # 문제상황 입력
presentation_text = st.text_area("고민 상황, 가치덕목과 관련된 이야기 내용을 적어보세요.", height=300)

# 이미지 스타일 선택
image_style = st.selectbox("이미지 스타일 선택", ["사진스타일", "수채화", "미니얼 일러스트레이션","웹툰", "손그림"])

# 이미지 생성 버튼
generate_button = st.button("이미지 생성")

if generate_button and presentation_text:
    # 선택한 스타일에 따라 프롬프트 수정
    style_prompt = {
        "사진스타일": "한국적인 느낌으로 사진을 만들어줘",
        "수채화": "수채화 스타일로 이것도 한국스타일로",
        "미니멀 일러스트레이션": "미니멀 일러스트레이션 스타일로 이것도 한국스타일로",
        "웹툰": "교과서에 나오는 삽화 스타일로, 한국 도덕 초등학교 교과서 스타일로 이것도 한국 스타일로",
        "손그림":"교과서에 나오는 삽화 스타일로, 한국 도덕 초등학교 교과서 스타일로"
    }

    prompt = f"{presentation_text} {style_prompt[image_style]}"

    try:
        # OpenAI API를 호출하여 이미지 생성
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )

        # 생성된 이미지 표시
        generated_image_url = image_response.data[0].url
        st.image(generated_image_url, caption="")

        # 이미지 다운로드 버튼 생성
        st.markdown(f"[이미지 다운로드]({generated_image_url})", unsafe_allow_html=True)
    except Exception as e:
        st.error("이미지 생성 중 오류 발생: " + str(e))
