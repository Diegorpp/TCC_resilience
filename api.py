from fastapi import FastAPI, status
from datetime import datetime
from backend.model import Test_data
now = datetime.now()

app = FastAPI()

def funcao_pesada():
    pass


# healthz nome padrão para verificar o status da aplicação.
@app.get("/healthz", status_code=status.HTTP_200_OK)
def healthz():
    current_time = datetime.now()
    duration = current_time - now

    # if duration.seconds > 10:
    return {"message": f"{duration.seconds}"}
    # return {f"message": "System is no ready yet."}

@app.post("/processa_algo", status_code=status.HTTP_200_OK)
def processa_algo(data: Test_data):
    current_time = datetime.now()
    # duration = current_time - now
    # if duration.seconds > 10:

    return {"message": f"{data}"}


