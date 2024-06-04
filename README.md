# banco_seguro

El programa se desarrollo en Python y se utilizo las siguientes dependencias

FastAPI: Framework  para construir APIs con Python.
Uvicorn: Servidor ASGI para ejecutar la aplicación FastAPI.
Pydantic: Para la validación y gestión de datos basados en modelos de Python.
SQLAlchemy: Un ORM para interactuar con la base de datos.
PyMySQL: Un adaptador de base de datos MySQL para Python.
ngrok: Para que la base de datos tenga salida al exterior 

Para que el programa funcione correctamente se debe instalar lo siguiente:

PREPARACIÓN DEL ENTORNO EN AWS CDK

Desde la terminal de WINDOWS se debe hacer la configuración con los siguientes comandos: 

1.	aws configure                                                                                                   
2.	aws s3 ls
3.	npm install -g aws-cdk  
4.	cdk bootstrap


CONFIGURACIÓN DEL ENTORNO IDE VISULACODE

Desde la terminal de VISUALCODE se debe hacer la configuración con los siguientes comandos: 

1.	Ls
2.	Cdk init
3.	cdk init  --language python     
4.	. .venv\Scripts\Activate   
5.	pip install -r  requirements.txt                      
6.	Cdk deploy


COMANDOS PARA INSTALAR LAS DEPENDENCIAS NECESARIAS:

pip install fastapi uvicorn pydantic sqlalchemy pymysql pyngrok

COMANDOS PARA EJECUTAR LOS DIFERENTES SCRIPTS:

uvicorn bsretirar:app --reload      
uvicorn bsdepositar:app --reload      
uvicorn bscambiar_claver:app --reload    

CREAR UNA BASE DE DATOS EN MYSQ LLAMADA BANCO_SEGURO

Nombre de la tabla:  cuentabancaria
Nombre de los campos:
    id = Column(Integer, primary_key=True, autoincrement=True)
    numerodecuenta = Column(String(20))
    titular = Column(String(100))
    tarjeta_de_debito = Column(String(16))
    clavetarjeta = Column(String(4))
    correoelectronico = Column(String(100))
    claveanterior = Column(String(20))
    clavenueva = Column(String(20))
    saldo = Column(Float)


