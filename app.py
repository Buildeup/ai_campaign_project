import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# 🔥 현재 디렉토리를 모듈 검색 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit_app import campaign_ui, blog_ui  # analysis_ui는 아직 없으면 제외!

# 💡 기본 설정
st.set_page_config(page_title="AI Campaign Management", page_icon="📢", layout="wide")

# 💡 사이드바 메뉴
st.sidebar.title("AI 캠페인 관리")
page = st.sidebar.radio("페이지 선택", ["캠페인 등록", "블로그 리스트 검색"])

# 💡 선택한 페이지에 따라 호출
if page == "캠페인 등록":
    campaign_ui.show()
elif page == "블로그 리스트 검색":
    blog_ui.show()
# elif page == "블로그 분석":
#     analysis_ui.show()

# 💡 푸터
st.sidebar.markdown("©️ 2025 Buildeup e.TMS")
