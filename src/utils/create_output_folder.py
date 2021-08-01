import os
import os.path
import shutil
from config import RESULT_FOLDER, SPREADSHEET_NAMES  # noqa
from functools import wraps


def create_output_folder(func):
    """There is a decorator, it is used to create the final folder
     and place the file in it.
    :param func: function on which the add-in will be performed
    :return: wrapper
    """
    @wraps(func)
    def wrapper(data, name, headings, column_width, column):
        if os.path.isdir('../' + RESULT_FOLDER):
            func(data, name, headings, column_width, column)
        else:
            os.mkdir('../' + RESULT_FOLDER)
            func(data, name, headings, column_width, column)
        for item in SPREADSHEET_NAMES:
            item = item + '.xlsx'
            if os.path.exists(item):
                shutil.copy(item, '../' + RESULT_FOLDER)
                os.remove(item)
    return wrapper
