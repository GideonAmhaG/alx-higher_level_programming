#!/usr/bin/python3
"""module for City class"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class that inherits from Base of relationship_state"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
