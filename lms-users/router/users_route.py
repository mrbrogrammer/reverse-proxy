
from fastapi import APIRouter, Depends
from service.user_service import UserService
from domain.dto.user_dto import UserDTO
from pydantic import BaseModel

router = APIRouter(tags=["users"])

def get_user_service():
    return UserService()

@router.post("/users/")
def crea_user_endpoint(
    user_data: UserDTO,
    user_service: UserService = Depends(get_user_service)
):
    # The controller layer delegates logic to the service layer
    result = user_service.get_user(user_data.id)
    return result
