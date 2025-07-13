from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import TipoDocumentoResponse
from .service import get_all
from app.shared.dependencies import get_db

router = APIRouter(prefix="/documentos", tags=["Documentos"])

@router.get("", response_model=list[TipoDocumentoResponse])
def get_documentos(db: Session = Depends(get_db)):
    return get_all(db)