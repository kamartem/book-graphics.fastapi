from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from ..models.orm.exhibition import Exhibition as ORMExhibition
from ..models.pydantic.exhibition import Exhibition, ExhibitionCreate

router = APIRouter()


# @router.get("/", response_model=List[Exhibition], name="exhibitions:all")
# def retrieve_exhibitions(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(ORMExhibition).offset(skip).limit(limit).all()


@router.get("/{id}", response_model=Exhibition, name="exhibitions:detail")
async def retrieve_exhibition(id: int):
    exhibition: ORMExhibition = await ORMExhibition.get(id)
    return Exhibition.from_orm(exhibition)


# @router.post("/", response_model=Exhibition, name="exhibitions:create")
# def create_exhibition(db: Session, exhibition: serializers.ExhibitionCreate):
#     db_exhibition = ORMExhibition(**exhibition.dict())
#     db.add(db_exhibition)
#     db.commit()
#     db.refresh(db_exhibition)
#     return db_exhibition
