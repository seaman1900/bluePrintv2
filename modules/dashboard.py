# 展示个人数据
import streamlit as st

from models.user import User
from models.print import Print

def dashboard(user: User):
    st.title("用户数据展示")
    st.write(user)