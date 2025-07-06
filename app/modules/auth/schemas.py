from pydantic import BaseModel, EmailStr
from app.modules.visitantes.schemas import VisitanteRequest

class RegisterRequest(BaseModel):
    visitante: VisitanteRequest
    password: str

    class Config:
        orm_mode: True

class AuthRequest(BaseModel):
    correo: EmailStr
    password: str

    class Config:
        orm_mode: True

class AuthResponse(BaseModel):
    token: str

    class Config:
        orm_mode: True