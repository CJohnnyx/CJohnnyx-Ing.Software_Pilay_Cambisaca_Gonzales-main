from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import crud, models, schemas
from database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Gestion de Citas Medicas",
    description="Backend para un sistema de citas medicas utilizando FastAPI.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE","OPTIONS"],
    allow_headers=["Authorization","Content-Type"],
)

# Crea las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

# --- Endpoints para Pacientes ---
@app.post("/pacientes/", response_model=schemas.Paciente, tags=["Pacientes"])
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.create_paciente(db=db, paciente=paciente)

@app.get("/pacientes/", response_model=List[schemas.Paciente], tags=["Pacientes"])
def read_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes

@app.get("/pacientes/{paciente_id}", response_model=schemas.Paciente, tags=["Pacientes"])
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente

# --- Endpoints para MÃ©dicos ---
@app.post("/medicos/", response_model=schemas.Medico, tags=["Medicos"])
def create_medico(medico: schemas.MedicoCreate, db: Session = Depends(get_db)):
    return crud.create_medico(db=db, medico=medico)

@app.get("/medicos/", response_model=List[schemas.Medico], tags=["Medicos"])
def read_medicos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medicos = crud.get_medicos(db, skip=skip, limit=limit)
    return medicos

# --- Endpoints para Citas ---
@app.post("/citas/", response_model=schemas.Cita, tags=["Citas"])
def create_cita(cita: schemas.CitaCreate, db: Session = Depends(get_db)):
    # Validar que el paciente y el mÃ©dico existen
    paciente = crud.get_paciente(db, paciente_id=cita.paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail=f"Paciente con id {cita.paciente_id} no encontrado")
    
    medico = crud.get_medico(db, medico_id=cita.medico_id)
    if not medico:
        raise HTTPException(status_code=404, detail=f"Medico con id {cita.medico_id} no encontrado")

    return crud.create_cita(db=db, cita=cita)

@app.get("/citas/", response_model=List[schemas.Cita], tags=["Citas"])
def read_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    citas = crud.get_citas(db, skip=skip, limit=limit)
    return citas