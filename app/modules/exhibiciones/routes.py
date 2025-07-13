from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import ExhibicionResponse
from .service import get_all, get_by_id
from app.shared.dependencies import get_db

router = APIRouter(prefix="/exhibiciones", tags=["Exhibiciones"])

@router.get("", response_model=list[ExhibicionResponse])
def get_exhibiciones(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{id}", response_model=ExhibicionResponse)
def get_exhibicion(id: int, db: Session = Depends(get_db)):
    return get_by_id(id, db)