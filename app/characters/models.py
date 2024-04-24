from sqlalchemy import Column, Integer, String
from app.database import Base


class Character(Base):
    """SQLAlchemy model to represent a character in the database.
        This class defines the structure of the 'characters' table in the database,
        which stores information about characters.

    Attributes:
        id (int): The unique identifier of the character (clave primaria de la tabla).
        name (str): The name of the character.
        height (int): The height of the character in centimeters.
        mass (int): The mass of the character in kilograms.
        hair_color (str): The color of the character's hair.
        skin_color (str): The color of the character's skin.
        eye_color (str): The color of the character's eyes.
        birth_year (int): The birth year of the character.
        __tablename__: Name of table in DB
    """

    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
