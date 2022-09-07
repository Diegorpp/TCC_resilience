from fastapi import FastAPI, status
from datetime import datetime

now = datetime.now()

app = FastAPI()


# healthz nome padrão para verificar o status da aplicação.
@app.get("/healthz", status_code=status.HTTP_200_OK)
def healthz():
    current_time = datetime.now()
    duration = current_time - now

    if duration.seconds > 5:
        return {"message": f"{duration.seconds}"}
    return {f"message": "System is no ready yet."}

