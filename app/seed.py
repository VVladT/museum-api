from datetime import date

from sqlalchemy import text

from app.db.database import SessionLocal, Base, engine
from app.modules.auth.models import User
from app.modules.auth.service import get_password_hash
from app.modules.categorias.models import Categoria
from app.modules.documentos.models import TipoDocumento
from app.modules.exhibiciones.models import Exhibicion
from app.modules.tipos_ticket.models import TipoTicket

from app.modules.visitantes.models import Visitante

def reset_database():
    with engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
        Base.metadata.drop_all(bind=conn)
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
    Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()

    # Tipos de documento
    if not db.query(TipoDocumento).first():
        documentos = [
            TipoDocumento(nombre="DNI", regex=r"^\d{8}$"),
            TipoDocumento(nombre="Pasaporte", regex=r"^[A-Z0-9]{6,9}$"),
        ]
        db.add_all(documentos)
        db.commit()

    # Verifica si ya existe el visitante por documento
    num_doc = "12345678"
    correo = "juan@correo.com"

    visitante = db.query(Visitante).filter_by(numDocumento=num_doc).first()
    if not visitante:
        visitante = Visitante(
            idTipoDocumento=1,  # asegúrate que este valor exista
            numDocumento=num_doc,
            nombre="Juan",
            apellidoPat="Pérez",
            apellidoMat="Gómez",
            fechaNac=date(1990, 5, 20),
            correo=correo
        )
        db.add(visitante)
        db.commit()
        db.refresh(visitante)

    # Verifica si ya existe el usuario por correo
    user = db.query(User).filter_by(correo=correo).first()
    if not user:
        hashed_password = get_password_hash("123456")
        user = User(
            correo=correo,
            hashed_password=hashed_password,
            visitante_id=visitante.id
        )
        db.add(user)
        db.commit()

    # Categorías
    if not db.query(Categoria).first():
        categorias = [
            Categoria(nombre="Arte"),
            Categoria(nombre="Ciencia"),
            Categoria(nombre="Historia"),
        ]
        db.add_all(categorias)
        db.commit()

    # Exhibiciones
    if not db.query(Exhibicion).first():
        categorias = db.query(Categoria).all()

        exhibiciones = [
            Exhibicion(
                nombre="Renacimiento",
                descripcion="Pinturas europeas del siglo XV",
                categoria_id=categorias[0].id  # Arte
            ),
            Exhibicion(
                nombre="Robótica",
                descripcion="Historia de la automatización",
                categoria_id=categorias[1].id  # Ciencia
            ),
            Exhibicion(
                nombre="Imperios antiguos",
                descripcion="Egipto, Roma y más",
                categoria_id=categorias[2].id  # Historia
            ),
        ]

        db.add_all(exhibiciones)
        db.commit()

    # Tipos de ticket
    if not db.query(TipoTicket).first():
        tickets = [
            TipoTicket(nombre="Adulto", precio=20.0),
            TipoTicket(nombre="Menor de edad", precio=10.0),
            TipoTicket(nombre="Universitario", precio=15.0),
            TipoTicket(nombre="Entrada Libre", precio=0.0)
        ]
        db.add_all(tickets)
        db.commit()

    db.close()
    print("✅ Seed ejecutado con éxito")

if __name__ == "__main__":
    reset_database()
    seed()