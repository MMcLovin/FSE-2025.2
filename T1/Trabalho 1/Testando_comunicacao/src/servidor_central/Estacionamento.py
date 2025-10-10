from typing import Dict
from src.comum.models.Andar import Andar
import asyncio

class Estacionamento:
    def __init__(self):
        """
        isso aqui é um prototipo
        self.vagas: Dict = {
            "0": { 
                "PNE": 0,
                "Idoso": 1,
                "Comum": 0,
            },
            "1": { 
                "PNE": 1,
                "Idoso": 0,
                "Comum": 0,
            },
        } """

        self.terreo = Andar(pne=1,idoso=2,comum=1)
        self.primeiro_andar = Andar(pne=2,idoso=4,comum=2)
        self.segundo_andar = Andar(pne=2,idoso=4,comum=3)
        self.geral = Andar(
            pne = self.terreo.vagas_pne_total + self.primeiro_andar.vagas_pne_total + self.segundo_andar.vagas_pne_total,
            idoso = self.terreo.vagas_idoso_total + self.primeiro_andar.vagas_idoso_total + self.segundo_andar.vagas_idoso_total,
            comum = self.terreo.vagas_comum_total + self.primeiro_andar.vagas_comum_total + self.segundo_andar.vagas_comum_total
        )

    async def atualizar_vagas(self, andar:int, vagas: dict):
        try:
            # talvez a gnt tenha q usar lock para impedir que uma leitura seja realizada enquanto a gnt t� atualizando
            # como atualizar o geral? fazer uma thread para ficar somando os outros andares?
            if andar == 0:
                await self.terreo.atualizar_vagas(vagas)
            elif andar == 1:
                await self.primeiro_andar.atualizar_vagas(vagas)
            elif andar == 2:
                await self.segundo_andar.atualizar_vagas(vagas)
            elif andar == 3:
                await self.geral.atualizar_vagas(vagas)
            else:
                raise Exception(f"Erro no atualizar_vagas: Andar invalido")
        except Exception as e:
            print(f"Erro no atualizar_vagas: {e}")

    async def print_vagas(self, andar:int):
        try:
            if andar == 0:
                print(f"Vagas ocupadas\nPNE: {self.terreo.vagas_pne_ocupadas}, Idoso: {self.terreo.vagas_idoso_ocupadas}, Comum: {self.terreo.vagas_comum_ocupadas}")
                print(f"Vagas totais\nPNE: {self.terreo.vagas_pne_total}, Idoso: {self.terreo.vagas_idoso_total}, Comum: {self.terreo.vagas_comum_total}")
            elif andar == 1:
                print(f"Vagas ocupadas\nPNE: {self.primeiro_andar.vagas_pne_ocupadas}, Idoso: {self.primeiro_andar.vagas_idoso_ocupadas}, Comum: {self.primeiro_andar.vagas_comum_ocupadas}")
                print(f"Vagas totais\nPNE: {self.primeiro_andar.vagas_pne_total}, Idoso: {self.primeiro_andar.vagas_idoso_total}, Comum: {self.primeiro_andar.vagas_comum_total}")
            elif andar == 2:
                print(f"Vagas ocupadas\nPNE: {self.segundo_andar.vagas_pne_ocupadas}, Idoso: {self.segundo_andar.vagas_idoso_ocupadas}, Comum: {self.segundo_andar.vagas_comum_ocupadas}")
                print(f"Vagas totais\nPNE: {self.segundo_andar.vagas_pne_total}, Idoso: {self.segundo_andar.vagas_idoso_total}, Comum: {self.segundo_andar.vagas_comum_total}")
            elif andar == 3:
                #print(f"PNE: {self.geral.vagas_pne}, Idoso: {self.geral.vagas_idoso}, Comum: {self.geral.vagas_comum}")
                pass
            else:
                raise Exception("Erro no print_vagas: Andar invalido")
        except Exception as e:
            print(f"Erro no print_vagas: {e}")