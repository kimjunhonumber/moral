from openai import OpenAI
import streamlit as st
import time
import random
from io import BytesIO  # 파일 다운로드를 위해 필요
import os

# # secrets.toml에 저장된 API 키들을 리스트로 준비
# api_keys = [
#     st.secrets["api_key1"],
#     st.secrets["api_key2"],
#     st.secrets["api_key3"],
#     st.secrets["api_key4"],
#     st.secrets["api_key5"],
#     st.secrets["api_key6"]
# ]

# # 세션 상태에서 현재 API 키를 관리
# if 'api_key' not in st.session_state:
#     # API 키를 랜덤하게 선택하여 세션 상태에 저장
#     st.session_state.api_key = random.choice(api_keys)

# client = OpenAI(api_key=st.session_state.api_key)


# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


st.set_page_config(layout="wide")

st.title("생각+ 생각키우기")

# 사용자로부터 필요한 정보를 입력받습니다.
st.header("마음 문장 만들기 ")
problem = st.text_area("두개 이상의 낱말을 사용해 덕목과 관련된 짧은 글 만들어보기 예시) 예절은 다른 사람을 존중하는 것입니다.")

st.divider()

@st.cache_data  # st.experimental_memo 대신 st.cache_data 사용
def generate_law_document(problem):
    persona = f'''
    이 프롬프트는 도덕을 공부하는 사용자로부터 도덕과 관련된 두 낱말을 이용하여 짧은 도덕 글짓기를합니다. 사용자가 제공한 내용이 현실에 맞지 않거나 사실에 맞지 않는 경우 GPT가 수정해서 작성합니다. 문장이 매끄러운지, 도덕적 올바른지, 일반적인 사람이 공감이 되는말인지 평가해 주세요. 도덕적 상황에 대한 내용을 작성한 후 피드백을 반드시 작성합니다. 다음은 사용자가 제공한 내용입니다:
    도덕적 상황: {problem}
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": "도덕적 행동에 대해서 평가해 주세요"}
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response.choices[0].message.content

# 법률안 생성 버튼
if st.button("마음 문장 만들기"):
    law_document = generate_law_document(problem)
    st.subheader("마음 문장 만들기")
    st.write(law_document)
    
    # 생성된 법률안을 TXT 파일로 변환
    txt_file = BytesIO(law_document.encode('utf-8'))
    
    # 다운로드 링크 제공
    st.download_button(
        label="나의 도덕행동 평가서",
        data=txt_file,
        file_name="generated_law_document.txt",
        mime="text/plain"
    )
