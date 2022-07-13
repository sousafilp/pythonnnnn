from src.Locacao.Locacao import Locacao
from src.Operacao.Operacao import Operacao
from src.Reserva.Reserva import Reserva


class RepositorioOperacao:

    def __init__(self):
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):
        if operacao not in self.operacoes:
            self.operacoes.append(operacao)
            operacao.set_ativo(True)
        else:
            print('Operacao ja cadastrada!!')

    def buscar_reservas(self, cpf: str):
        reserva = []
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.is_ativo() is True and isinstance(operacao, Reserva):
                reserva.append(operacao)
        return reserva

    def buscar_locacoes(self, cpf: str):
        locacao = []
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.is_ativo() is True and isinstance(operacao, Locacao):
                locacao.append(operacao)
        return locacao

    def deletar_reservas(self, cpf: str, codigo: int):
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.get_codigo() == codigo and operacao.is_ativo() is True and isinstance(
                    operacao, Reserva):
                operacao.set_ativo(False)

    def deletar_locacao(self, cpf: str, codigo: int):
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.get_codigo() == codigo and operacao.is_ativo() is True and isinstance(
                    operacao, Locacao):
                operacao.set_ativo(False)

    def listar_locacoes(self, cpf: str):
        locacoes = []
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and isinstance(operacao, Locacao):
                locacoes.append(operacao)
        return locacoes

    def numero_locacoes(self, cpf: str):
        num = self.listar_locacoes(cpf)
        return len(num)

    def numero_locacoes(self, codigo: int):
        locacoes = []
        for operacao in self.operacoes:
            if operacao.get_codigo() == codigo and isinstance(operacao, Locacao):
                locacoes.append(operacao)
        return len(locacoes)

    def numero_locacoes_ativas(self, cpf: str):
        locacoes = []
        for operacao in self.operacoes:
            if operacao.get_cpf() == cpf and operacao.is_ctivo() is True and isinstance(operacao, Locacao):
                locacoes.append(operacao)
        return len(locacoes)

    def numero_locacoes_ativas(self, codigo: int):
        locacoes = []
        for operacao in self.operacoes:
            if operacao.get_codigo() == codigo and operacao.is_ativo() is True and isinstance(operacao, Locacao):
                locacoes.append(operacao)
        return len(locacoes)

    def numero_reservas(self, codigo: int):
        reservas = []
        for operacao in self.operacoes:
            if operacao.get_codigo() == codigo and operacao.is_ativo() is True and isinstance(operacao, Reserva):
                reservas.append(operacao)
        return len(reservas)
