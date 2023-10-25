# from sqlalchemy.orm import Session
# import models
# import schemas
#
#
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# -- CRUD
from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first
    # eig een sql query, first anders blijft zoeken ook al uniek


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):  # was json en omgezet naar User IN
    fake_hashed_password = user.password + "notreallyhashed"  # placeholder lmao
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)  # toevoegen aan db, klaarzetten
    db.commit()  # schrijven naar db
    db.refresh(db_user)  # user updaten in db want we schrijven email en pw maar ook id is nodig dus refresh
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)  # maken van item een dict en "**" zetten per attr er in
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
