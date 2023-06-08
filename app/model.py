from sqlalchemy import Column, DateTime, Integer,String, Float, ForeignKey
from config import Base
from sqlalchemy.orm import relationship

class Interacion(Base):
    __tablename__ = 'interacion'
    
    id = Column(Integer, primary_key=True)

class Sensor(Base):
    __tablename__ = 'sensor'
    
    id = Column(Integer, primary_key=True)
    num_serie = Column(Integer)
    estado = Column(String)

class Localizacion(Base):
    __tablename__ = 'localizacion'
    
    id = Column(Integer, primary_key=True)
    latitud = Column(Integer)
    longitud = Column(Integer)
    descripcion = Column(String)

class Registro_user(Base):
    __tablename__ = 'registro_user'
    
    id = Column(Integer, primary_key=True)
    edad = Column(Integer)
    sexo = Column(String)
    enfermedad_respiratoria = Column(String)

class Registro_loc(Base):
    __tablename__ = 'registro_loc'

    id = Column(Integer, primary_key=True)
    id_regstro = Column(Integer, ForeignKey('registro_user.id'))
    id_localizacion = Column(Integer, ForeignKey('localizacion.id'))
    feha = Column(DateTime)
    hora = Column(DateTime)
    observacion = Column(String)

class Registro(Base):
    __tablename__ = 'registro'

    id = Column(Integer, primary_key=True)
    id_sensor = Column(Integer, ForeignKey('sensor.id'))
    id_localizacion = Column(Integer, ForeignKey('localizacion.id'))
    so = Column(Float)
    no2 = Column(Float)
    co2 = Column(Float)
    o3 = Column(Float)
    pst = Column(Float)

#Monóxido de azufre (SO)
#Dióxido de nitrógeno (NO2)
#Dióxido de carbono (CO2)
#Ozono (O3)
#Partículas totales en suspensión (PST)