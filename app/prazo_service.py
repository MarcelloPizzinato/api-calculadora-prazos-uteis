import requests
from datetime import date, timedelta
from fastapi import FastAPI, HTTPException

#Função para puxar os feriados da API Brasil

def get_feriados_nacionais(ano: int) -> list[date]:
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar feriados do ano {ano} na BrasilAPI")

    feriados_json = response.json()
    datas_feriados = [date.fromisoformat(f['date']) for f in feriados_json]

    return datas_feriados

def calcular_data_vencimento(data_entrada: date, prazo_dias: int) -> date:
    
    data_atual = data_entrada
    dias_restantes = prazo_dias
    
    feriados = get_feriados_nacionais(data_atual.year)
    
    while dias_restantes > 0:
        data_atual += timedelta(days=1)
        
        if data_atual.year != (data_atual - timedelta(days=1)).year:
            feriados.extend(get_feriados_nacionais(data_atual.year))
            
        if data_atual.weekday() >= 5:
                continue
                
        if data_atual in feriados:
                continue
                
        dias_restantes -= 1
            
    return data_atual