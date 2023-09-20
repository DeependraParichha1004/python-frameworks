import json
from class_feat import Item
from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get('/process')
def calculate(item:Item):
    x = item.a  # Use item.a instead of item[a]
    y = item.b  # Use item.b instead of item[b]
    return {'ans': x + y}

if __name__ == "__main__":
    a = 2
    b = 3
    json_data = json.dumps({'a': 3, 'b': 5})
    response = requests.get('http://127.0.0.1:8000/process', json=json_data)
    print(response.json())  # Print the response from the POST request
    uvicorn.run(app, host="127.0.0.1", port=8000)