# 展示页面
import streamlit as st

# apis
from apis.api_print import get_prints_all
from states import get_states

# models
from models.print import Print

# modules
from modules.print_card import print_card

# 设置页面wide显示
st.session_state.page = "blue_print"
if st.session_state.get("page") == "blue_print":
    st.set_page_config(layout='wide')


cur_states = get_states()

if cur_states.view_type == 'preview':
    st.title("Blue Print")
    left, center, right = st.columns([1,2,1])
    prints = get_prints_all()
    with center:
      for print in prints:
        print = Print(**print)
        print_card(print)