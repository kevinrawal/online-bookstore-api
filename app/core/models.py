"""models"""
import sys
from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

sys.path.append('../')

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(TIMESTAMP) 

    carts = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    price = Column(DECIMAL(10, 2))
    quantity_available = Column(Integer)
    created_at = Column(TIMESTAMP)

    carts = relationship("Cart", back_populates="book")
    order_items = relationship("OrderItem", back_populates="book")

class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    quantity = Column(Integer)
    created_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="carts")
    book = relationship("Book", back_populates="carts")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(DECIMAL(10, 2))
    status = Column(String)
    created_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_items")
    book = relationship("Book", back_populates="order_items")
