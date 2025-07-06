from datetime import timedelta, datetime
from jose import jwt
from passlib.context import  CryptContext
from sqlalchemy.orm import Session
from .models import User
from .schemas import RegisterRequest
from app.modules.visitantes.models import Visitante

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "bcYjKpaJCw6VkrFjzlwpELmYJjoEhuOw"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(db: Session, correo: str, password: str):
    user = db.query(User).filter(User.correo == correo).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_user_with_visitante(db: Session, user_data: RegisterRequest):
    if db.query(User).filter(User.correo == user_data.visitante.correo).first():
        raise ValueError("Correo ya registrado")
    if db.query(Visitante).filter(Visitante.numDocumento == user_data.visitante.numDocumento).first():
        raise ValueError("Documento ya registrado")

    # Crear visitante
    visitante = Visitante(
        idTipoDocumento=user_data.visitante.idTipoDoc,
        numDocumento=user_data.visitante.numDocumento,
        nombre=user_data.visitante.nombre,
        apellidoPat=user_data.visitante.apellidoPat,
        apellidoMat=user_data.visitante.apellidoMat,
        fechaNac=user_data.visitante.fechaNac,
        correo=user_data.visitante.correo
    )
    db.add(visitante)
    db.flush()

    hashed_password = get_password_hash(user_data.password)
    user = User(
        correo=user_data.visitante.correo,
        hashed_password=hashed_password,
        visitante_id=visitante.id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user