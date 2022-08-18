from sqlalchemy import Column, String, Integer

from src import Model

class Tag(Model):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)

    def __init__(self, name):
        self.name = name
