import streamlit as st

# 사이드바에 메뉴를 추가합니다.
st.sidebar.title('Home')
st.sidebar.write('[1. 생각AI](1. 생각AI.py)')
st.sidebar.write('[1.1 생각+(생각의 힘)](1.1 생각+(생각의 힘).py)')
st.sidebar.write('[1.2 생각+(이미지 생성)](1.2 생각+(이미지 생성).py)')
st.sidebar.write('[2.1 마음+(배우고 싶은 점)](2.1 마음+(배우고 싶은 점).py)')
st.sidebar.write('[2.2 마음+(짧은 문장)](2.2 마음+(짧은 문장).py)')
st.sidebar.write('[2.3 마음+(노래)](2.3 마음+(노래).py)')
st.sidebar.write('[3. 마음AI](3. 마음AI.py)')
st.sidebar.write('[3. 실천AI](3. 실천AI.py)')
st.sidebar.write('[3.1 실천+(계획세우기)](3.1 실천+(계획세우기).py)')

# 메인 페이지 내용
st.title('덕이(AI)에게 물어보세요')
st.write('이 페이지는 초등학생들의 도덕학습을 위해 제작된 챗봇입니다.')

# 파일을 선택하여 실행
selection = st.sidebar.radio("Go to", [
    "Home", 
    "1. 생각AI", "1.1 생각+(생각의 힘)", "1.2 생각+(이미지 생성)",
    "2.1 마음+(배우고 싶은 점)", "2.2 마음+(짧은 문장)", "2.3 마음+(노래)", "3. 마음AI",
    "3. 실천AI", "3.1 실천+(계획세우기)"
])

# 선택한 파일을 실행
if selection == "Home":
    st.title("Home")
elif selection == "1. 생각AI":
    exec(open("pages/1. 생각AI.py").read())
elif selection == "1.1 생각+(생각의 힘)":
    exec(open("pages/1.1 생각+(생각의 힘).py").read())
elif selection == "1.2 생각+(이미지 생성)":
    exec(open("pages/1.2 생각+(이미지 생성).py").read())
elif selection == "2.1 마음+(배우고 싶은 점)":
    exec(open("pages/2.1 마음+(배우고 싶은 점).py").read())
elif selection == "2.2 마음+(짧은 문장)":
    exec(open("pages/2.2 마음+(짧은 문장).py").read())
elif selection == "2.3 마음+(노래)":
    exec(open("pages/2.3 마음+(노래).py").read())
elif selection == "3. 마음AI":
    exec(open("pages/3. 마음AI.py").read())
elif selection == "3. 실천AI":
    exec(open("pages/3. 실천AI.py").read())
elif selection == "3.1 실천+(계획세우기)":
    exec(open("pages/3.1 실천+(계획세우기).py").read())

