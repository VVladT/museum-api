from pydantic import BaseModel

class ExhibicionRequest(BaseModel):
    nombre: str
    idCategoria: int
    descripcion: str

class ExhibicionResponse(BaseModel):
    id: int
    nombre: str
    categoria: str
    descripcion: str
