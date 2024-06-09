# Sistema Bancário Versão 1.1

# Inicializando variáveis de saldo e contadores de depósitos e saques
saldo = 0
saque = 0
qtd_dep = 0
qtd_saque = 0
num_conta = 0
num_cpf = 0
clientes = []
contas = []
AGENCIA = "0001"

def criar_cliente(clientes):
    '''
    Função para criar um novo cliente.

    Args:
        clientes (list): Lista de clientes existentes.

    Returns:
        list: Lista de clientes atualizada com o novo cliente.

    '''
    print("Você escolheu a opção Cadastrar Novo Cliente!")
    nome = input("Informe o seu nome: ")
    dt_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    num_cpf = input("Informe o seu número de CPF (somente números): ")
    endereco = input("Informe o seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"Nome": nome, "Data de nascimento": dt_nascimento, "CPF": num_cpf, "Endereço": endereco})

    print("Cliente cadastrado com sucesso!")
    print(f"Seja bem vindo, {nome}!\n")
    return clientes

def criar_conta(AGENCIA, num_cpf, num_conta, clientes):
    '''
    Função para criar uma uma nova conta bancária.

    Args:
        AGENCIA (str): Cógigo da âgencia.
        num_cpf (str): CPF do cliente.
        num_conta (int): Número da última conta criada.
        clientes (list):Lista de clientes cadastrados.

    Returns:
        tuple: Dados atualizados da âgencia, CPF, número da conta e lista de clientes.
    '''
    print("Você escolheu a opção Criar Nova Conta: ")
    num_cpf = input("Informe um CPF já cadastrado: ")
    cliente = next((cliente for cliente in clientes if cliente ["CPF"] == num_cpf), None)
    if cliente: 
        num_conta += 1
        contas.append({"Agencia": AGENCIA, "Número da conta": num_conta, "Clientes": cliente})
        print("Conta criada com sucesso. Número da conta: ", num_conta,"\n")
        return AGENCIA, num_cpf, num_conta, clientes
    else:
        print("Cliente não cadastrado. Por favor, criar cadastro primeiro! \n")
        return AGENCIA, None, num_conta, clientes

def realizar_deposito(saldo, qtd_dep, /):
    '''
    Função para realizar um depósito.

    Args:
        saldo (float): Saldo atual da conta.
        qtd_dep (int): Quantidade de depósitos realizados.

    Returns:
        tuple: Saldo atualizado e quantidade de dépositos.
    '''
    print("Você escolheu a opção Depósito.")
    deposito = float(input("Informe o valor que será depositado: "))
    if deposito > 0:
    # Se o valor for positivo
        print("Depósito realizado com sucesso!")
        saldo += deposito
        print(f"Valor depositado: R$ {deposito:.2f}")
        print(f"Saldo: R$ {saldo:.2f} \n")
        qtd_dep += 1
    else:
        print("Valor informado é inválido. \n")
    return saldo, qtd_dep

def realizar_saque(*, saldo, saque, qtd_saque):
    '''
    Função para realizar um saque.

    Args:
        saldo (float): Saldo atual da conta.
        saque (float): Valor a ser sacado.
        qtd_saque (int): Quantidadede de saques realizados.

    Returns:
        tuple: Saldo atualizado, valor do saque e quantidade de saques.
    '''
    print("Você escolheu a opção Saque.")
    saque = float(input("Informe o valor que deseja sacar: "))
    if saque > saldo:
        print("Saldo insuficiente! \n")
    elif saque > 500:
        print("O limite máximo para essa operação é de R$ 500. \n")
    elif qtd_saque >= 3:
        print("Operação não concluída. Número máximo de saques excedido. \n")
    # Realizando o saque se o valor estiver dentro do limites
    else:
        print("Saque realizado com sucesso!")
        saldo -= saque
        print(f"Valor do saque: R$ {saque:.2f}")
        print(f"Saldo: R$ {saldo:.2f} \n")
        qtd_saque += 1
    return saldo, saque, qtd_saque

def ver_extrato(saldo, qtd_saque, /, *, qtd_dep):
    '''
    Função para visualizar o extrato da conta.

    Args:
        saldo (float): Saldo atual da conta.
        qtd_saque (int): Quantidade de saques realizados.
        qtd_dep (int): Quantidade de depósitos realizados.

    Returns:
        tuple: Saldo, quantidade de saques e quantidade de depósitos.
    '''
    print("Você escolheu a opção Extrato.")
    print("Visualizar Extrato")
    if qtd_saque != 0 and qtd_dep != 0:
        # Exibindo informações do extrato se houver movimentações na conta
        print(f"Saques realizados: {qtd_saque}")
        print(f"Depósitos realizados: {qtd_dep}")
        print(f"Saldo: R$ {saldo:.2f} \n")
    else:
        print("Não foram realizadas movimentações na conta. \n")
    return saldo, qtd_saque, qtd_dep

# Loop principal do menu
while True:
    # Exibindo o menu inicial e solicitando uma escolha  do usuário
    menu_inicial = int(input('''Escolha uma das opções:
    [1] Depósito
    [2] Saque 
    [3] Extrato
    [4] Cadastrar Clientes
    [5] Criar Conta
    [0] Sair
    ''')) 

    # ÍNICIO DEPÓSITO
    if menu_inicial == 1:
        saldo, qtd_dep = realizar_deposito(saldo, qtd_dep)
    # FIM DEPÓSITO
            
    # ÍNICIO SAQUE
    elif menu_inicial == 2:
        saldo, saque, qtd_saque = realizar_saque(saldo = saldo, saque = saque, qtd_saque = qtd_saque)
    # FIM SAQUE

    # ÍNICIO EXTRATO
    elif menu_inicial == 3:
        saldo, qtd_saque, qtd_dep = ver_extrato(saldo, qtd_saque, qtd_dep = qtd_dep)
    # FIM EXTRATO

    # ÍNICIO CADASTRAR CLIENTE
    elif menu_inicial == 4:
        clientes = criar_cliente(clientes)
    # FIM CADASTRO CLIENTE

    # ÍNICIO CRIAR CLIENTE
    elif menu_inicial == 5:
        AGENCIA, num_cpf, num_conta, clientes = criar_conta(AGENCIA, num_cpf, num_conta, clientes)
    # FIM CRIAR CLIENTE

    # SAIR 
    elif menu_inicial == 0:
        print("Você escolheu a opção Sair.")
        print("Obrigado por usar este sistema. Até mais!!!")
        break

    else: 
        print("Opção inválida. Tente novamente.")
