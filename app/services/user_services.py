import sys
from sqlalchemy.orm import Session

sys.path.append('../')

from app.core.models import User
from app.core.schemas import UserCreate

def create_user(user: UserCreate, db: Session):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user