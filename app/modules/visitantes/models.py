from app.db.database import Base

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Visitante(Base):
    __tablename__ = "visitantes"
    id = Column(Integer, primary_key=True, index=True)
    idTipoDocumento = Column(Integer, ForeignKey("tipos_documento.id"), nullable=False)
    numDocumento = Column(String(15), unique=True, index=True)
    nombre = Column(String(50))
    apellidoPat = Column(String(35))
    apellidoMat = Column(String(35))
    fechaNac = Column(Date)
    correo = Column(String(255))

    user = relationship("User", back_populates="visitante", uselist=False)