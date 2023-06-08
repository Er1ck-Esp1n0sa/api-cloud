from fastapi import FastAPI
import model
from config import engine 
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome Home"

app.include_router(router.router, prefix="/registro", tags=["registro"])