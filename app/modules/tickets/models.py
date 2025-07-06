from app.db.database import Base
from sqlalchemy import Column, Integer, String, Float

class TipoTicket(Base):
    __tablename__ = "tipos_ticket"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    precio = Column(Float, nullable=False)