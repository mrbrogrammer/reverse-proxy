from repository.user_repository import UserRepository
from domain.dto.user_dto import UserDTO
from typing import List, Optional

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    def get_user(self, user_id: int) -> Optional[UserDTO]:
            return self.repository.get_by_id(user_id)
    def create_user(self, name: str, email: str) -> UserDTO:
        user = UserDTO(name=name, email=email)
        self.repository.add(user)
        return user