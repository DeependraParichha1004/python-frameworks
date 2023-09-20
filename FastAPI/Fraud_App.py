import uvicorn
from fastapi import FastAPI
import pickle
from class_feat import Fraud
app=FastAPI()
out=open('xgboost_fraud.pkl','rb')
classifier=pickle.load(out)

@app.get('/')
def home():
    return {'Message':"Welcome to the xgboost fraud app"}

@app.post('/predict')
def fraud_prediction(data:Fraud):
    data=data.dict()
    var1=data['step']
    var2=data['type']
    var3=data['amount']
    var4=data['oldbalanceOrg']
    var5=data['newbalanceOrig']
    var6=data['oldbalanceDest']
    var7=data['newbalanceDest']

    y_pred=classifier.predict([[var1,var2,var3,var4,var5,var6,var7]])
    y_pred=y_pred[0]

    if(y_pred):
        return {'result':"yes, it is fraud"}
    else:
        return {'result': "No, it is not fraud"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)