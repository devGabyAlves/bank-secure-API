from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_conect()
    repo = UserRepository(conn)

    username = "Gaby"
    password = "&18xMG\ump8K"

    repo.registry_user(username, password)
    user = repo.get_user_by_username(username)
    print(user)
    
    repo.edit_balance(user[0], 6321.99)
    print(user)