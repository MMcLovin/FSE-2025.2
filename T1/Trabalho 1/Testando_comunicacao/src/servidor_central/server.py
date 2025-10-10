import asyncio
import uvicorn
from fastapi import FastAPI
from typing import List, Dict
from contextlib import asynccontextmanager
from src.servidor_central.Estacionamento import Estacionamento
import pydantic
import httpx

async def retornar_vagas():
    await asyncio.sleep(3)
    endpoint = f"http://127.0.0.1:8081/placar/atualizar"
    while True:
        try:
            print(f"-"*30+"")
            print(f"Retornando vagas para o terreo...")
            var = vars(estacionamento)["vagas"]
            print(var)
            payload = var
            response = httpx.post(url=endpoint, json=payload)
        except Exception as e:
            print(f"Erro ao retornar vagas pro terreo: {e}")
        finally:
            print(f"-"*30+"\n")
            await asyncio.sleep(1)

@asynccontextmanager
async def main(app: FastAPI):
    global estacionamento
    try:
        estacionamento = Estacionamento()
        print("\nIniciando servidor central...")
        print(f"Estacionamento inicial:\n{vars(estacionamento)}\n")
        print("Criando tasks...")
        #task_retornar_vagas = asyncio.create_task(retornar_vagas())

        yield

        #task_retornar_vagas.cancel()

    except Exception as e:
        print(f"erro: {e}")

app = FastAPI(
    lifespan=main
)

@app.post("/andares/{andarId}/vagas")
async def atualizar_vagas(andarId: int, vagas: Dict):
    
    await estacionamento.atualizar_vagas(andarId, vagas)
    print(f"*"*30+"")
    print(f"Atualizando andar {andarId}:")
    await estacionamento.print_vagas(andarId)
    print(f"*"*30+"")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)