# bootcamp-dio-desafio2
Desafio de projeto de sistema bancário (versão 2) disponível na plataforma DIO, proposto pelo Bootcamp Potência Tech powered by iFood | Ciências de Dados com Python
## Descrição do Desafio
Precisa-se deixar o código mais modularizado, para isso é necessário criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 precisa-se criar duas novas funções: criar usuário (cliente do banco) e criar conta-corrente (vincular com usuário).
## Operação de depósito
A função de depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
## Operação de saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
## Operação de extrato
A função extrato deve receber por posição e nome (positional only e keyword only). Argumentos pocionais: saldo, argumentos nomeados: extrato
## Criar usuário (cliente): 
O programa deve armazenar os usuários em uma lista, um usuário é composto por nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro, bairro, cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
## Criar conta-corrente:
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
## Dica:
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
