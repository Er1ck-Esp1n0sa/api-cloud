from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RegistroSchema, RequestRegistro, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestRegistro,db:Session=Depends(get_db)):
    crud.create_registro(db, registro=request.parameter)
    return Response(code=200,status= "ok",message="resgistro creado").dict(exclude_none=True)


@router.get("/get")
async def get(db:Session=Depends(get_db)):
    _registro = crud.get_registro(db, 0, 100)
    return Response(code=200, status="ok", message="datos optenidos", result=_registro).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _registro = crud.get_registro_by_id(db, id)
    return Response(code=200, status="ok", message="datos optenidos", result=_registro).dict(exclude_none=True)


@router.post("/update")
async def update_registro(request:RequestRegistro ,db:Session=Depends(get_db)):
    _registro = crud.updat_registro(db, registro_id=request.parameter.id,
                                    so=request.parameter.so, no2=request.parameter.no2, co2=request.parameter.co2, o3=request.parameter.o3, pst=request.parameter.pst)
    return Response(code=200, status="ok", message="datos modificados", result=_registro)

@router.delete("/delete{id}")
async def delete(id:int,db:Session=Depends(get_db)):
    crud.remove_registro(db,registro_id=id)
    return Response(code=200, status="ok", message="datos eliminados").dict(exclude_none=True)
