import asyncio

class Andar:
    def __init__(self, pne, idoso, comum):
        self.vagas_pne_total = pne
        self.vagas_idoso_total = idoso
        self.vagas_comum_total = comum
        
        self.vagas_pne_ocupadas = 0
        self.vagas_idoso_ocupadas = 0
        self.vagas_comum_ocupadas = 0

        self.vagas_pne_livres = self.vagas_pne_total
        self.vagas_idoso_livres = self.vagas_idoso_total
        self.vagas_comum_livres = self.vagas_comum_total
        
        self.vagas_totais = self.vagas_pne_total + self.vagas_idoso_total + self.vagas_comum_total
        self.vagas_ocupadas = 0
        self.vagas_livres = self.vagas_totais 

        self.lock = asyncio.Lock()

    async def atualizar_vagas(self, vagas:dict):
        try:
            async with self.lock:
                # logica pra atualizar as vagas, tenho que ver como o payload das vagas ta chegando pra poder atribuir eles aos meus atributos
                self.vagas_pne_ocupadas = vagas["PNE"]
                self.vagas_idoso_ocupadas = vagas["Idoso"]
                self.vagas_comum_ocupadas = vagas["Comum"]

                self.vagas_pne_livres = self.vagas_pne_total - self.vagas_pne_ocupadas
                self.vagas_idoso_livres = self.vagas_idoso_total - self.vagas_idoso_ocupadas
                self.vagas_comum_livres = self.vagas_comum_total - self.vagas_comum_ocupadas

                self.vagas_totais = self.vagas_pne_total + self.vagas_idoso_total + self.vagas_comum_total
                self.vagas_ocupadas = 0 # tenho q ver essa parte
                self.vagas_livres = self.vagas_totais - self.vagas_ocupadas
        except Exception as e:
            raise Exception(f"Erro no atualizar_vagas: {e}")
