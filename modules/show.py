import os

from modules import utils


def show_header():
    print('\033[;1mBanco da WLC Soluções\033[0;0m')
    print('1 - Mostrar saldo total por pessoa;')
    print('2 - Mostrar saldo total por conta;')
    print('3 - Mostrar total de todas as contas por data;')
    print('4 - Mostrar os logs de erros;')
    print('5 - Sair')


def show_balance_people(accounts, records):
    people_list = list()
    accounts_types_list = list()
    for account in accounts:
        people_list.append((account[1], 0))
        accounts_types_list.append((account[0], account[2]))

    accounts_type = dict(accounts_types_list)
    people_balance = dict(people_list)

    for record in records:
        if record[3] == accounts_type['Conta Corrente'] or record[3] == accounts_type['Conta Investimentos']:
            people_balance['Pessoa A'] += record[1]
        else:
            people_balance['Pessoa B'] += record[1]

    for key in people_balance:
        print(f'Saldo da {key}: {people_balance[key]}')

def show_balance_accounts(accounts, records):
    accounts_list = list()
    accounts_types_list = list()
    for account in accounts:
        accounts_list.append((account[2], 0))
        accounts_types_list.append((account[0], account[2]))

    accounts_type = dict(accounts_types_list)
    counts_balance = dict(accounts_list)

    for record in records:
        if record[3] == accounts_type['Conta Corrente']:
            counts_balance['CCA'] += record[1]
        elif record[3] == accounts_type['Conta Investimentos']:
            counts_balance['CIA'] += record[1]
        else:
            counts_balance['CPB'] += record[1]

    for key in counts_balance:
        print(f'Saldo de todas as contas {key}: {counts_balance[key]}')

def show_log_errors(logs):
    if logs:
        for id, log in enumerate(logs):
            print(f'{id + 1} - {log}')
    else:
        print('Não há erros!')