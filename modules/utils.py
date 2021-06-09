import os

def find_or_exception_xlsx_directory():
    XLSX_DIRECTORY = os.path.join(os.getcwd(), 'data')
    XLSX_EXTENSION = '.xlsx'
    for file in os.listdir(XLSX_DIRECTORY):
        if file.endswith(XLSX_EXTENSION):
            return os.path.join(XLSX_DIRECTORY, file)

    raise Exception(f'Não existe nenhum arquivo .xlsx no diretório {XLSX_DIRECTORY}')


def find_or_create_error_logs_directory():
    LOG_DIRECTORY = os.path.join(os.getcwd(), 'error_logs')
    LOG_EXTENSION = '.txt'

    for file in os.listdir(LOG_DIRECTORY):
        if file.endswith(LOG_EXTENSION):
            return os.path.join(LOG_DIRECTORY, file)

    return os.path.join(LOG_DIRECTORY, 'logs.txt')


def create_log_error(worksheet, id_row, id_col):
    logs = open(find_or_create_error_logs_directory(), 'a', encoding="utf-8")
    logs.write(f"Célula da linha {id_row} e coluna {id_col} referente ao campo {worksheet.row_values(0)[id_col]} na planilha {worksheet.name} está vázia, toda a linha será ignorada;\n")
    logs.close()