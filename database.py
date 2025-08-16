from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# --- CONFIGURACIÓN PARA POSTGRESQL ---
# Reemplaza los valores con tus credenciales de PostgreSQL.
# Formato: "postgresql://usuario:contraseña@host:puerto/nombre_basedatos"
SQLALCHEMY_DATABASE_URL = "sqlite:///./citas_medicas.db"

# El motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Creación de una sesión local para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos declarativos de SQLAlchemy
Base = declarative_base()

# Función para obtener una sesión de base de datos en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()