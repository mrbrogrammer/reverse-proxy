
from fastapi import APIRouter, Depends
from service.user_service import UserService
from domain.dto.user_dto import UserDTO
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from domain.dto import user_dto
from domain.dto import user_dto
from domain.user import User
from fastapi import APIRouter
from repository.sql_alchemy_product_repository import SqlAlchemyUserRepository
from config.database import get_db

router = APIRouter(tags=["users"])

def get_user_service(db: Session = Depends(get_db)):
    return UserService(SqlAlchemyUserRepository(db))

@router.get('/users', response_model=List[user_dto.UserDTO])
def test_users(db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    users = user_service.get_users()
    user_dto_list = [user_dto.UserDTO.from_orm(user) for user in users]
    return user_dto_list

@router.get('/users/{user_id}', response_model=user_dto.UserDTO)
def get_user_by_id(user_id: int, db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_dto.UserDTO.from_orm(user)
