import textwrap

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def criar_conta(self, tipo_conta, saldo_inicial=0):
        conta = Conta(tipo_conta, saldo_inicial)
        self.contas.append(conta)
        return conta

    def listar_contas(self):
        return self.contas

class Conta:
    num_conta = 1

    def __init__(self, tipo_conta, saldo_inicial):
        self.numero = Conta.num_conta
        self.tipo_conta = tipo_conta
        self.saldo = saldo_inicial
        Conta.num_conta += 1

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        return f"Conta {self.numero} - Saldo: R${self.saldo:.2f}"

# Função para buscar usuário por CPF
def buscar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

usuarios = []

def criar_novo_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    usuario = Usuario(nome, cpf)
    usuarios.append(usuario)
    print("Novo usuário cadastrado com sucesso!")

def menu():
    while True:
        print("\n==== Menu ====")
        print("1. Criar novo usuário")
        print("2. Acessar conta do usuário")
        print("3. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            criar_novo_usuario()
        elif opcao == '2':
            cpf = input("Digite o CPF do usuário: ")
            usuario = buscar_usuario(usuarios, cpf)
            if usuario:
                conta = None
                while True:
                    print("\n==== Conta do Usuário ====")
                    print("1. Criar nova conta")
                    print("2. Listar contas")
                    print("3. Fazer depósito")
                    print("4. Fazer saque")
                    print("5. Ver extrato")
                    print("6. Voltar")

                    opcao_conta = input("Digite a opção desejada: ")

                    if opcao_conta == '1':
                        tipo_conta = input("Digite o tipo da conta: ")
                        saldo = float(input("Digite o saldo inicial: "))
                        conta = usuario.criar_conta(tipo_conta, saldo)
                        print(f"Nova conta criada: Conta {conta.numero}")
                    elif opcao_conta == '2':
                        contas = usuario.listar_contas()
                        if contas:
                            print("Contas do usuário:")
                            for conta in contas:
                                print(conta.numero, conta.tipo_conta)
                        else:
                            print("O usuário não possui nenhuma conta.")
                    elif opcao_conta == '3':
                        valor = float(input("Digite o valor para depósito: "))
                        conta.depositar(valor)
                        print("Depósito realizado com sucesso.")
                    elif opcao_conta == '4':
                        valor = float(input("Digite o valor para saque: "))
                        conta.sacar(valor)
                    elif opcao_conta == '5':
                        print(conta.extrato())
                    elif opcao_conta == '6':
                        break
                    else:
                        print("Opção inválida. Por favor, tente novamente.")
            else:
                print("Usuário não encontrado. Por favor, cadastre um novo usuário.")
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu()