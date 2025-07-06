from app.db.database import Base
from sqlalchemy import Column, Integer, String

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)