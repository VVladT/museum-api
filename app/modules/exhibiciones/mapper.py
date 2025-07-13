from app.modules.exhibiciones.models import Exhibicion
from app.modules.exhibiciones.schemas import ExhibicionResponse


def map_exhibicion(exhibicion: Exhibicion):
    return ExhibicionResponse(
        id=exhibicion.id,
        nombre=exhibicion.nombre,
        categoria=exhibicion.categoria.nombre,
        descripcion=exhibicion.descripcion
    )

def map_exhibiciones(exhibiciones: list[Exhibicion]) -> list[ExhibicionResponse]:
    return [map_exhibicion(e) for e in exhibiciones]
