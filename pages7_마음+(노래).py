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

st.title("마음+ 마음 노래 만들기")

# 사용자로부터 필요한 정보를 입력받습니다.
st.header("1.연상하기 ")
problem = st.text_area("덕목과 관련된어 연상되는 낱말을 적어보세요. 예시) 친구, 웃음, 노래")

st.header("2. 가사 만들어 보기")
ideal = st.text_area(" 떠오르는 낱말로 덕목과 관련 노래 가사를 지어 보세요. 예시) 친구를 보면 웃음이 나와.")

st.divider()

@st.cache_data  # st.experimental_memo 대신 st.cache_data 사용
def generate_law_document(problem, ideal):
    persona = f'''
    이 프롬프트는 사용자로부터 제공된 낱말과 가사를 바탕으로 작곡에 필요한 가사작성에 도움을 주는 GPT 모델입니다. 이 가사작성 모델은 덕목과 관련되어 학생들의 덕목과 관련된 노래를 작사 작곡 함으로써, 도덕적 삶에 대한 태도를 강화시킨다. 사용자가 제공한 내용이 현실에 맞지 않거나 사실에 맞지 않는 경우 GPT가 수정해서 작성합니다. 도덕적 상황에 대한 내용을 작성한 후 피드백을 반드시 작성합니다. 가사를 작성한 다음 https://suno.com/ 사이트를 이용하도록 추천해 주세요.  다음은 사용자가 제공한 내용입니다:
    도덕적 상황: {problem}
    겪은 상황을 통해서 도덕적으로 알게된 것: {ideal}
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": "가사를 작성해 주세요."}
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response.choices[0].message.content

# 법률안 생성 버튼
if st.button("도덕 가사 추천"):
    law_document = generate_law_document(problem, ideal)
    st.subheader("도덕 가사 추천")
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
