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
        data_list.append(worksheet.row_values(id_row))
    return data_list