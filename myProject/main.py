# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
#
# import crud
# import schemas
# import models
# from database import SessionLocal, engine
# import os
#
# if not os.path.exists('.\sqlitedb'):
#     os.makedirs('.\sqlitedb')
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# # POST /users
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db, user=user)
#
#
# # GET /users/?skip=&limit=
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# # GET /users/{user_id}
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# # POST /users/{user_id}/items
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_items(db=db, item=item, user_id=user_id)
#
#
# # GET /items/?skip=&limit=
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

# -- main
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, SessionLocal

if not os.path.exists('sqlitedb'):
    os.makedirs('sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
        # als het error zou geven, probeert het maar als het niet lukt gaat db dicht --> errorhandling of try catch
    finally:
        db.close()


# GET /users/?skip=&limit=
@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):  # async weg
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


# POST /users
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user=user)


# GET /users/{user_id}
@app.get("/users/{id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# GET /items/?skip=&limit=
@app.get("/items", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# POST /users/{user_id}/items/
@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db_session)):
    return crud.create_item(db, item=item, user_id=user_id)  # op volgorde van crud methode
