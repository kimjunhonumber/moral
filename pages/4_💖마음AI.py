from openai import OpenAI
import streamlit as st
import time
import random
import os

# API 키 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# 업데이트된 Assistant ID
assistant_id = "asst_5SiKVdqD5bk8Y0K6SivNqmg5"

# 페이지 설정
st.set_page_config(page_title="마음AI", page_icon="💓")
st.title("❤‍🔥마음AI")

# 사용자 정의 CSS 추가
st.markdown("""
    <style>
    .stApp {
        background-color: #FAF9F6; /* 아주 밝은 회색 배경 */
        color: #333333; /* 진한 회색 텍스트 */
    }
    .stSidebar {
        background-color: #F7F7F7; /* 밝은 회색 사이드바 */
        color: #333333; /* 진한 회색 텍스트 */
    }
    .stButton > button {
        background-color: #6C63FF; /* 밝은 보라색 버튼 */
        color: white; /* 흰색 텍스트 */
        border-radius: 10px; /* 둥근 모서리 */
        border: none; /* 테두리 제거 */
    }
    .stTextInput > div > input {
        background-color: #E0FFFF; /* 라이트 시안 입력 상자 */
        color: #333333; /* 진한 회색 텍스트 */
        border-radius: 10px; /* 둥근 모서리 */
        border: 1px solid #CCCCCC; /* 회색 테두리 */
    }
    .stAlert {
        background-color: #FFDDC1; /* 밝은 주황색 알림 */
        color: #333333; /* 진한 회색 텍스트 */
    }
    .stMarkdown {
        background-color: #FFFACD; /* 라이트 옐로우 마크다운 */
        color: #333333; /* 진한 회색 텍스트 */
        border-radius: 10px; /* 둥근 모서리 */
        padding: 10px; /* 패딩 추가 */
    }
    </style>
    """, unsafe_allow_html=True)



# 사이드바 설정
with st.sidebar:
    if "thread_id" not in st.session_state:
        st.session_state.thread_id = ""

    thread_btn = st.button("Thread 생성")

    if thread_btn:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id
        st.subheader(f"Created Thread ID: {st.session_state.thread_id}")
        st.info("ID 생성되었습니다.")
        st.info("ID를 기억하면 대화내용을 이어갈 수 있습니다.")
        st.divider()
        st.subheader("추천 질문")
        st.info("고민이 있는 학생에게 공감하는 방법은 무엇입니까?")
        st.info("고민상황에 나라면 어떻게 행동할까?")
        st.info("급식 시간에 끼어드는 학생이 있다면 나라면 어떻게 행동할까?")
        st.info("나의 고민을 해결하는 방법을 추천해줘.")

# 스레드 ID 입력란
thread_id = st.text_input("Thread ID", value=st.session_state.thread_id)

# 초기 메시지 설정
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "안녕하세요, 저는 마음AI 챗봇입니다. 먼저 왼쪽의 'Thread 생성'버튼을 눌러주세요. 무엇을 도와드릴까요?"}]

# 아이콘을 설정하는 함수
def get_avatar(role):
    return "🐯" if role == "user" else "🐻"

# 메시지 출력
for msg in st.session_state.messages:
    avatar = get_avatar(msg["role"])
    st.chat_message(msg["role"], avatar=avatar).write(msg["content"])

# 사용자 입력 처리
if prompt := st.chat_input():
    if not thread_id:
        st.error("Please add your thread_id to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar=get_avatar("user")).write(prompt)

    response = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    run_id = run.id

    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status == "completed":
            break
        else:
            time.sleep(2)

    thread_messages = client.beta.threads.messages.list(thread_id)
    msg = thread_messages.data[0].content[0].text.value

    # 어시스턴트의 응답을 한 글자씩 출력
    st.session_state.messages.append({"role": "assistant", "content": msg})
    full_message = ""
    message_placeholder = st.empty()
    for char in msg:
        full_message += char
        message_placeholder.write(f"🐻 {full_message}")
        time.sleep(0.05)  # 출력 속도 조절
