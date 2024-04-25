from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import Character
from .schemas import CharacterBase


def insert_character(db: Session, character: CharacterBase):
    """Add new character in the DB.

    Args:
        db (Session): Session object to interact with the database.
        character (CharacterBase): object with info character.

    Returns:
        CharacterBase or bool: if load successfully the character info, if not False.
    """
    try:
        db.add(Character(**character.__dict__))
        db.commit()
        return character
    except SQLAlchemyError:
        return False


def select_character(db: Session, id: int):
    """Consulta un personaje por su ID.

    Args:
        db (Session): Session object to interact with the database.
        id (int): ID character.

    Returns:
        Character or None: object with found info character, or None if not exist or had a error.
    """
    try:
        consult = db.query(Character).filter(Character.id == id).first()
        if consult:
            return consult
    except SQLAlchemyError:
        return None


def select_all_characters(db: Session):
    """Gets all characters in the database.

    Args:
        db (Session): Session object to interact with the database.

    Returns:
        List[Character] or None: List of all characters, or None if there is an error.
    """
    try:
        return db.query(Character).all()
    except SQLAlchemyError:
        return None


def delete_character(db: Session, id: int):
    """Removes a character from the database by its ID.

    Arguments:
        db (Session): Database session.
        id (int): ID character.

    Returns:
        Character or bool: The character removed if successful, False if not found or fails.
    """
    try:
        character = db.query(Character).filter(Character.id == id).first()
        if not character:
            return False
        db.delete(character)
        db.commit()
        return character
    except SQLAlchemyError:
        return False
