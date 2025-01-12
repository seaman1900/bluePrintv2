from pydantic import BaseModel
from typing import List

class PrintMetadata(BaseModel):
    views: int
    comments: int
    likes: int
    dislikes: int
    total_invest: int

class Print(BaseModel):
    print_id: str
    author_id: str
    title: str
    created_at: str # 这里改成str
    price: int
    description: str
    body: str
    metadata: PrintMetadata
    tags: List[str]
    status: str