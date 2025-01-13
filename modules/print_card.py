import streamlit as st
from datetime import datetime

from models.print import Print
from models.user import User
from models.balance import Balance

from apis.api_user import get_user
from apis.api_balance import get_balance, update_balance
from apis.api_transaction import buy_print, check_purchase
from states import get_states

def head(print_info: Print, author: User):
    col1, col2, col3 = st.columns([1,4,1], vertical_alignment='center', gap='medium')
    col1.image(author.avatar_url)
    with col2:
        col2.html('<h3>'+ print_info.title +'</h3>')
        st.caption("📅 "+ print_info.created_at +" by " + author.username)
    with col3:
        # 价格
        st.markdown(":green-background[$"+ str(print_info.price) +"]")

def main_content(print_info: Print):
    st.write(print_info.description)

# 购买的二次确认窗口
@st.dialog("second_check")
def buy_dialog(price, print_info: Print):
    cur_state = get_states()
    # 判断是否登录
    if not cur_state.is_login:
        st.error("请先登录")
    else:
        user = cur_state.user
        balance = get_balance(user.user_id)
        st.write(f"当前余额：{balance} 价格：{price}")
        if st.button("确定", key=user.user_id+"_buy_confirm"):
            result = check_purchase(user.user_id, print_info.print_id)
            if result == "yes":
                # 跳转到详情页
                cur_state.view_type = "detail"
                cur_state.print_info = print_info
                st.rerun()
            else:
                if balance >= price:
                    # 创建transaction
                    trans = buy_print(user.user_id, print_info.print_id, price)
                    st.success(trans)
                    new_buyer_balance = Balance(
                        user_id=user.user_id,
                        balance= - price,
                        frozen_amount=0,
                        last_update_time=None
                    )
                    new_seller_balance = Balance(
                        user_id=print_info.author_id,
                        balance= price,
                        frozen_amount=0,
                        last_update_time=None
                    )
                    # 买家减少余额, 卖家增加余额
                    updated_buyer_balance = update_balance(user.user_id, new_buyer_balance)
                    updated_seller_balance = update_balance(print_info.author_id, new_seller_balance)
                    st.success(f"买家余额：{updated_buyer_balance} 卖家余额：{updated_seller_balance}")
                    st.write("购买成功")
                else:
                    st.error("余额不足")

# 状态信息显示
def status_bar(print_info: Print):
    col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment='center')
    col1.caption("👀 " + str(print_info.metadata.views))
    col2.caption("💬 " + str(print_info.metadata.comments))
    col3.caption("👍 " + str(print_info.metadata.likes))
    col4.caption("👎 " + str(print_info.metadata.dislikes))
    if col5.button("🛒 Buy", key=print_info.print_id+"_buy"):
        buy_dialog(print_info.price, print_info)

# 投资相关的数据先不展示

# 预览界面
# @st.dialog("Preview")
# def preview(print_info: Print):
#     st.write("这是预览界面")
#     if st.button("buy", key=print_info.print_id+"_preview"):
#         st.session_state.view_type = "detail"
#         st.rerun()

def print_card(print_info: Print):
    author_id = print_info.author_id
    author = get_user(author_id)
    author = User(**author)
    with st.container(border=True):
        head(print_info, author)
        main_content(print_info)
        status_bar(print_info)