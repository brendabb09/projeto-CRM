import mysql.connector# Importa a função mysql.connector para conectar ao banco de dados MySQL

class Usuario:
    def __init__(self, nome, telefone,email,senha):#inicializa os atributos da classe
        self.nome = nome # o atributo nome da instancia atribui o valor do parametro nome
        self.telefone = telefone
        self.email =  email
        self.senha = senha
class Cliente:
    def __init__(self, nome, telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
class SistemaDeCRM:
    def __init__(self):#inicializando
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="crm_db"
        )
        self.cursor = self.conexao.cursor()#executa o comando sql no banco de dados conectado

    def adicionar_usuario(self):
        nome = input("Digite o nome do usuário: ")#solicita o nome do usuario 
        telefone = input("Digite o telefone do usuário: ")
        email = input('digite o email do usuario :')
        senha = input('digite a senha do usuario :')
        usuario = Usuario(nome, telefone,email,senha)#cria uma estancia da classe usuario
        sql = "INSERT INTO usuario (nome, telefone,email, senha) VALUES (%s, %s, %s, %s )"
        valores = (usuario.nome, usuario.telefone ,usuario.email,usuario.senha)#atribuir os espaços vazio
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Usuário adicionado com sucesso.')

    def adicionar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input('digite o email do cliente: ')
        cliente = Cliente(nome, telefone,email)
        sql = "INSERT INTO cliente (nome, telefone, email) VALUES (%s, %s ,%s)"
        valores = (cliente.nome, cliente.telefone, cliente.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Cliente adicionado com sucesso.')

    def listar_usuarios(self):
        self.cursor.execute("SELECT nome, telefone,email, senha FROM usuario")
        usuarios = self.cursor.fetchall()#recupera os registro 
        for usuario in usuarios:# para cada usuario em usuario imprimir o resultado da f string abaixo
            print(f"Nome: {usuario[0]}, Telefone: {usuario[1]}, email:{usuario[2]},senha:{usuario[3]}")

    def listar_clientes(self):
        self.cursor.execute("SELECT nome, telefone,email FROM cliente")
        clientes = self.cursor.fetchall()#recuperar os registro 
        for cliente in clientes:## para cada cliente em cliente imprimir o resultado da f string abaixo
            print(f"Nome: {cliente[0]}, Telefone: {cliente[1]} email{cliente[2]}")

    def fechar_conexao(self):#fecha
        self.cursor.close()
        self.conexao.close()

    def menu(self):#define o metodo menu 
        while True:# enquanto for verdadeiro o loop vai rodar 
            print("Menu:")
            print("1. Adicionar usuário")
            print("2. Adicionar cliente")
            print("3. Listar usuários")
            print("4. Listar clientes")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.adicionar_usuario()
            elif escolha == '2':
                self.adicionar_cliente()
            elif escolha == '3':
                self.listar_usuarios()
            elif escolha == '4':
                self.listar_clientes()
            elif escolha == '5':
                self.fechar_conexao()
                print("Conexão fechada. Saindo...")
                break# finaliza o loop
            else:# se opcao for falsa ele mostra na tela 
                print("Opção inválida. Tente novamente.")

# Instancia o sistema de CRM e exibe o menu
sistema = SistemaDeCRM()#cria uma intancia da classe sistemadecrm
sistema.menu()# Chama o método menu para exibir o menu e permitir a interação do usuário.
