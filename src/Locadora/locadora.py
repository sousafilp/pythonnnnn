from src.Cliente.cliente import Cliente
from src.Filme.Filme import Filme
from src.Repositorio_Cliente.repositorio_cliente import RepositorioCliente
from src.Repositorio_Filme.repositorio_filme import RepositorioFilme
from src.Repositorio_Operacao.repositorio_operacao import RepositorioOperacao
from src.Reserva.Reserva import Reserva


class Locadora:

    def __init__(self, clientes: RepositorioCliente, filmes: RepositorioFilme, operacoes: RepositorioOperacao):
        self._clientes = clientes
        self._filmes = filmes
        self._operacoes = operacoes

    def cadastrarCliente(self, cliente: Cliente):
        self._clientes.cadastrar(cliente)

    def buscarCliente(self, cpf: str):
        return self._clientes.buscar(cpf)

    def atualizarCadastroCliente(self, cliente: Cliente):
        self._clientes.atualizar(cliente)

    def removerCliente(self, cpf: str):
        if self._operacoes.numero_locacoes_ativas(cpf) == 0:
            self._clientes.deletar(cpf)

    def cadastrar_filme(self, filme: Filme):
        self._filmes.cadastrar(filme)

    def buscar_filme(self, codigo: int):
        return self._filmes.buscar(codigo)

    def atualizar_cadastro_filme(self, filme: Filme):
        self._filmes.atualizar(filme)

    def removerFilme(self, codigo: int):
        if self._operacoes.numero_locacoes_ativas(codigo) == 0:
            self._filmes.deletar(codigo)

    def reservar_filme(self, cpf: str, codigo: int):
        op = Reserva(cpf, codigo)
        if self.buscarCliente(cpf) is not None:
            if self.buscar_filme(codigo) is not None:
                self._operacoes.cadastrar(op)


    def finalizar_reserva_filme(self, cpf: str, codigo: int):
        pass

    def locar_filme(self, cpf: str, codigo: int):
        pass

    def devolver_filme(self, cpf: str, codigo: int):
        cliente = self.buscarCliente(cpf)
        filme = self.buscar_filme(codigo)
        locacao = self._operacoes.buscar_locacoes(cpf)
        if cliente is not None and filme is not None and locacao is not None:
            self._operacoes.deletar_reservas(cpf, codigo)

    def imprimir_historico_locacoes(self, cpf: str):
        if self.buscarCliente(cpf) is not None:
            print(self._operacoes.listar_locacoes(cpf))

    def imprimir_filmes_mais_locados(self, top: int):
        pass