from pydantic import BaseModel
from typing import Optional

class ExhibicionRequest(BaseModel):
    nombre: str
    idCategoria: int
    descripcion: Optional[str]

class ExhibicionResponse(BaseModel):
    nombre: str
    categoria: str
    descripcion: str

class CategoriaResponse(BaseModel):
    id: int
    nombre: str