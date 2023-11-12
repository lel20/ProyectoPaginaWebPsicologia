#Librerías
from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI() #Se invoca a la clase FastApi()

#Se define una variable que indique donde se encuentran las plantillas
template =Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def raiz(request: Request):
    return template.TemplateResponse("index.html",{"request":request})
@app.get("/sobremi")
def sobreMi(request: Request):
    return template.TemplateResponse("sobreMi.html",{"request":request})