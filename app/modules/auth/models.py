from app.db.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(80), nullable=False)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"), unique=True, nullable=True)

    visitante = relationship("Visitante", back_populates="user")