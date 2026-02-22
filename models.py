from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class User(BaseModel):
    id: str
    email: str
    plan: str = "free"
    calculations_used: int = 0
    max_calculations: int = 10

class CalcHistory(BaseModel):
    id: str
    user_id: str
    input_data: Dict[str, Any]
    result: Dict[str, Any]
    created_at: datetime
