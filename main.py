# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
app.counter = 0

class PatientRq(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: str
    patient: dict


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/patient")
def create_patient(rq: PatientRq):
    app.counter += 1
    return PatientResp(id=str(app.counter), patient=rq.dict())

@app.get("/patient/{pk}")
def patient_finder(pk):
    if pk > app.counter:
        raise HTTPException(status_code=404, detail="Item not found")
    return PatientRq

