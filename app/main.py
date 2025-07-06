from fastapi import FastAPI
from .modules.auth.routes import router as auth_router
from .db.database import Base, engine
from app.modules.auth.models import *
from app.modules.documentos.models import *
from app.modules.exhibiciones.models import *
from app.modules.tickets.models import *
from app.modules.visitantes.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MuseumAPI")

app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}