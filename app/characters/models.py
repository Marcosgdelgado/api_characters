from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Character(Base):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    height: Mapped[int]
    mass: Mapped[int]
    hair_color: Mapped[str]
    skin_color: Mapped[str]
    eye_color: Mapped[str]
    birth_year: Mapped[int]
