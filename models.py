from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    cedula = Column(String, unique=True, index=True)
    telefono = Column(String)
    email = Column(String, unique=True, index=True)

    citas = relationship("Cita", back_populates="paciente")

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    especialidad = Column(String, index=True)
    telefono = Column(String)
    email = Column(String, unique=True, index=True)

    citas = relationship("Cita", back_populates="medico")

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    fecha_hora = Column(DateTime, default=datetime.datetime.utcnow)
    motivo = Column(String)
    estado = Column(String, default="Programada") # Ej: Programada, Cancelada, Realizada

    paciente = relationship("Paciente", back_populates="citas")
    medico = relationship("Medico", back_populates="citas")