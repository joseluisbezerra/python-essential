def show_header():
    print('\033[;1mBanco da WLC Soluções\033[0;0m')
    print('1 - Mostrar saldo total por pessoa;')
    print('2 - Mostrar saldo total por conta;')
    print('3 - Mostrar total de todas as contas por data;')
    print('4 - Mostrar os logs de erros;')
    print('5 - Sair')


def show_balance_people(accounts, records):
    if accounts:
        people_accounts = dict()
        people_list = list()
        for account in accounts:
            if account[1] in people_accounts.keys():
                people_accounts[account[1]].append(account[2])
            else:
                people_accounts[account[1]] = [account[2]]
            people_list.append((account[1], 0))

        people_balance = dict(people_list)
        for record in records:
            for person in people_accounts:
                if record[3] in people_accounts[person]:
                    people_balance[person] += record[1]

        print('\033[;1mLista do saldo total por pessoa:\033[0;0m')
        for person in people_balance:
            print(f'Saldo da {person}: {people_balance[person]}')
    else:
        print('\033[;1mNão há contas na planilha!\033[0;0m')


def show_balance_accounts(accounts, records):
    if accounts:
        accounts_list = list()
        for account in accounts:
            accounts_list.append((account[2], 0))

        accounts_balance = dict(accounts_list)

        for record in records:
            accounts_balance[record[3]] += record[1]

        print('\033[;1mLista do saldo total por conta:\033[0;0m')
        for account in accounts_balance:
            print(
                f'Saldo de todas as contas {account}: {accounts_balance[account]}')
    else:
        print('\033[;1mNão há contas na planilha!\033[0;0m')


def show_balance_dates(accounts, records):
    if accounts:
        if records:
            date_list = list()
            for record in records:
                date_list.append((record[0], 0))

            date_balance = dict(date_list)

            for record in records:
                date_balance[record[0]] += record[1]

            print('\033[;1mLista do total de todas as contas por data:\033[0;0m')
            for date in date_balance:
                print(
                    f'Saldo de todas as operações das contas no {date}: {date_balance[date]}')
        else:
            print('\033[;1mNão há registros na planilha!\033[0;0m')
    else:
        print('\033[;1mNão há contas na planilha!\033[0;0m')


def show_log_errors(logs):
    if logs:
        print('\033[;1mLista de logs:\033[0;0m')
        for id, log in enumerate(logs):
            print(f'{id + 1} - {log}')
    else:
        print('\033[;1mNão há erros!\033[0;0m')
