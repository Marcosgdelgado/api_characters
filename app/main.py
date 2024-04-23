import uvicorn
from fastapi import FastAPI
from app.characters.routes import router as characters_routes
from app.database import initialize_db, close_session

app = FastAPI()


@app.get("/")
def root():
    """Show base url."""
    return {"message": "Hello to the Character API"}


@app.on_event("startup")
async def startup_event():
    initialize_db()


@app.on_event("shutdown")
async def shutdown():
    close_session()


app.include_router(characters_routes)

if __name__ == "__main__":
    # Inicia API
    uvicorn.run(app, host="0.0.0.0", port=8000)
