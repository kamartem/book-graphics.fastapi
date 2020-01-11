from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.orm.base import Base

class GalleryImage(Base):
    title = Column(String, index=True)
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))

    gallery = relationship("Gallery", back_populates="images")
