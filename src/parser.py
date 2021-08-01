import utils
import config
from tqdm import tqdm


def main():
    print(config.INTRO)
    max_pages = utils.analysis_pagination()
    goods = utils.take_goods(max_pages)
    group_goods = utils.sort_product(goods)
    for value in tqdm(config.SPREADSHEET_NAMES, desc='Create spreadsheets'):
        utils.build_spreadsheet(group_goods[value], value,
                                config.TABLE_SETTINGS[value]['headings'],
                                config.TABLE_SETTINGS[value]['column_width'],
                                config.TABLE_SETTINGS[value]['column'])
    print('Ready! See the output folder...')


if __name__ in '__main__':
    main()
