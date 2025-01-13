# 维护用到的所有state
import streamlit as st
from pydantic import BaseModel
from typing import List, Optional
from models.user import User
from models.print import Print

class States(BaseModel):
  user: Optional[User]
  print_info: Optional[Print]
  is_login: bool
  view_type: str

def get_states() -> States:
  if "proj_states" not in st.session_state:
    st.session_state.proj_states = States(
      user=None,
      is_login=False,
      view_type="preview",
      print_info=None
    )
  return st.session_state.proj_states
