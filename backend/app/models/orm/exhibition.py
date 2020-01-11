from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.orm.base import Base

from app.application import db

class Exhibition(Base):
    __tablename__ = 'exhibitions'

    id = db.Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    galleries = relationship("Gallery", back_populates="exhibition")
