# Sistema Bancário Versão 1.1

Este é um sistema bancário simples desenvolvido em Python. Ele permite criar clientes e contas bancárias, realizar depósitos, saques e visualizar extratos.

## Funcionalidades

- **Cadastrar Novo Cliente:** Adiciona um novo cliente ao sistema.
- **Criar Nova Conta:** Criar uma nova conta bancária associada a um cliente existente.
- **Realizar Depósito:** Permite depositar um valor na conta bancária.
- **Realizar Saque:** Permite sacar um valor da conta bancária, sujeito a limites.
- **Ver Extrato:** Exibe o extrato da conta bancária, mostrando saques, depósitos e o saldo.

## Requisitos

- Python 3.x

## Como Usar

1. Clone este repositório.

2. Navegue até o diretório do projeto.

3. Execute o script Python.

4. Escolha uma das opções do menu para interagir com o sistema.

### Descrição das opções

- **[1] Depósito:** Permite realizar um depósito na conta bancária.
- **[2] Saque:** Permite realizar um saque da conta bancária. O limite máximo para saque é de R$ 500 por operação, e até 3 saques por dia.
- **[3] Extrato:** Exibe o extrato da conta bancária, mostrando o número de saques, depósitos e o saldo atual.
- **[4] Cadastrar Clientes:** Adiciona um novo cliente ao sistema.
- **[5] Criar Conta:** Cria uma nova conta bancária para um cliente já cadastrado.
- **[0] Sair:** Encerra o sistema.

## Estrutura do Código
- `criar_cliente(clientes)`: Função para cadastrar um novo cliente.
- `criar_conta(AGENCIA, num_cpf, num_conta, clientes)`: Função para criar uma nova conta bancária.
- `realizar_deposito(saldo, qtd_dep)`: Função para realizar um depósito.
- `realizar-saque(*, saldo, saque, qtd_saque)`: Função para realizar um saque.
- `ver_extrato(saldo, qtd_saque, *, qtd_dep)`: Função para visualizar o extrato da conta.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT.

# Contato

Para mais informaçõe, entre em contato pelo **email:** quasedev@protonmail.com
Ou através do meu **LinkedIn:** [Francis Monteles](https://www.linkedin.com/in/francis-monteles-693064255/)
