from pydantic import BaseModel


class CharacterBase(BaseModel):

    name: str = None
    height: int = 0
    mass: int = 0
    hair_color: str = None
    skin_color: str = None
    eye_color: str = None
    birth_year: int = 0


class CharacterId(BaseModel):
    id: int


class Character(CharacterBase):
    """Used when reading data, when returning it from the API."""

    class Config:
        """Tell the Pydantic model to read the data even if it is not a dict."""

        orm_mode = True
