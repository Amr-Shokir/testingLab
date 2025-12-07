
from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.repository_factory import RepositoryFactory

def test_get_user_repository():
  repo = RepositoryFactory.get_repository("user")
  assert isinstance(repo,UserRepository) 

def test_get_product_repository():
  repo = RepositoryFactory.get_repository("product")
  assert isinstance(repo,ProductRepository) 

def test_invalid_type():
  
  try: 
  
    RepositoryFactory.get_repository("invalid_type")
    assert False, "expected valueError for unknown repository"
  
  except ValueError as ve:
    assert str(ve) == "Unknown repository type"

