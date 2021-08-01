TARGET_URL = 'https://spinningline.ru/'
TARGET_PATH = 'yummy-m-46428.html'
NAVIGATION_NAME = 'page'
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/4.0)'
MARKUP_ANALYZER = 'lxml'
TYPES_GOODS = ['Вертлюг', 'Приманка', 'Штопор']
RESULT_FOLDER = 'output'
SPREADSHEET_NAMES = ['swivel', 'bait', 'corkscrew']
HEADING_STYLE = {'bold': True}
TABLE_SETTINGS = {
    'swivel': {
        'headings': [('A1', 'Имя товара'), ('B1', 'Изображение'),
                     ('C1', 'Код товара'), ('D1', 'Цена'),
                     ('E1', 'Номер'), ('F1', 'Нагрузка'), ('G1', 'Упаковка')],
        'column_width': [('A:A', 27), ('B:B', 20), ('C:C', 10), ('D:D', 10), ('E:E', 10), ('F:F', 10), ('G:G', 10)],
        'column': ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    },
    'bait': {
        'headings': [('A1', 'Имя товара'), ('B1', 'Изображение'),
                     ('C1', 'Код товара'), ('D1', 'Цена'),
                     ('E1', 'Вес'), ('F1', 'Вид ловли'), ('G1', 'Длинна'),
                     ('H1', 'Страна изготовления'), ('I1', 'Тип'), ('J1', 'Упаковка'),
                     ('K1', 'Форма'), ('L1', 'Цвет')],
        'column_width': [('A:A', 27), ('B:B', 20), ('C:C', 10), ('D:D', 10),
                         ('E:E', 10), ('F:F', 10), ('G:G', 10), ('H:H', 10),
                         ('I:I', 10), ('J:J', 10), ('K:K', 10), ('L:L', 10)],
        'column': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    },
    'corkscrew': {
        'headings': [('A1', 'Имя товара'), ('B1', 'Изображение'),
                     ('C1', 'Код товара'), ('D1', 'Цена'),
                     ('E1', 'Размер'), ('F1', 'Упаковка')],
        'column_width': [('A:A', 27), ('B:B', 20), ('C:C', 10), ('D:D', 10), ('E:E', 10), ('F:F', 10)],
        'column': ['A', 'B', 'C', 'D', 'E', 'F']
    }
}

INTRO = fr"""
    ┌─┐┌─┐┬─┐┌─┐┌─┐┬─┐  ┌─┐┌─┐┬┌┐┌┌┐┌┬┌┐┌┌─┐┬  ┬┌┐┌┌─┐
    ├─┘├─┤├┬┘└─┐├┤ ├┬┘  └─┐├─┘││││││││││││ ┬│  ││││├┤ 
    ┴  ┴ ┴┴└─└─┘└─┘┴└─  └─┘┴  ┴┘└┘┘└┘┴┘└┘└─┘┴─┘┴┘└┘└─┘
    From here {TARGET_URL} we take this "Yummy"           
    """

success = 'Ready! See the output folder...'