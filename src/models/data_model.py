from sqlalchemy import Column, String, Integer, Date

from src import Model

class Data(Model):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(1000), nullable=True)
    uri = Column(String(1000), nullable=True)
    user_uri = Column(String(1000), nullable=True)
    vote = Column(Integer, nullable=True)
    answer = Column(Integer, nullable=True)
    view = Column(Integer, nullable=True)
    date = Column(Date, nullable=True)

    def __init__(self, title=None, uri=None, user_uri=None, vote=None, answer=None, view=None, date=None):
        self.title = title
        self.uri = uri
        self.user_uri = user_uri
        self.vote = vote
        self.answer = answer
        self.view = view
        self.date = date
