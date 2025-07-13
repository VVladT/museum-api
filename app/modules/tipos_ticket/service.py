from sqlalchemy.orm import Session

from app.modules.tipos_ticket.models import TipoTicket


def get_all(db: Session):
    return db.query(TipoTicket).all()