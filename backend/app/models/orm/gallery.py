from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.orm.base import Base

class Gallery(Base):
    title = Column(String, index=True)
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))

    exhibition = relationship("Exhibition", back_populates="galleries")
    images = relationship("GalleryImage", back_populates="gallery")
