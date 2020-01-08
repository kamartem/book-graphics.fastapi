from sqlalchemy.orm import Session

from . import models, schemas


def get_exhibition(db: Session, exhibition_id: int):
    return db.query(models.Exhibition).filter(models.Exhibition.id == exhibition_id).first()


def get_exhibitions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exhibition).offset(skip).limit(limit).all()


def create_exhibition(db: Session, exhibition: schemas.ExhibitionCreate):
    db_exhibition = models.Exhibition(**exhibition.dict())
    db.add(db_exhibition)
    db.commit()
    db.refresh(db_exhibition)
    return db_exhibition
