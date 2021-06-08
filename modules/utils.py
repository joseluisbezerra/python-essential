import os

def find_xlsx_directory():
    XLSX_DIRECTORY = os.path.join(os.getcwd(), 'data')
    XLSX_EXTENSION = '.xlsx'
    for file in os.listdir(XLSX_DIRECTORY):
        if file.endswith(XLSX_EXTENSION):
            return os.path.join(XLSX_DIRECTORY, file)