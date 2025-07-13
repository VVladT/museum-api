from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Exhibicion(Base):
    __tablename__ = "exhibiciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    descripcion = Column(String(255), nullable=False)

    categoria = relationship("Categoria", backref="exhibiciones")