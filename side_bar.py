import streamlit as st

# 사이드바 제목
st.sidebar.title('Home')

# 사이드바 링크 추가
st.sidebar.markdown('### 생각AI')
st.sidebar.write('[1. 생각AI](1. 생각AI.py)')
st.sidebar.write('[1.1 생각+(생각의 힘)](1.1 생각+(생각의 힘).py)')
st.sidebar.write('[1.2 생각+(이미지 생성)](1.2 생각+(이미지 생성).py)')

st.sidebar.markdown('### 마음AI')
st.sidebar.write('[2.1 마음+(배우고 싶은 점)](2.1 마음+(배우고 싶은 점).py)')
st.sidebar.write('[2.2 마음+(짧은 문장)](2.2 마음+(짧은 문장).py)')
st.sidebar.write('[2.3 마음+(노래)](2.3 마음+(노래).py)')
st.sidebar.write('[3. 마음AI](3. 마음AI.py)')

st.sidebar.markdown('### 실천AI')
st.sidebar.write('[3. 실천AI](3. 실천AI.py)')
st.sidebar.write('[3.1 실천+(계획세우기)](3.1 실천+(계획세우기).py)')

# 사이드바 항목 클릭 시 파일 실행
selection = st.sidebar.radio("Go to", [
    "Home", 
    "1. 생각AI", "1.1 생각+(생각의 힘)", "1.2 생각+(이미지 생성)",
    "2.1 마음+(배우고 싶은 점)", "2.2 마음+(짧은 문장)", "2.3 마음+(노래)", "3. 마음AI",
    "3. 실천AI", "3.1 실천+(계획세우기)"
])

# 파일에 해당하는 페이지 내용 표시
if selection == "Home":
    st.title("Home")
elif selection == "1. 생각AI":
    exec(open("1. 생각AI.py").read())
elif selection == "1.1 생각+(생각의 힘)":
    exec(open("1.1 생각+(생각의 힘).py").read())
elif selection == "1.2 생각+(이미지 생성)":
    exec(open("1.2 생각+(이미지 생성).py").read())
elif selection == "2.1 마음+(배우고 싶은 점)":
    exec(open("2.1 마음+(배우고 싶은 점).py").read())
elif selection == "2.2 마음+(짧은 문장)":
    exec(open("2.2 마음+(짧은 문장).py").read())
elif selection == "2.3 마음+(노래)":
    exec(open("2.3 마음+(노래).py").read())
elif selection == "3. 마음AI":
    exec(open("3. 마음AI.py").read())
elif selection == "3. 실천AI":
    exec(open("3. 실천AI.py").read())
elif selection == "3.1 실천+(계획세우기)":
    exec(open("3.1 실천+(계획세우기).py").read())
