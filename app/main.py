import uvicorn
from fastapi import FastAPI
from app.characters.routes import router as characters_routes
from app.database import create_db_and_tables, close_session

descrption = """
CharactersApp API helps load, find and remove characters with their personal information.

## Items

You can **load new characters**, **read characters info** and **remove characters**.

## Users

You will be able to:

* **Create characters** (implemented).
* **Read all characters** (implemented).
* **Find character by ID** (implemented).
* **Remove character in DB by ID** (implemented).

"""
app = FastAPI(
    title="CharactersApp",
    description=descrption,
    version="0.1",
)


@app.get("/")
def root():
    """Show base url."""
    return {"message": "Hello to the Character API"}


@app.on_event("startup")
async def startup_event():
    """Start DB"""
    create_db_and_tables()


@app.on_event("shutdown")
async def shutdown():
    """Close connection DB"""
    close_session()


# mounting routes
app.include_router(characters_routes)

if __name__ == "__main__":
    # Init APP
    uvicorn.run(app, host="0.0.0.0", port=8000)
