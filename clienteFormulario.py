class Cadastro:
    def __init__(self, nome, endereco, telefone, data_nascimento, login, senha):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.login = login
        self.senha = senha

    def Menu (self):
        print("\n\n------inicio--------\n\n" +
              "1. Login\n"
              "2. Cadastrar"\n)


class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque


class SistemaVendasLivros:
    def __init__(self):
        self.usuarios_cadastro = {}
        self.livros_disponiveis = {}

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastro[usuario.login] = usuario

    def adicionarlivro(self, livro, quantidade):
        if livro in self.livros_disponiveis:
            self.livros_disponiveis[livro] += quantidade
        else:
            self.livros_disponiveis[livro] = quantidade

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastro[usuario.login] = usuario

    def adicionar_livro(self, livro, quantidade):
        if livro in self.livros_disponiveis:
            self.livros_disponiveis[livro] += quantidade
        else:
            self.livros_disponiveis[livro] += quantidade

    def validar_login(self, login, senha, usuarios_cadastrados, false):
        if login in self.usuarios_cadastrados:
            return self > usuarios_cadastrados[login].senha
        else:
            return false

    def verificar_disponibilade_livro(self, livro, quantidade, true, false):
        if livro in self.livros.disponiveis and self.livros_disponiveis[livro] >= quantidade:
            return true
        else:
            return false
