from pydantic import BaseModel


class CharacterBase(BaseModel):
    """Base model representing the core attributes of a character.
    Attributes:
        name (str): The name of the character.
        height (int): The height of the character in centimeters.
        mass (int): The mass of the character in kilograms.
        hair_color (str): The color of the character's hair.
        skin_color (str): The color of the character's skin.
        eye_color (str): The color of the character's eyes.
        birth_year (int): The birth year of the character.
    """

    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int


class Character(CharacterBase):
    """Model representing a character with an additional identifier.

    Attributes:
        id (int): The unique identifier of the character.
    """

    id: int

    class Config:
        orm_mode = True


class CharactersOut(BaseModel):
    """Output model representing selected attributes of a character.

    Attributes:
        id (int): The unique identifier of the character.
        name (str): The name of the character.
        height (int): The height of the character in centimeters.
        mass (int): The mass of the character in kilograms.
        birth_year (int): The birth year of the character.
        eye_color (str): The color of the character's eyes.
    """

    id: int
    name: str
    height: int
    mass: int
    birth_year: int
    eye_color: str

    class Config:
        orm_mode = True
