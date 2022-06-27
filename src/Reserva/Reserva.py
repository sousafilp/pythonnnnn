from src.Operacao.Operacao import Operacao


class Reserva(Operacao):
    def __init__(self, cpf: str, codigo: int, prioridade: int):
        super().__init__(cpf, codigo)
        self._prioridade = prioridade
        
    def set_prioridade(self, prioridade: int):
        self._prioridade = prioridade

    def get_prioridade(self):
        return self._prioridade
