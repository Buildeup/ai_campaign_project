import streamlit as st
import pandas as pd
from modules import naver_api_handler, db_handler


def show():
    st.header("2️⃣ 블로그 리스트 검색")

    # if "campaign_id" not in st.session_state: # 캠페인 ID 확인 로직 주석 처리
    #     st.warning("⚠️ 먼저 캠페인을 등록하세요.")
    #     return

    with st.form("blog_search_form"):
        keyword = st.text_input("🔎 키워드")
        num_results = st.number_input("🔢 반환할 블로그 수 (최대 1000개)", min_value=10, max_value=1000, step=10, value=100)
        sort_option = st.selectbox("⚙️ 정렬", ["정확도순", "최신순"])
        submitted = st.form_submit_button("검색")

        if submitted and keyword:
            st.info(f"🔍 '{keyword}' 블로그 {num_results}개 검색 중…")
            blogs = naver_api_handler.search_and_parse(keyword, total_count=num_results, sort_option=sort_option)
            if not blogs:
                st.warning("❌ 검색 결과가 없습니다.")
                return

            st.success(f"✅ 총 {len(blogs)}개 블로그를 가져왔습니다.")
            st.dataframe(pd.DataFrame(blogs))

            # saved = db_handler.save_blogs_to_db(blogs, st.session_state["campaign_id"]) # DB 저장 로직 주석 처리
            # st.success(f"💾 DB 저장 완료: {saved}개")
            st.warning("⚠️ 블로그 검색 결과 저장은 현재 비활성화되어 있습니다.") # DB 저장 비활성화 경고
        elif submitted:
            st.warning("⚠️ 키워드를 입력해주세요.")
