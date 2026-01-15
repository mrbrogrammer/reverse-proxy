from sqlalchemy.orm import Session
from domain.dto.user_dto import UserDTO
from repository.user_repository import UserRepository
from typing import List, Optional

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session
    def get_by_id(self, user_id: int) -> Optional[UserDTO]:
        return self.session.query(UserDTO).filter(UserDTO.id == user_id).first()
    def add(self, user: UserDTO) -> None:
        self.session.add(user)
        self.session.commit()
    def list_all(self) -> List[UserDTO]:
        return self.session.query(UserDTO).all()