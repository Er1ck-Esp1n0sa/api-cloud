from sqlalchemy.orm import Session
from model import Registro
from schemas import RegistroSchema

# optener todos los registro
def get_registro(db:Session, skip: int=0, limit:int=100):
    return db.query(Registro).offset(skip).limit(limit).all()

# optener registros por id
def get_registro_by_id(db:Session, registro_id: int):
    return db.query(Registro).filter(Registro.id == registro_id).first()


# crear registro
def create_registro(db:Session, registro: RegistroSchema):
    _registro = Registro(so=registro.so, no2=registro.no2, co2=registro.co2, o3=registro.o3, pst=registro.pst)
    db.add(_registro)
    db.commit()
    db.refresh()
    return _registro

# eliminar registro
def remove_registro(db:Session, registro_id:int):
    _registro = get_registro_by_id(db=db,registro_id=registro_id)
    db.delete(_registro)
    db.commit()

# modificar registro
def updat_registro(db:Session, registro_id:int, so:float, no2:float, co2:float, o3:float, pst:float):
    _registro = get_registro_by_id(db=db,registro_id=registro_id)
    _registro.so = so
    _registro.no2 = no2
    _registro.co2 = co2
    _registro.o3 = o3
    _registro.pst = pst
    db.commit()
    db.refresh(_registro)
    return _registro