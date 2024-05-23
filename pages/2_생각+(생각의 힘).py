from openai import OpenAI
import streamlit as st
import random
from io import BytesIO  # 파일 다운로드를 위해 필요
import os

# API 키 설정
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

st.set_page_config(layout="wide")

st.title("생각+ 생각키우기")

# 사용자로부터 필요한 정보를 입력받습니다.
st.header("1. 내가 겪었던 일 ")
problem = st.text_area("행동과 관련된 내가 겪었던 일을 입력하세요. 예시) 부모님의 심부름을 했다.")

st.header("2. 아는 힘")
ideal = st.text_area("겪은 상황을 통해서 도덕적으로 알게 된 것은? 예시) 부모님 말씀을 잘 듣는 것은 바른 행동이다.")

st.header("3. 생각하는 힘")
solution = st.text_area("겪은 상황을 통해서 한 나의 판단은? 예시) 부모님의 심부름을 해드리면 내 마음이 뿌듯하다고 판단된다.")

st.header("4. 마음의 힘")
government_action = st.text_area("겪은 상황에서 자신을 돌아보면서 나의 마음 표현하기? 예시) 부모님을 돕는 것은 기쁜 일이다.")

st.header("5. 행동의 힘")
penalties = st.text_area("상황에서 내가 할 수 있는 도덕적 행동은? 예시) 부모님을 항상 도와드릴 것이다.")

st.markdown("---")  # 구분선

@st.cache_data
def generate_moral_document(problem, ideal, solution, government_action, penalties):
    persona = f'''
    이 프롬프트는 사용자로부터 제공된 도덕적 상황, 겪은 상황을 통해서 도덕적으로 알게 된 것, 그 상황에 대한 나의 판단, 겪은 상황에서 자신이 느낀 점, 도덕적 판단을 내린 후 내가 하는 행동을 바탕으로,
    나의 도덕적 행동에 대해서 평가에 도움을 주는 GPT 모델입니다. 이 도덕적 모델은 나의 상황에 대해 도덕적 지식과 생각 그리고 감정 등을 판단하여 이상적인 도덕적 행동을 하기 위한 구체적인 방안을 제시해야 합니다.
    사용자가 제공한 내용이 현실에 맞지 않거나 사실에 맞지 않는 경우 GPT가 수정해서 작성합니다. 도덕적 상황에 대한 내용을 작성한 후 피드백을 반드시 첫째, 둘째, 셋째 개조식으로 여러 문단으로 작성합니다.
    다음은 사용자가 제공한 내용입니다.
    도덕적 상황: {problem}
    겪은 상황을 통해서 도덕적으로 알게 된 것: {ideal}
    겪은 상황을 통해서 한 나의 판단은: {solution}
    겪은 상황에서 자신을 돌아보면서 나의 마음 표현하기: {government_action}
    상황에서 내가 할 수 있는 도덕적 행동은: {penalties}
    '''

    response = client.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": "도덕적 생각에 대해서 평가해 주세요"}
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response.choices[0].message['content']

# 법률안 생성 버튼
if st.button("도덕적 행동 평가서"):
    moral_document = generate_moral_document(problem, ideal, solution, government_action, penalties)
    st.subheader("도덕적 행동 평가")
    st.write(moral_document)
    
    # 생성된 문서를 TXT 파일로 변환
    txt_file = BytesIO(moral_document.encode('utf-8'))
    
    # 다운로드 링크 제공
    st.download_button(
        label="나의 도덕행동 평가서",
        data=txt_file,
        file_name="generated_moral_document.txt",
        mime="text/plain"
    )
