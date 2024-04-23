# APIRouter creates path operations for item module
from fastapi import HTTPException, APIRouter
from .crud import select_all_users, select_user, insert_character, delete_character
from .schemas import CharacterId, CharacterBase
from app.database import get_session

router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404: {"message": "Not Found"}},
)


@router.get("/character/getAll")
def return_all_characters():
    # TODO: generar json de respuesta
    result = select_all_users(get_session())
    if result is None:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return {"message": f"{result}"}


@router.post("/character/getCharacter/{CharacterId}")
def read_character(id: CharacterId):
    # TODO: identificar forma de saber si el personaje existe o no en la DB
    result = select_user(get_session(), id)
    if result is None:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return {"message": f"{result}"}


@router.post("/character/add")
def create_character(character: CharacterBase):
    # TODO: validar y confirmar si se desea ingresar usuario repetido.
    # TODO: Validar datos que se intentan ingresar
    result = insert_character(get_session(), character)
    if result:
        message = result
    else:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return {"message": message}


@router.delete("/character/delete/{CharacterId}")
def delete_character_by_id(id: CharacterId):
    # TODO: validar respuesta teniendo en cuenta si el ID existe o no y si borro o no
    result = delete_character(get_session(), id)
    if result is False:
        raise HTTPException(status_code=400, detail="HTTP Code 400 - Bad Request")
    return {"message": f"{result}"}
