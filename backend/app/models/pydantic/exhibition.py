from pydantic import BaseModel


class ExhibitionBase(BaseModel):
    title: str


class ExhibitionCreate(ExhibitionBase):
    pass


class Exhibition(ExhibitionBase):
    pass
