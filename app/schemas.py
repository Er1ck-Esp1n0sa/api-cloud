from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
import datetime

T = TypeVar('T')

class InteracionSchema(BaseModel):
    id: Optional[int]=None

class SensorSchema(BaseModel):
    id: Optional[int]=None
    num_serie: int
    estado = str

class LocalizacionSchema(BaseModel):
    id: Optional[int]=None
    latitud: int
    longitud: int
    descripcion: str

class Registro_userSchema(BaseModel):
    id: Optional[int]=None
    edad: int
    sexo: str
    enfermedad_respiratoria: str

class RegistroLocSchema(LocalizacionSchema):
    id: Optional[int]=None
    id_localizacion: LocalizacionSchema
    feha: datetime.datetime
    hora: datetime.datetime
    observacion: str
    
class RegistroSchema(BaseModel):
    id: Optional[int]=None
    id_sensor: SensorSchema
    id_localizacion: LocalizacionSchema
    so: Optional[float]=None
    no2: Optional[float]=None
    co2: Optional[float]=None
    o3: Optional[float]=None
    pst: Optional[float]=None

    class Config:
        orm_mode = True

class RequestRegistro(BaseModel):
    parameter: RegistroSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status : str 
    message: str
    result: Optional[T]
