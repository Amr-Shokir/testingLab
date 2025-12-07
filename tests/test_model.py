from models.user import User
from repositories.repository_factory import RepositoryFactory

def test_user_creation():
  u = User(1, "ali", "@gmail.com")
  assert u.id == 1
  assert u.name == "ali"
  assert u.email == "@gmail.com"


