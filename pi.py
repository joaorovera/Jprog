import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'joao2908',
    database = 'projetointegrador'
)

senha = 'Joao2908'
class Cliente():

    def cadastrar_cliente(nome, idade, cpf, email):
        cursor = conexao.cursor()
        sql = f"INSERT INTO cliente (nome, idade, cpf, email) VALUES ('{nome}', {idade}, '{cpf}', '{email}')"
        cursor.execute(sql)
        conexao.commit()
        print("Cliente cadastrado com sucesso!")

    def calcular_frete(distancia):
        if distancia <= 500:
            frete = 0
            print(f'A venda não irá ter uma taxa de frete.')
        elif distancia > 500 and distancia <= 2500:
            frete = 20
            print(f'A taxa do frete será {frete} reais.')
        else:
            frete = 40
            print(f'A taxa do frete será {frete} reais.')
       
    def atualizar_cliente(nome, idade, cpf, email, idcliente):
        cursor = conexao.cursor()
        sql = f"UPDATE cliente SET nome = '{nome}', idade = {idade},  cpf = '{cpf}', email = '{email}' WHERE idcliente = {idcliente}"
        cursor.execute(sql)
        conexao.commit()
        print("Cliente atualizado com sucesso!")

class Eletro():
    def __init__(self, nome, uso, garantia, valor, quantidade) -> None:
        self.nome = nome
        self.uso = uso
        self.garantia = garantia
        self.valor = valor
        self.quantidade = quantidade

    def cadastrar_produto(nome, uso, garantia, valor, quantidade):
        cursor = conexao.cursor()
        sql = f"INSERT INTO eletros (nome, uso, garantia, valor, quantidade) VALUES ('{nome}', {uso}, {garantia}, {valor}, {quantidade})"
        cursor.execute(sql)
        conexao.commit()
        print("Produto cadastrado com sucesso!")
   
    def atualizar_produto(nome,uso,garantia,valor,quantidade, ideletro):
        cursor = conexao.cursor()
        sql = f"UPDATE eletros SET nome = '{nome}', uso = {uso},  garantia = {garantia}, valor = {valor}, quantidade = {quantidade} WHERE ideletro = {ideletro}"
        cursor.execute(sql)
        conexao.commit()
        print("Produto atualizado com sucesso!")

    def mostrarProduto(produto):
        cursor=conexao.cursor()
        cursor.execute(f"Select ideletro FROM eletros where nome = '{produto}'")
        produtos = cursor.fetchone()
        for i in produtos:
            ideletro = i
        cursor.execute(f"Select valor FROM eletros where nome = '{produto}'")
        produtox = cursor.fetchone()
        for i in produtox:
            valor = i
        return (ideletro,valor)
   
    def mostrarCliente(nome1):
        cursor=conexao.cursor()
        cursor.execute(f"Select idcliente FROM cliente where nome = '{nome1}'")
        nomes = cursor.fetchone()
        try:
            for i in nomes:
                idcliente = i
            return idcliente
        except:
            print('O cliente não possui cadastro, ou foi digitado de maneira errada')

    def mostrar_produtos(produto):
        cursor=conexao.cursor()
        cursor.execute(f"Select valor, quantidade FROM eletros where nome = '{produto}'")
        produtos = cursor.fetchall()
        for i in produtos:
            print(i)

    def buscar_produto(nome):
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome, garantia, valor, quantidade FROM eletros where nome = '{nome}'")
        produto = cursor.fetchone()
        for i in produto:
            print(i)

    def parcelar(produto):
        cursor=conexao.cursor()
        cursor.execute(f"Select valor FROM eletros where nome = '{produto}'")
        parcelamento = cursor.fetchone()
        for i in parcelamento:
            if i <= 300:
                print("O valor infelizmente não pode ser parcelado.")
            elif i >300 and i <= 500:
                parcelas = i/5
                print(f"O parcelamento disponibilizado é 5 parcelas de {parcelas}")
            elif i >500 and i <= 800:
                parcelas = i/8
                print(f"O parcelamento disponibilizado é 8 parcelas de {parcelas}")
            else:
                parcelas = i/12
                print(f"O parcelamento disponibilizado é 12 parcelas de {parcelas}")

    def confirmar_venda(produto):
        cursor = conexao.cursor()
        cursor.execute(f"Select quantidade FROM eletros where nome = '{produto}'")
        quant = cursor.fetchone()
        for i in quant:
            sql = f"UPDATE eletros SET quantidade = {i - 1} WHERE nome = '{produto}'"
            cursor.execute(sql)
        conexao.commit()

    def cadastrar_venda(ideletro, idcliente, valor, data):
        cursor = conexao.cursor()
        sql = f"INSERT INTO vendas (ideletro, idcliente, valor, data) VALUES ({ideletro}, {idcliente}, {valor}, '{data}')"
        cursor.execute(sql)
        conexao.commit()
        print("Venda cadastrado com sucesso!")

    def mostrar_estoque():
        cursor = conexao.cursor()
        cursor.execute(f"Select nome, quantidade FROM eletros")
        estoque = cursor.fetchall()
        for i in estoque:
            print(i)



