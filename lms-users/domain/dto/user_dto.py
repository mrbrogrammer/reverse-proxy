from pydantic import BaseModel
from typing import List, Optional

class UserDTO(BaseModel):
    uid: Optional[int] = None
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

