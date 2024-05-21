from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True

class CartBase(BaseModel):
    user_id: int
    book_id: int
    quantity: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    order_id: int
    book_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    total_price: float
    status: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    created_at: str
    order_items: List[OrderItem] = []

    class Config:
        orm_mode = True
