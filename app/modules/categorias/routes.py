from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.modules.categorias.schemas import CategoriaResponse
from app.modules.categorias.service import get_all
from app.shared.dependencies import get_db

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("", response_model=list[CategoriaResponse])
def get_categorias(db: Session = Depends(get_db)):
    return get_all(db)