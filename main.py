# -*-coding:utf-8 -*-
from fastapi import FastAPI,File, UploadFile
from model import files as fileM
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request



app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

@app.get("/file/{typess}")
def get_files(typess:str):
    return fileM.get_file(types=typess)

@app.post("/upload/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    rt = {"path":[]}
    for file in files:
        print(file.filename)
        file_data = await file.read()
        #print(len(file_data))
        save_file = fileM.save_file(filename=file.filename,filedata=file_data)
        rt["path"].append(save_file["path"])
    return rt

@app.get("/download/")
def download_file(url:str):
    m_gets = fileM.download_file(url)
    #print(m_gets)
    return m_gets

@app.get("/allfiles/")
def all_files():
    #print(fileM.get_all_file)
    return fileM.get_all_file()

@app.get("/delfile")
def del_file(name:str,tag:str):
    request = fileM.del_file(name=name,types=tag)
    return request

