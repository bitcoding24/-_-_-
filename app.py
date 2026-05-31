import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="GA 위험지수차이 그래프",
    page_icon="📊",
    layout="wide"
)

st.title("📊 전국 학교 실제 학사일정 vs GA 최적 학사일정 차이 분석")
st.caption("Colab에서 계산한 GA 분석 결과 그래프를 보여주는 페이지입니다.")

HTML_PATH = Path("ga_graphs.html")

if not HTML_PATH.exists():
    st.error(f"HTML 파일을 찾지 못했습니다: {HTML_PATH}")
    st.stop()

html_code = HTML_PATH.read_text(encoding="utf-8")

components.html(
    html_code,
    height=1400,
    scrolling=True
)