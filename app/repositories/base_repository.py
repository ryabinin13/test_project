from abc import ABC, abstractmethod
from app import SessionLocal

class BaseRepository(ABC):
    def __init__(self, model):
        self.db = SessionLocal()
        self.model = model

    @abstractmethod
    def create(self, data: dict):
        pass

    def get_all(self):
        return self.db.query(self.model).all()

    def get(self, id):
        return self.db.query(self.model).where(self.model.id == id).first()

    @abstractmethod
    def update(self, data: dict):
        pass

    @abstractmethod
    def delete(self, id):
        pass

        


