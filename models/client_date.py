from pydantic import BaseModel
from typing import Optional


class Client(BaseModel):
    id: Optional[int] = None
    cliente: str
    contacto: str
    fecha_ingreso: str
    diagnostico: str
    tipo: str
    marca_modelo: str
    estado: str