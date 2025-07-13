from sqlalchemy.orm import Session

from .models import TipoDocumento


def get_all(db: Session):
    return db.query(TipoDocumento).all()