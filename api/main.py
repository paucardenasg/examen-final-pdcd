import uvicorn
import pickle
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel


API_KEY = "pau_saca_10"
API_KEY_NAME = "code"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

app = FastAPI(title="Funding challenge!",
              description="Esta API permite saber si a un proyecto se le otorgarán fondos o no."
                          "Para ello, se recibirá como input la descripción del proyecto y se regresará"
                          "un 1 en caso de que sí se otorguen los fondos y un 0 en caso contrario.",
              version="0.0.1")


def get_api_key(api_key_query: str = Security(api_key_query)):
    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Acceso denegado, favor de ingresar la contraseña."
        )


class Project(BaseModel):
    Description: str


@app.on_event("startup")
def load_model():
    global model
    with open("./model/model_desc.pickle", "rb") as openfile:
        model = pickle.load(openfile)
    global vectorizer
    with open("./model/vectorizer.pickle", "rb") as openfile:
        vectorizer = pickle.load(openfile)
    global tf_idf
    with open("./model/tf_idf.pickle", "rb") as openfile:
        tf_idf = pickle.load(openfile)


@app.get("/api/v1/classify")
async def classify_project(inputs: Project, api_key: APIKey = Depends(get_api_key)):
    finals = str(inputs.Description)
    finals = [finals]
    # Crear bag of words
    pred_bow = vectorizer.transform(finals).toarray()
    # Crear tf_idf
    pred_tf_idf = tf_idf.fit_transform(pred_bow).toarray()
    pred_tf_idf = list(pred_tf_idf[0])
    pred = model.predict([pred_tf_idf])
    dict_pred = {0: 'Not founded',
                 1: 'Founded'}
    return {"Prediction": dict_pred.get(pred[0])}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
