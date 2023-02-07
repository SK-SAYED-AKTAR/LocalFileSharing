from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import shutil
import os



app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/")
def home(request: Request):
    filePath = "./templates/home.html"
    with open(filePath) as f:
        myfile = f.read()
    return HTMLResponse(content=myfile)


@app.get("/download")
def download(request: Request):
    return templates.TemplateResponse("download.html", {"request": request, "_files": os.listdir("./UploadedFiles")})

@app.get("/file_download/{filename}")
def download(request: Request, filename: str):
    print(filename)
    return FileResponse(f"./UploadedFiles/{filename}")



@app.get("/share")
def share(request: Request):
    filePath = "./templates/share.html"
    with open(filePath) as f:
        myfile = f.read()
    return HTMLResponse(content=myfile)

@app.post("/share")
def share(request: Request, myfile: UploadFile):
    with open("./UploadedFiles/"+myfile.filename, 'wb') as f:
        shutil.copyfileobj(myfile.file, f)
        
    filePath = "./templates/home.html"
    with open(filePath) as f:
        myfile = f.read()
    return HTMLResponse(content=myfile)


