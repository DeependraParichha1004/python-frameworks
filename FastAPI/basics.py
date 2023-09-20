import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
app=FastAPI()
@app.get('/')
def home(name:str):
    return {'Message':f"hello, {name}"}

#query parameter
@app.get('/name-query-parameter')#http://127.0.0.1:8000?name=deependra
def _name(name:str):
    return {"name":name}

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
#     # run using uvicorn basics:app --reload in the terminal




