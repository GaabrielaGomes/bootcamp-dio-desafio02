# Objetivo Geral: separar as funções existentes de saque, depósito e extrato em funções. 
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária
# - criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)

# Função Saque deve receber os argumentos apenas por nome (keyword only). 
# Sugestão de argumentos: saldo, valor, extrato, limite, numero_saque, limite_saque. Sugestão de retorno: saldo e extrato

# Função de Depósito deve receber os argumentos apenas por posição (positional only). 
#Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

# Função extrato deve receber por posição e nome (positional only e keyword only). 
# Argumentos pocionais: saldo, argumentos nomeados: extrato

# nova função -> listar contas (opcional)

# Criar usuário (cliente): 
# O programa deve armazenar os usuários em uma lista, um usuário é composto por nome, data de nascimento, cpf e endereço. 
# O endereço é uma string com o formato: logradouro, nro, bairro, cidade/sigla estado. 
# Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# Criar conta corrente:
# O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. 
# O núemro da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". 
# O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

# Diga: para vincular um usuário a uma conta, filtre a lista de usuarios buscando o número 
# do CPF informado para cada usuário da lista

def menu():
    menu = int(input('''\n ======== Menu ========
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar Cliente
    [5] - Criar Conta Corrente
    [6] - Listar Contas
    [0] - Sair
Digite a operação desejada: '''))
    return menu

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
    else:
        print('\nNão é possível depositar valor negativo')
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    if numero_saque <= limite_saque:
        if saldo >= valor and valor <= limite:
            saldo -= valor
            numero_saque += 1
            extrato += f'Saque: R$ {valor:.2f}\n'
        else:
            print('\nValor de saque inválido. Verifique seu saldo ou limite máximo de R$500 por saque.')
    else:
        print('\nNúmero máximo de saques diários excedido.')

    return saldo, extrato

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência:{conta['agencia']}")
        print(f"Número da Conta:{conta['numero_conta']}")
        print(f"Titular:{conta['usuario']['nome']}")

def criar_usuario(usuarios):
    cpf = input("\nDigite o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return print("\nCPF já cadastrado, verifique e tente novamente")
           
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Logradouro, nº - Bairro - cidade/UF): ") 

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nCliente cadastrado com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nCliente não encontrado")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def extratos(saldo, /, *, extrato):
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("\nInforme o valor do depósito em R$: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("\nInforme o valor do saque em R$: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )

        elif opcao == 3:
            extratos(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("\nOperação inválida. Selecione novamente a operação desejada.")

main()

