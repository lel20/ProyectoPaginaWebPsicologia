#Librerías
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def presntar():
    return "Hola mundo"