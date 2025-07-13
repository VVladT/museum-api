from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)