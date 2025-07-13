from sqlalchemy.orm import Session

from app.modules.categorias.models import Categoria


def get_all(db: Session):
    return db.query(Categoria).all()