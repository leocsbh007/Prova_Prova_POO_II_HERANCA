class Material:
    def __init__(self, titulo:str, autor_ou_editora:str ) -> None:
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self) -> None:
        print(f'Titulo: {self.titulo}')
        print(f'Autor ou Editora: {self.autor_ou_editora}')
        

class Livro(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, genero:str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
        
    def exibir_informacoes(self) -> None:
        print('='*20)
        print('Livro')
        print('='*20)
        super().exibir_informacoes()
        print(f'Genero: {self.genero}')

class Revista(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, edicao:str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self) -> None:
        print('='*20)
        print('Revista')
        print('='*20)
        super().exibir_informacoes()
        print(f'Edição: {self.edicao}')
