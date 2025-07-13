from fastapi import FastAPI
from .modules.auth.routes import router as auth_router
from .modules.documentos.routes import router as documentos_router
from .modules.tipos_ticket.routes import router as tipos_ticket_router
from .modules.categorias.routes import router as categorias_router
from .modules.exhibiciones.routes import router as exhibiciones_router

app = FastAPI(title="MuseumAPI")

app.include_router(auth_router)
app.include_router(documentos_router)
app.include_router(tipos_ticket_router)
app.include_router(categorias_router)
app.include_router(exhibiciones_router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}