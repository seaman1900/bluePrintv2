# 首页
import streamlit as st
from states import get_states

if __name__ == "__main__":
    
    cur_states = get_states()

    st.session_state.page = "home"
    if st.session_state.get("page")=="home":
        st.set_page_config(layout="wide")
    
    st.title("Blue Print")
    st.write("In Blue Print, You can create, invest and enjoy")
    
    #  -----------     Platform  -----------
    st.subheader("Platform")
    col1, col2, col3 = st.columns(3,gap='medium')
    with col1:
        with st.container(border=True):
            st.markdown("### Create")
            st.write("Article")
            st.write("Video")
            st.write("Code")
            st.write("Anthing Valuable")
    with col2:
        with st.container(border=True):
            st.markdown("### Invest")
            st.write("Content Promotion")
            st.write("Content Maintenance")
            st.write("Ad Placement")
            st.write("Angel Investment")

    with col3:
        with st.container(border=True):
            st.markdown("### Enjoy")
            st.write("所有内容均需付费")
            st.write("最低1积分即可查看")
            st.write("参与内容投资")
            st.write("享受收益分红")


    #  -----------     Community  -----------
    st.subheader("Community")
    col1, col2, col3 = st.columns(3,gap='medium')
    with col1:
        with st.container(border=True):
            st.markdown("### Report")
            st.write("举报违规内容, 违规评论")
            st.write("参与社区治理, 获取治理积分, 享受平台收益分红")
    with col2:
        with st.container(border=True):
            st.markdown("### Suggest")
            st.write("针对平台功能提出建议, 共建平台未来")
            st.write("完善平台功能， 获取平台收益分红")
