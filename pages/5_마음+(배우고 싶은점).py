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

st.title("마음+ 마음 본받기")

# 사용자로부터 필요한 정보를 입력받습니다.
st.header("1. 내가 읽은 위인전을 제목을 적어 봅시다. ")
problem = st.text_area("자신이 본받고 싶은 인물을 적어보세요. 예시) 이순신, 손기정 등 ")

st.header("2. 내가 읽은 위인의 본받을 점을 알아봅시다. ")
ideal = st.text_area("위인을 통해서 본받을 인성 핵심 가치는 무엇인가? 예시) 이순신의 나라를 위하는 마음.")

st.header("3. 본받을 점과 연결 시켜서 내가 부족한 점을 적어 보세요")
solution = st.text_area("상대방에 대한 배려하는 마음, 성실성, 정직, 예의 등  예시) 나이팅케일 처럼 상대방을 위해 봉사하는 마음이 난 부족한 것 같아.")


st.divider()

@st.cache_data  # st.experimental_memo 대신 st.cache_data 사용
def generate_law_document(problem, ideal, solution):
    persona = f'''
    이 프롬프트는 사용자로부터 본받고 싶은 위인전의 제목, 위인의 본받을 점, 위인을 통해 나의 부족한 점을 보충하고 더 나은 사람이 되기 위해 도움을 주는 GPT 모델입니다. 초등학생들 수준에 실천할 수 있도록 해주세요. 이 도덕적 모델은 나의 부족한 점을 판단하여 더 나온 사람이 되기 위한 구체적인 실천 방안을 제시해야 합니다. 구체적인 실천방안은 1주일로 제시하고, 1일차, 2일자, 3일차 이렇게 제시합니다. 사용자가 제공한 내용이 현실에 맞지 않거나 사실에 맞지 않는 경우 GPT가 수정해서 작성합니다. 도덕적 상황에 대한 내용을 작성한 후 피드백을 반드시 작성합니다. 다음은 사용자가 제공한 내용입니다:
    도덕적 상황: {problem}
    겪은 상황을 통해서 도덕적으로 알게된 것: {ideal}
    겪은 상황을 통해서 한 나의 판단은: {solution}
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": "실천 계획을 추천해주세요."}
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response.choices[0].message.content

# 법률안 생성 버튼
if st.button("인성 행동 실천 평가서"):
    law_document = generate_law_document(problem, ideal, solution)
    st.subheader("인성 실천 행동 평가")
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
