import streamlit as st

from modules.auth_card import auth_card
from modules.dashboard import dashboard

from states import get_states

# 设置页面wide显示
st.session_state.page = "personal"
if st.session_state.get("page") == "personal":
    st.set_page_config(layout='wide')

cur_states = get_states()

if cur_states.is_login:
    user = cur_states.user
    dashboard(user)
else:
    auth_card()
