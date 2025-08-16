from pydantic import BaseModel
from typing import List, Optional
import datetime

# --- Esquemas para Paciente ---
class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    telefono: Optional[str] = None
    email: str

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int

    class Config:
        orm_mode = True

# --- Esquemas para Medico ---
class MedicoBase(BaseModel):
    nombre: str
    apellido: str
    especialidad: str
    telefono: Optional[str] = None
    email: str

class MedicoCreate(MedicoBase):
    pass

class Medico(MedicoBase):
    id: int

    class Config:
        orm_mode = True

# --- Esquemas para Cita ---
class CitaBase(BaseModel):
    paciente_id: int
    medico_id: int
    fecha_hora: datetime.datetime
    motivo: Optional[str] = None
    estado: str = "Programada"

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: int
    paciente: Paciente
    medico: Medico

    class Config:
        orm_mode = True