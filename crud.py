from sqlalchemy.orm import Session
import models, schemas

# --- CRUD para Pacientes ---
def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

# --- CRUD para Médicos ---
def get_medico(db: Session, medico_id: int):
    return db.query(models.Medico).filter(models.Medico.id == medico_id).first()

def get_medicos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medico).offset(skip).limit(limit).all()

def create_medico(db: Session, medico: schemas.MedicoCreate):
    db_medico = models.Medico(**medico.dict())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

# --- CRUD para Citas ---
def get_cita(db: Session, cita_id: int):
    return db.query(models.Cita).filter(models.Cita.id == cita_id).first()

def get_citas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cita).offset(skip).limit(limit).all()

def create_cita(db: Session, cita: schemas.CitaCreate):
    db_cita = models.Cita(**cita.dict())
    # Aquí se podrían añadir validaciones (ej. no agendar dos citas a la misma hora)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita