from pydantic import BaseModel
from typing import List, Optional

class UserDTO(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True