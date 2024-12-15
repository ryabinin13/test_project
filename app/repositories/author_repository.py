from app.schemas import AuthorBody
from app.models import Author
from app.repositories.base_repository import BaseRepository

class AuthorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Author)

    def create(self, authorbody: AuthorBody):
        author = Author(name=authorbody.name, lastname=authorbody.lastname, birthday=authorbody.birthday)
        self.db.add(author)
        self.db.commit()
        return author.id
    
    def update(self, id, authorbody: AuthorBody):
        author = self.db.query(Author).where(Author.id == id).first()
        if author:
            author.name = authorbody.name
            author.birthday = authorbody.birthday
            author.lastname = authorbody.lastname

        self.db.commit()
        return author.id

    def delete(self, id):
        author = self.db.query(Author).where(Author.id == id).first()
        self.db.delete(author)
        self.db.commit()
        return id
