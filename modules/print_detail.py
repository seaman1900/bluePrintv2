# 详情页
import streamlit as st
from models.print import Print
from models.user import User

from states import get_states

from apis.api_invest import create_invest

# 返回按钮
def back_bar():
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("back", key="back", icon=':material/arrow_back:', type='tertiary'):
            cur_states = get_states()
            cur_states.view_type = "preview"
            st.rerun()
    with col2:
        pass

# 内容主体
def main_print(print_info: Print):
    st.title(print_info.title)
    st.caption(print_info.description)
    st.markdown(print_info.body)

# 投资窗口
@st.dialog("invest")
def invest_window(print_info: Print, user: User, investment_type: str):
    st.header("投资: ")
    number = st.number_input("投资金额：", min_value=0, max_value=1000, value=100)
    if st.button("确认投资", key="invest"):
        result = create_invest(user.user_id, print_info.print_id, number, investment_type)
        st.success(result)

# 投资按钮
def invest_bar(print_info: Print):
    cur_states = get_states()
    user = cur_states.user
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("内容推荐"):
            invest_window(print_info, user, "Content Promotion")
    with col2:
        if st.button("内容维护"):
            invest_window(print_info, user, "Content Maintenance")
    with col3:
        if st.button("广告投放"):
            invest_window(print_info, user, "Ad Placement")
    with col4:
        if st.button("天使投资"):
            invest_window(print_info, user, "Angel Investment")

# 评论区
def comments():
    pass

def print_detail(print_info: Print):
    main_print(print_info)
    invest_bar(print_info)

