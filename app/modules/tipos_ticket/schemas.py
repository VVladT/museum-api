from pydantic import BaseModel


class TipoTicketResponse(BaseModel):
    id: int
    nombre: str
    precio: float
