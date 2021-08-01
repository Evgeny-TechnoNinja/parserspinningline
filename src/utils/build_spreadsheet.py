import xlsxwriter
from .create_output_folder import create_output_folder
from config import HEADING_STYLE  # noqa


@create_output_folder
def build_spreadsheet(data, name, headings, column_width, column):
    """Build an Excel spreadsheet.
    :param data: product with category
    :param name:  spreadsheet file name
    :param headings: header settings
    :param column_width: column width settings
    :param column: how many columns, list of letters
    """
    keys = list(data[0].keys())
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()
    style = workbook.add_format(HEADING_STYLE)
    row = 2
    # header
    for item in headings:
        worksheet.write(item[0], item[1], style)
    for item in column_width:
        worksheet.set_column(item[0], item[1])
    # body
    for value in data:
        for index, col in enumerate(column):
            worksheet.write(f'{col + str(row)}', value.get(keys[index]))
        row += 1
    workbook.close()
