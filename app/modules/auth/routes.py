from fastapi import APIRouter, HTTPException, Depends
from .service import create_user_with_visitante, create_access_token, authenticate_user
from .schemas import AuthResponse, AuthRequest, RegisterRequest
from sqlalchemy.orm import Session

from app.shared.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=AuthResponse)
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = create_user_with_visitante(db, user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    token = create_access_token({"sub": user.correo})
    return AuthResponse(token=token)

@router.post("/login", response_model=AuthResponse)
def login(auth_data: AuthRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, auth_data.correo, auth_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token({"sub": user.correo})
    return AuthResponse(token=token)