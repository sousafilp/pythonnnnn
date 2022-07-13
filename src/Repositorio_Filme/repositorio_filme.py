from src.Filme.Filme import Filme


class RepositorioFilme:

    def __init__(self):
        self._filmes = []

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_codigo()) is None:
            self._filmes.append(filme)
        else:
            print("Filme ja existente")

    def buscar(self, codigo: int):
        for filme in self._filmes:
            if codigo == filme.get_codigo():
                return filme
            else:
                return None

    def atualizar(self, filme: Filme):
        filme = self.buscar(filme.get_codigo())
        if filme is not None:
            filme.set_preco_locacao(filme.get_preco_locacao())
            filme.set_numero_copias(filme.get_numero_copias())
        else:
            print('Erro, nao foi possivel encontrar o filme!!!')

    def deletar(self, codigo: int):
        encontrou = False
        for filme in self._filmes:
            if filme.get_codigo() == codigo:
                self._filmes.pop(self._filmes.index(filme))
                print(f'Filme {filme.get_titulo()} removido com suceesso :D')
                encontrou = True
        if not encontrou:
            print('Filme nao encontrado!!!')

    def listar(self):
        for filme in self._filmes:
            print(f'{filme.get_titulo()}')
