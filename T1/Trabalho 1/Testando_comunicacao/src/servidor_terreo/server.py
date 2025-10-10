import asyncio
import uvicorn
from fastapi import FastAPI
from typing import List, Dict
from contextlib import asynccontextmanager
import httpx

# o que eu quero fazer?
# [x] iniciar os servidor central
# [x] iniciar o servidor terreo
# [x] criar a classe estacionamento
    # [x] criar a classe andar
    # [] testar o envia com a classe andar só com o terreo incialmente
    # [] agora que eu criei a classe estacionamento, eu posso (por enquanto) manter o send_vagas como está e alterar somente o envio do servidor central para o servidor terreo
# [x] criar uma task que envia um dado fixo para o servidor central
# [x] criar o endpoint no servidor central
# [x] criar a task que fica publicando o estado atual do estacionamento para o servidor terreo
# [x] criar o endpoint no servidor terreo para receber a atualizacao de todas as vagas
    # [x] tô resolvendo qual tipo de dado vem na req

async def send_vagas_terreo():
    # VEI, ISSO AQUI ME FUDEU MUITO, IA NENHUMA CONSEGUIA ME AJUDAR. Quando a gnt inicia o servidor FastAPI, se a task começar a rodar imediatamente, ele meio que rouba a execução e isso gera muitos problemas, pois não dava mais pra matar a task com ctrl+z (no linux ainda funcionava) ou ctrl+c, ai qunado ia iniciar o server novamente dava erro pq ele não havia sido fechado corretamente e continuava usando a porta, dai tinha q matar o processo a blá blá blá
    await asyncio.sleep(2)
    andarId = 0
    endpoint = f"http://127.0.0.1:8080/andares/{andarId}/vagas"
    while True:
        try:
            # o payload tem que ter um "objeto" vaga
            payload = {
                "vagas":{
                    "PNE":0,
                    "Idoso":1,
                    "Comum":0,
                }
            }
            andarId = 0
            response = httpx.post(url=endpoint, json=payload, timeout=5)
            print(f"-"*30+"")
            print(f"enviando vagas do andar {andarId}")
            if response.status_code == 200:
                print("Sucesso na req")
            else:
                print(f"Falha na req: {response.status_code}")

        except Exception as e:
            print(f"Erro no send_vagas_terreo: {e}")
        finally:
            print(f"-"*30+"\n")
            await asyncio.sleep(1)

async def send_vagas_primeiro_andar():
    # VEI, ISSO AQUI ME FUDEU MUITO, IA NENHUMA CONSEGUIA ME AJUDAR. Quando a gnt inicia o servidor FastAPI, se a task começar a rodar imediatamente, ele meio que rouba a execução e isso gera muitos problemas, pois não dava mais pra matar a task com ctrl+z (no linux ainda funcionava) ou ctrl+c, ai qunado ia iniciar o server novamente dava erro pq ele não havia sido fechado corretamente e continuava usando a porta, dai tinha q matar o processo a blá blá blá
    await asyncio.sleep(2)
    andarId = 1
    endpoint = f"http://127.0.0.1:8080/andares/{andarId}/vagas"
    while True:
        try:
            # o payload tem que ter um "objeto" vaga
            payload = {
                "vagas":{
                    "PNE":1,
                    "Idoso":2,
                    "Comum":1,
                }
            }
            andarId = 0
            response = httpx.post(url=endpoint, json=payload, timeout=5)
            print(f"-"*30+"")
            print(f"enviando vagas do andar {andarId}")
            if response.status_code == 200:
                print("Sucesso na req")
            else:
                print(f"Falha na req: {response.status_code}")

        except Exception as e:
            print(f"Erro no send_vagas_terreo: {e}")
        finally:
            print(f"-"*30+"\n")
            await asyncio.sleep(1)

@asynccontextmanager
async def main(app: FastAPI):
    print("INFO: Iniciando servidor terreo...")
    
    task_send_vagas_terreo=asyncio.create_task(send_vagas_terreo())
    task_send_vagas_primeiro_andar=asyncio.create_task(send_vagas_primeiro_andar())

    yield

    task_send_vagas_terreo.cancel()
    task_send_vagas_primeiro_andar.cancel()


app = FastAPI(
    lifespan=main
)

@app.post("/placar/atualizar")
async def atualizar_vagas(vagas_andares: dict):
    #print("chamar o metodo na modbus com .lock() para atualizar o placar")
    print(f"*"*30+"")
    print(f"vagas andar terreo: {vagas_andares["0"]}")
    print(f"vagas primeiro andar: {vagas_andares["0"]}")
    print(f"*"*30+"\n")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)