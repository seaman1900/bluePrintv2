from pydantic import BaseModel
from typing import List
from datetime import datetime

class Metadata(BaseModel):
    followers: int
    likes: int
    dislikes: int

# 用户模型
class User(BaseModel):
    user_id: str
    username: str
    email: str
    password_hash: str
    registration_date: datetime
    last_login: datetime
    role: List[str]
    avatar_url: str
    mark_list: List[dict]
    wish_list: List[dict]
    metadata: Metadata


# 登录请求模型
class LoginRequest(BaseModel):
    username: str
    password: str

# 注册请求模型
class RegisterRequest(BaseModel):
    username: str
    email: str
    avatar_url: str
    password: str

# 更新用户信息请求模型
class UpdateUserRequest(BaseModel):
    username: str
    email: str
    avatar_url: str
    password: str