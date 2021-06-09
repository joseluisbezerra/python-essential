import datetime, xlrd
from modules import utils

def get_accounts_data(worksheet):
    data_list = list()
    for id_row in range(1, worksheet.nrows):
        ERRORS = 0
        EMPYT = ''
        for id_col, col in enumerate(worksheet.row_values(id_row)):
            if col == EMPYT:
                utils.create_log_error(worksheet, id_row, id_col)
                ERRORS += 1
        if ERRORS:
            continue
        data_list.append(tuple(worksheet.row_values(id_row)))
    return data_list

def get_records_data(data, worksheet):
    data_list = list()

    for id_row in range(1, worksheet.nrows):
        ERRORS = 0
        EMPYT = ''
        ID_DATE = 0
        data_validate = []
        for id_col, col in enumerate(worksheet.row_values(id_row)):
            if col == EMPYT:
                utils.create_log_error(worksheet, id_row, id_col)
                ERRORS += 1
            else:
                if id_col == ID_DATE:
                    col_validate = datetime.datetime(*xlrd.xldate_as_tuple(col, data.datemode)).strftime("%d/%m/%y")
                    col = col_validate
                data_validate.append(col)
        if ERRORS:
            continue
        data_list.append(tuple(data_validate))
    return data_list

def get_logs_data():
    data_list = list()
    try:
        logs = open(utils.find_or_create_error_logs_directory(), 'r', encoding="utf-8")
    except FileNotFoundError:
        return False
    for log in logs.readlines():
        data_list.append(log)
    return tuple(data_list)
    