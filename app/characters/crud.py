import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import Character
from .schemas import CharacterBase


def insert_character(db: Session, character: CharacterBase) -> None:
    try:
        db.add(Character(**character.__dict__))
        db.commit()
        return character.__dict__
    except SQLAlchemyError:
        return False


def select_user(db: Session, id: int) -> sa.engine.Result:
    try:
        consult = db.query(Character).filter(Character.id == id.id).first()
        if consult:
            return consult.__dict__
    except SQLAlchemyError:
        return None


def select_all_users(db: Session) -> sa.engine.Result:
    try:
        results = db.query(
            Character.id,
            Character.name,
            Character.height,
            Character.mass,
            Character.birth_year,
            Character.eye_color,
        ).all()
        return results
    except SQLAlchemyError:
        return None


def delete_character(db: Session, id):
    try:
        character = db.query(Character).filter(Character.id == id.id).first()
        if not character:
            return False
        db.delete(character)
        db.commit()
        return True
    except SQLAlchemyError:
        return False
