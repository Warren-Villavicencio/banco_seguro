from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy import String, Integer, Column, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pyngrok import ngrok  
from fastapi.responses import JSONResponse 



URL_DATABASE = "mysql+pymysql://root:@localhost:3306/banco_seguro"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Ingreso(Base):
    __tablename__ = "cuentabancaria"
    id = Column(Integer, primary_key=True, autoincrement=True)
    numerodecuenta = Column(String(20))
    titular = Column(String(100))
    tarjeta_de_debito = Column(String(16))
    clavetarjeta = Column(String(4))
    correoelectronico = Column(String(100))
    claveanterior = Column(String(20))
    clavenueva = Column(String(20))
    saldo = Column(Float)


class RetiroBase(BaseModel):
    numerodecuenta: str
    monto: float   
    

    


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


app = FastAPI()

def start_ngrok():
    url = ngrok.connect(8000)  
    print(f'ngrok tunnel "http://127.0.0.1:8000" -> "{url}"')



@app.get("/")
def read_root():
    return {"Bienvenidos a Banco Seguro Desarrollado por: Warren Antonio Villavicencio Merino"}






@app.post("/retirar/", status_code=status.HTTP_200_OK)
async def retirar_dinero(retiro: RetiroBase, db: db_dependency):
    cuenta = db.query(Ingreso).filter(Ingreso.numerodecuenta == retiro.numerodecuenta).first()
    if cuenta is None:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    if cuenta.saldo < retiro.monto:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    cuenta.saldo -= retiro.monto
    db.commit()
    return {"mensaje": "Retiro realizado exitosamente", "saldo_actual": cuenta.saldo}

if __name__ == "__main__":
    
    start_ngrok()
    
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)