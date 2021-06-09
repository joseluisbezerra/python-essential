import os

from modules import utils

def show_header():
    print('\033[;1mBanco da WLC Soluções\033[0;0m')
    print('1 - Mostrar saldo total por pessoa;')
    print('2 - Mostrar saldo total por conta;')
    print('3 - Mostrar total de todas as contas por data;')
    print('4 - Mostrar os logs de erros;')
    print('5 - Sair')


def show_log_errors(logs):
    if logs:
        for id, log in enumerate(logs):
            print(f'{id + 1} - {log}')
    else:
        print('Não há erros!')