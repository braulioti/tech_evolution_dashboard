from sqlalchemy import Column, Integer, ForeignKey

from src import Model

class DataTag(Model):
    __tablename__ = "data_tag"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    data_id = Column(Integer, ForeignKey("data.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tag.id"), nullable=False)

    def __init__(self, data_id, tag_id):
        self.data_id = data_id
        self.tag_id = tag_id
