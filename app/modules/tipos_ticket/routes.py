from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import TipoTicketResponse
from .service import get_all
from app.shared.dependencies import get_db

router = APIRouter(prefix="/tipos-ticket", tags=["Tipos-Ticket"])

@router.get("", response_model=list[TipoTicketResponse])
def get_tipos_ticket(db: Session = Depends(get_db)):
    return get_all(db)
