import sys
import os

# 경로 등록
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_app import campaign_ui, blog_ui

# Initialize session state for page if not already set
if "page" not in st.session_state:
    st.session_state.page = "캠페인 등록" # Default starting page

st.set_page_config(page_title="AI Campaign Management", page_icon="📢", layout="wide")

# 사이드바 메뉴
st.sidebar.title("📋 AI 캠페인 관리")
# Use the session state to control the radio button's value and update it
st.session_state.page = st.sidebar.radio(
    "페이지 선택",
    ["캠페인 등록", "블로그 리스트 검색"],
    index=["캠페인 등록", "블로그 리스트 검색"].index(st.session_state.page)
)

# 페이지 라우팅
if st.session_state.page == "캠페인 등록":
    campaign_ui.show()
elif st.session_state.page == "블로그 리스트 검색":
    blog_ui.show()

# 푸터
st.sidebar.markdown("©️ 2025 Buildeup e.TMS")