def menu():
    while True:
        tentativa = input('Por gentileza, digite a senha: ')
        if tentativa != senha:
            print('senha incorreta, tente novamente')
        else:
            break
   
    while True:
        print("\n\n----------------------\n--- Menu Principal ---\n----------------------\n")
        print("1. Cadastrar produto")
        print("2. Atualizar produto")
        print("3. mostrar estoque")
        print('4. Realizar uma venda')
        print("5. Buscar produto")
        print("6. Cadastrar cliente")
        print("7. Atualizar cliente")
        print("0. Encerrar programa")
        opcao = input("\nDigite a opção desejada: ")
       
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            uso = input("Quanto tempo de uso: ")
            garantia = input("Quantos anos de garantia terá: ")
            valor= input("Valor referente ao produto: ")
            quantidade= input("Quantos produtos em estoque: ")
            Eletro.cadastrar_produto(nome,uso,garantia,valor,quantidade)
        elif opcao == "2":
            nome = input("Digite o nome do produto: ")
            uso = input("Quanto tempo de uso: ")
            garantia = input("Quantos anos de garantia terá: ")
            valor= input("Valor referente ao produto: ")
            quantidade= input("Quantos produtos em estoque: ")
            ideletro = int(input("Digite o ID do produto a ser atualizado: "))
            Eletro.atualizar_produto(nome,uso,garantia,valor,quantidade,ideletro)
        elif opcao == "3":
            Eletro.mostrar_estoque()
        elif opcao == "4":
            cadastro = input("O cliente já possui cadastro? ").lower()
            if cadastro=="nao" or cadastro=="n" or cadastro=="não":
                nome = input("Digite o nome do cliente: ")
                idade = input("Quanto anos de idade: ")
                cpf = input("Digite o cpf do cliente: ")
                email= input("Digite o email do cliente: ")
                Cliente.cadastrar_cliente(nome,idade,cpf,email)
            data = datetime.datetime.today()
            nome1 = input("qual o nome do cliente realizando a compra: ")
            while True:
                try:
                    distancia = int(input("Qual a distancia da casa do cliente em metros: "))
                    Cliente.calcular_frete(distancia)
                    break
                except:
                    print("Apenas numeros, por favor.")
            produto = input("Qual produto o cliente deseja ver: ")
            try:
                Eletro.mostrar_produtos(produto)
                Eletro.parcelar(produto)
            except:
                print("O produto desejado não existe em estoque!")
                continue
            resposta = input('o cliente comprou? ').lower()
            if resposta == "sim" or resposta == "s" or resposta == "si":
                try:
                    Eletro.cadastrar_venda(Eletro.mostrarProduto(produto)[0],Eletro.mostrarCliente(nome1),Eletro.mostrarProduto(produto)[1],data)
                except:
                    continue
                Eletro.confirmar_venda(produto)
            else:
                print("É uma pena mesmo, boa sorte na próxima venda!")
        elif opcao == "5":
            nome = input("Qual produto você deseja Buscar: ")
            try:
                Eletro.buscar_produto(nome)
            except:
                print("----------------------\nNão existe o produto desejado em estoque!")
        elif opcao == "6":
            nome = input("Digite o nome do cliente: ")
            idade = input("Quanto anos de idade: ")
            cpf = input("Digite o cpf do cliente: ")
            email= input("Digite o email do cliente: ")
            Cliente.cadastrar_cliente(nome,idade,cpf,email)
        elif opcao == "7":
            idcliente = input("Qual o id a ser atualizado: ")
            nome = input("Digite o nome do cliente: ")
            idade = input("Quanto anos de idade: ")
            cpf = input("Digite o cpf do cliente: ")
            email= input("Digite o email do cliente: ")
            Cliente.atualizar_cliente(nome, idade, cpf, email, idcliente)
        elif opcao == "0":
            print("estamos encerrando o programa")
            break
        else:
            print("Opção inválida!")

menu()

conexao.close()
