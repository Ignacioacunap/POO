from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import CREDS

# Construcción de la URL de conexión
URL = f"mysql+mysqlconnector://{CREDS['user']}:{CREDS['pass']}@{CREDS['host']}:{CREDS['port']}/{CREDS['db']}"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def guardar_cambios(entidad):
    """Función genérica para persistir datos con rollback automático en caso de error."""
    try:
        db.add(entidad)
        db.commit()
        db.refresh(entidad)
        return entidad.id
    except Exception as e:
        db.rollback()
        # Se podría loguear el error aquí si fuera necesario
        return None

def traer_todos(modelo):
    return db.query(modelo).all()

def buscar_uno(modelo, **filtros):
    return db.query(modelo).filter_by(**filtros).first()