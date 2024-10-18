from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [ 1,2,3]

@app.get('/contact')
def get_list():
    return {"name":'Platzi'}

@app.get('/html',response_class=HTMLResponse)
def get_list():
    return """ SOY UN HTML """
