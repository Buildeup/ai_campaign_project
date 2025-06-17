import streamlit as st
from modules import db_handler


def show():
    st.header("1️⃣ 캠페인 등록")

    with st.form("campaign_form"):
        name = st.text_input("🛍️ 상품명")
        url = st.text_input("🔗 상품 URL")
        submitted = st.form_submit_button("✅ 저장")

        if submitted:
            if not name or not url:
                st.warning("⚠️ 모든 항목을 입력해주세요.")
                return

            # campaign_id = db_handler.save_campaign(name, url)
            # if campaign_id:
            #     st.success(f"🎯 캠페인 저장 완료 (ID: {campaign_id})")
            #     st.session_state["campaign_id"] = campaign_id
            # else:
            #     st.error("❌ 캠페인 저장 실패")
            st.warning("⚠️ 현재 버전에서는 캠페인 저장 기능이 비활성화되어 있습니다.")
