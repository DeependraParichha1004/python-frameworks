import pydantic
from pydantic import BaseModel

class Fraud(BaseModel):
    step:int
    type:int
    amount:float
    oldbalanceOrg:float
    newbalanceOrig:float
    oldbalanceDest:float
    newbalanceDest:float

class Item(BaseModel):
    a: int
    b: int