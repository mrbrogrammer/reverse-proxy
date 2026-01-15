from abc import ABC, abstractmethod
from typing import List, Optional
from domain.dto.user_dto import UserDTO

class UserRepository(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserDTO]:
        pass

    @abstractmethod
    def add(self, user: UserDTO) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[UserDTO]:
        pass