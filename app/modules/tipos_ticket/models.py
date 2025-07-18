from sqlalchemy import Integer, String, Float, Column

from app.db.database import Base


class TipoTicket(Base):
    __tablename__ = "tipos_ticket"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    precio = Column(Float, nullable=False)