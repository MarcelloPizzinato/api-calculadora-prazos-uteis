# Calculadora de Prazos Úteis (API)

Uma API desenvolvida em Python para calcular a data de vencimentoexata de ofícios e obrigações legais, adicionando dias úteis a uma data de entrada.
O sistema pula automaticamente os finais de semana e os feriados nacioanis, garantidndo precisão no cálculo de SLAs (Service Level Agreements).

## Tecnologias Utilizadas:

* **Python** (Linguagem principal)
* **FastAPI** (Framework para criação da API e documentação automática)
* **Uvicorn** (Servidor ASGI)
* **Requests** (Para consumo de API externa)
* **Integração:** [BrasilAPI](https://brasilapi.com.br/) (Para consulta dinâmica de feriados nacionais)

## Arquitetura do Projeto

O projeto foi construído seguindo boas práticas de separação de responsabilidades:
* `main.py`: Responsável por gerenciar rotas da API e a comunicação HTTP.
* `prazo_service.py`: Isola as regra de negócio, realizando o cálculo matemático de datas e o consumo da BrasilAPI.

## Como executar o projeto localmente

1. Clone este repositório no seu computador.
2. Instale as dependências necessárias executando o comando a seguir no terminal:
   `pip install fastapi uvicorn requests`
3. Inicie o servidor com o comando:
   `uvicorn app.main:app --reload`
4. Acesse a documentação interativa (Swagger) no seu navegador:
    `http://127.0.0.1:8000/docs`

## Como testar

Na tela do Swagger, envie um JSON com a data de entrada (formato YYYY-MM-DD) e o prazo em dias. Exemplo de requisição:

{
  "data_entrada": "2026-06-09",
  "prazo_dias": 10
}
