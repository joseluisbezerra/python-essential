import xlrd, os

from modules import utils, get, show

def main():

    DATA_DIRECTORY = utils.find_or_exception_xlsx_directory()
    DATA = xlrd.open_workbook(DATA_DIRECTORY)
    RECORDS_WORKSHEET = DATA.sheet_by_index(0)
    ACCOUNTS_WORKSHEET = DATA.sheet_by_index(1)
    ACCOUNTS = get.get_accounts_data(ACCOUNTS_WORKSHEET)
    RECORDS = get.get_records_data(DATA, RECORDS_WORKSHEET)
    LOGS = get.get_logs_data()

    while True:
        LOG_ERRORS = 4
        EXIT = 5

        show.show_header()

        try:
            response = int(input('Selecione uma opção: '))
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[;1mInsira um valor válido!\033[0;0m\n')
            continue

        if response == LOG_ERRORS:
            os.system('cls' if os.name == 'nt' else 'clear')
            show.show_log_errors(LOGS)

        elif response == EXIT:
            utils.clear_log_errors()
            print('Saindo...')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[;1mInsira um valor válido!\033[0;0m\n')
            continue

main()