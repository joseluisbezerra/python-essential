import xlrd

from modules import utils


DATA_DIRECTORY = utils.find_xlsx_directory()
DATA = xlrd.open_workbook(DATA_DIRECTORY)
RECORDS_WORKSHEET = DATA.sheet_by_index(0)
ACCOUNTS_WORKSHEET = DATA.sheet_by_index(1)