from app.db.database import Base
from sqlalchemy import Column, Integer, ForeignKey


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    tipo_id = Column(Integer, ForeignKey("tipos_ticket.id"), unique=True, nullable=True)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"), unique=True, nullable=True)
    comprador_id = Column(Integer, ForeignKey("visitantes.id"), unique=True, nullable=True)