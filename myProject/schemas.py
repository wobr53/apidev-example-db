# from pydantic import BaseModel
#
#
# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
#
# class Item(ItemBase):   # ITEM OUT
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class ItemCreate(ItemBase):    # ITEM IN
#     pass
#
#
# class UserBase(BaseModel):
#     email: str
#
#
# class User(UserBase):   # USER OUT
#     id: int
#     is_active: bool
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True
#
#
# class UserCreate(UserBase):    # USER IN
#     password: str

# -- schemas
# Basemodels niet meer in de main file maar aparte file
from pydantic import BaseModel


class ItemBase(BaseModel):  # base classe voor items
    title: str
    description: str


class Item(ItemBase):  # Item OUT
    id: int
    owner_id: int

    class Config:  # item moet uit db worden gehaald --> altijd bij OUT classes
        orm_mode = True


class ItemCreate(ItemBase):  # Item IN
    pass
    # owner_id: int niet nodig want wordt in url meegegeven


class UserBase(BaseModel):  # base classe voor user
    email: str  # overerving naar andere, dus niet toevoegen bij OUt en IN


class User(UserBase):  # User OUT
    id: int
    is_active: bool
    # pw mag er niet bij worden uitgestuurd
    items: list[Item] = []  # lege lijst dat bij opvraag user, de items in een lege lijst worden gestopt

    class Config:  # user moet uit db worden gehaald --> altijd bij OUT classes
        orm_mode = True


class UserCreate(UserBase):  # User IN
    password: str
