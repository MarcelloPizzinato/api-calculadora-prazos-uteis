from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

from app import prazo_service
app = FastAPI(
    title="Calculadora de Prazos Úteis",
    description="API que calcula vencimento de prazos."
)

class SlaRequest(BaseModel):
    data_entrada: date
    prazo_dias: int

@app.get("/")
def pagina_inicial():

    return {
        "mensagem": "Bem-vindo à Calculadora de Prazos Úteis!",
        "dica": "Acesse http://127.0.0.1:8000/docs para testar a API."
    }

@app.post("/calcular-vencimento")
def calcular_vencimento(request: SlaRequest):

    data_final = prazo_service.calcular_data_vencimento(
        request.data_entrada,
        request.prazo_dias
    )

    return {
        "data_entrada": request.data_entrada,
        "prazo_dias": request.prazo_dias,
        "data_vencimento": data_final
    }