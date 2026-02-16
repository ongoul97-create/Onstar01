import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.express as px

# [설정] 페이지 레이아웃 및 제목
st.set_page_config(page_title="Streamlit 100단계 마스터", layout="wide")

# ==========================================
# PART 1. 기초 텍스트 및 기본 위젯 (01-30)
# ==========================================
st.title("🎓 Streamlit 기초부터 심화까지 100단계")
st.markdown("---")

with st.expander("Step 01-30: 기초 텍스트 및 입력 위젯"):
    st.header("1. 기본 출력")
    st.write("01: 일반 텍스트 출력")
    st.info("05: 정보 메시지 (Blue)")
    st.success("10: 성공 메시지 (Green)")
    
    st.header("2. 사용자 입력 (Widgets)")
    name = st.text_input("15: 텍스트 입력", placeholder="이름을 입력하세요")
    age = st.slider("20: 숫자 슬라이더", 0, 100, 25)
    gender = st.radio("25: 선택 버튼", ["남성", "여성", "기타"])
    agree = st.checkbox("30: 체크박스 동의 여부")

# ==========================================
# PART 2. 데이터 시각화 및 테이블 (31-60)
# ==========================================
with st.expander("Step 31-60: 데이터 처리 및 그래프"):
    st.header("3. 데이터 프레임 활용")
    # 샘플 데이터 생성
    data = pd.DataFrame(
        np.random.randn(10, 5),
        columns=[f'열 {i}' for i in range(1, 6)]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("35: 상호작용 표 (Dataframe)")
        st.dataframe(data, use_container_width=True)
    with col2:
        st.write("40: 정적 표 (Table)")
        st.table(data.iloc[:3])

    st.header("4. 차트 마법사")
    tab1, tab2 = st.tabs(["기본 차트", "고급 Plotly"])
    with tab1:
        st.line_chart(data) # 45: 라인 차트
        st.area_chart(data) # 50: 영역 차트
    with tab2:
        fig = px.scatter(data, x='열 1', y='열 2', size=np.abs(data['열 3'])*10, color='열 4')
        st.plotly_chart(fig) # 60: Plotly 연동

# ==========================================
# PART 3. 심화 레이아웃 및 상태 관리 (61-100)
# ==========================================
with st.expander("Step 61-100: 레이아웃 및 세션 상태(State)"):
    st.header("5. 사이드바 및 레이아웃")
    st.sidebar.title("65: 사이드바 메뉴")
    st.sidebar.date_input("70: 날짜 선택")
    
    # 75: 컬럼 배치
    c1, c2, c3 = st.columns(3)
    c1.metric("온도", "24 °C", "1.2 °C")
    c2.metric("습도", "48%", "-5%")
    c3.metric("기압", "1012 hPa", "0.2 hPa")

    st.header("6. 심화: 세션 상태 (Session State)")
    # 85: 카운터 예제 (페이지 새로고침 시 데이터 유지)
    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter():
        st.session_state.count += 1

    st.write(f"현재 카운트: {st.session_state.count}")
    st.button("90: 카운트 증가 (세션 유지)", on_click=increment_counter)

    st.header("7. 심화: 파일 업로드 및 캐시")
    uploaded_file = st.file_uploader("95: 파일 업로더") # CSV 등 파일 업로드 실습
    
    @st.cache_data
    def expensive_computation(x):
        time.sleep(2) # 100: 캐싱을 이용한 성능 최적화
        return x * x
    
    st.write("캐싱 테스트 결과:", expensive_computation(age))

st.markdown("---")
st.caption("Produced by Gemini | Streamlit Master Class 2026")
