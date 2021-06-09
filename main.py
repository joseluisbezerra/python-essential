import xlrd

from modules import utils, gets


DATA_DIRECTORY = utils.find_or_exception_xlsx_directory()
DATA = xlrd.open_workbook(DATA_DIRECTORY)
RECORDS_WORKSHEET = DATA.sheet_by_index(0)
ACCOUNTS_WORKSHEET = DATA.sheet_by_index(1)

print(gets.get_accounts_data(ACCOUNTS_WORKSHEET))
print(gets.get_records_data(DATA, RECORDS_WORKSHEET))