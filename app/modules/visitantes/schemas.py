from pydantic import BaseModel, EmailStr
from datetime import date

class VisitanteRequest(BaseModel):
    idTipoDoc: int
    numDocumento: str
    nombre: str
    apellidoPat: str
    apellidoMat: str
    fechaNac: date
    correo: EmailStr

    class Config:
        orm_mode: True

class VisitanteResponse(BaseModel):
    tipoDocumento: str
    numDocumento: str
    nombre: str
    apellidoPat: str
    apellidoMat: str
    fechaNac: date
    correo: EmailStr

    class Config:
        orm_mode: True