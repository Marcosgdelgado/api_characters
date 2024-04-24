# APIRouter creates path operations for item module
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from .crud import select_all_users, select_user, insert_character, delete_character
from .schemas import CharacterBase, Character, CharactersOut
from app.database import get_session

router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404: {"message": "Not Found"}},
)


@router.get("/character/getAll", response_model=list[CharactersOut])
def return_all_characters(db: Session = Depends(get_session)) -> list[CharactersOut]:
    """Show all characters loaded in the DB.

    Args:
        db (Session, optional): DB session object. Defaults to Depends(get_session).

    Raises:
        HTTPException: If query consult doesn't found raise a 400 error.

    Returns:
        list[CharactersOut]: List with result of query consult.
    """
    result = select_all_users(db)
    if result is None:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return result


@router.get("/character/get/{id}", response_model=Character)
def find_character(id: int, db: Session = Depends(get_session)) -> Character:
    """Find  character by ID.

    Args:
        id (int): Character ID
        db (Session, optional): DB session object. Defaults to Depends(get_session).

    Raises:
        HTTPException: If query consult doesn't found raise a 400 error.

    Returns:
        Character: Character object with  data founded.
    """
    result = select_user(db, id)
    if result is None:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return result


@router.post("/character/add", response_model=CharacterBase)
def create_character(character: CharacterBase, db: Session = Depends(get_session)) -> CharacterBase:
    """Add new character in DB.

    Args:
        character (CharacterBase): schema with needed info for new character.
        db (Session, optional): DB session object. Defaults to Depends(get_session).

    Raises:
        HTTPException: If query consult doesn't found raise a 400 error.

    Returns:
        CharacterBase: Character info after add it in DB.
    """
    result = insert_character(db, character)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")


@router.delete("/character/delete/{id}", response_model=Character)
def delete_character_by_id(id: int, db: Session = Depends(get_session)) -> Character:
    """Delete character in DB by ID

    Args:
        id (int): Character ID
        db (Session, optional): DB session object. Defaults to Depends(get_session).

    Raises:
        HTTPException: If query consult doesn't found raise a 400 error.

    Returns:
        Character: Info of character deleted
    """
    result = delete_character(db, id)
    if result is False:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return result
