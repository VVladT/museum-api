from pydantic import BaseModel, EmailStr
from app.modules.visitantes.schemas import VisitanteRequest

class RegisterRequest(BaseModel):
    visitante: VisitanteRequest
    password: str

class AuthRequest(BaseModel):
    correo: EmailStr
    password: str

class AuthResponse(BaseModel):
    token: str