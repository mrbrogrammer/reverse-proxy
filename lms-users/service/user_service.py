from repository.sql_alchemy_product_repository import SqlAlchemyUserRepository
from domain.dto.user_dto import UserDTO
from typing import List, Optional

class UserService:
    def __init__(self, repository: SqlAlchemyUserRepository):
        self.repository = repository
        
    def get_users(self) -> List[UserDTO]:
        users = self.repository.get_users()
        return users
    
    def get_user(self, user_id: int) -> Optional[UserDTO]:
        user = self.repository.get_user(user_id)
        return user

    def create_user(self, name: str, email: str) -> UserDTO:
        user = UserDTO(name=name, email=email)
        self.repository.add(user)
        return user