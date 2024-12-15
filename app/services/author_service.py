from app.schemas import AuthorBody
from app.repositories.author_repository import AuthorRepository

class AuthorService:

    def add_author(self, authorbody: AuthorBody):
        return AuthorRepository().create(authorbody)
    
    def get_author(self, id):
        return AuthorRepository().get(id)
    
    def get_all_author(self):
        return AuthorRepository().get_all()
    
    def delete_author(self, id):
        return AuthorRepository().delete(id)
    
    def update_author(self, id, authorbody: AuthorBody):
        return AuthorRepository().update(id, authorbody)