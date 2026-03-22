from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

# --- Reconciliation Schemas ---
class PatientContext(BaseModel):
    age: int
    conditions: List[str]
    recent_labs: Dict[str, Any]

class MedSource(BaseModel):
    system: str
    medication: str
    last_updated: Optional[str] = None
    last_filled: Optional[str] = None
    source_reliability: str

class ReconcileRequest(BaseModel):
    patient_context: PatientContext
    sources: List[MedSource]

# --- Validation Schemas ---
class ValidationRequest(BaseModel):
    demographics: Dict[str, Any]
    medications: List[str]
    allergies: List[str]
    conditions: List[str]
    vital_signs: Dict[str, Any]
    last_updated: str
