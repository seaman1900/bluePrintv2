# 维护用到的所有state
import streamlit as st
from pydantic import BaseModel
from typing import List, Optional
from models.user import User

class States(BaseModel):
  user: Optional[User]
  is_login: bool
  view_type: str


def get_states() -> States:
  if "proj_states" not in st.session_state:
    st.session_state.proj_states = States(
      user=None,
      is_login=False,
      view_type="preview"
    )
  return st.session_state.proj_states
