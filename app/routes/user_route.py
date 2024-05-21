import sys
from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine

sys.path.append('../')
from app.core.schemas import UserCreate, User

from app.services import user_services

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(db=db, user=user)
