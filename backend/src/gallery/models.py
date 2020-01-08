from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Exhibition(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    galleries = relationship("Gallery", back_populates="exhibition")


class Gallery(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))

    exhibition = relationship("Exhibition", back_populates="galleries")
    images = relationship("GalleryImage", back_populates="gallery")


class GalleryImage(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))

    gallery = relationship("Gallery", back_populates="images")
