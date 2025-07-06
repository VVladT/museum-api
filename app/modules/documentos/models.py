from app.db.database import Base
from sqlalchemy import Column, Integer, String

class TipoDocumento(Base):
    __tablename__ = "tipos_documento"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    regex = Column(String(30), nullable=True)