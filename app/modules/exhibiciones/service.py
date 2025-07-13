from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.modules.exhibiciones.mapper import map_exhibicion, map_exhibiciones
from app.modules.exhibiciones.models import Exhibicion


def get_by_id(id: int, db: Session):
    exhibicion = db.query(Exhibicion).options(joinedload(Exhibicion.categoria)).get(id)
    if not exhibicion:
        raise HTTPException(status_code=404, detail="Exhibición no encontrada")
    return map_exhibicion(exhibicion)

def get_all(db: Session):
    exhibiciones = db.query(Exhibicion).options(joinedload(Exhibicion.categoria)).all()
    return map_exhibiciones(exhibiciones)