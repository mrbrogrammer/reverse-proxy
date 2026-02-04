from sqlalchemy.orm import Session
from domain.dto.user_dto import UserDTO
from domain.user import User
from repository.user_repository import UserRepository
from typing import List, Optional

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> List[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = self.session.query(User).filter(User.id == user_id).first()
        if user:
            return User.from_orm(user)
        return None
    
    def add(self, user: UserDTO) -> None:
        self.session.add(user)
        self.session.commit()

    def list_all(self) -> List[UserDTO]:
        return self.session.query(UserDTO).all()