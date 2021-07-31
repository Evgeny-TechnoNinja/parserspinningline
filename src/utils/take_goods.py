from typing import Dict, Any

from config import TARGET_URL, TARGET_PATH, MARKUP_ANALYZER, NAVIGATION_NAME, TYPES_GOODS  # noqa
from .get_document import get_document
from bs4 import BeautifulSoup


def take_goods(num):
    """Takes all the necessary goods from the online store
    :param num: number of product pages (maximum number)
    :return: list of dictionaries where each dictionary is a product with its parameters
    """
    goods = []
    for current_number in range(1, num + 1):
        payload = {NAVIGATION_NAME: str(current_number)}
        document = get_document(TARGET_URL + TARGET_PATH, parameter=payload)
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        box_product = soup.select('div.b-prod')
        for item in box_product:
            name = item.select('div.b-prod__name-text')[0].get_text()
            part_name = name.split()[0]
            blank = dict()
            blank['product_name'] = name
            blank['link_picture'] = item.select('a.b-prod__img-href>meta[itemprop]')[0]['content']
            values = item.select('span.b-prod-prop__val')
            blank['product_code'] = values[0].get_text()
            blank['price'] = item.select('div.b-prod__price>span.b-prod__price_red')[0].get_text()
            if part_name == TYPES_GOODS[0]:
                field_names = ['number', 'breaking_load', 'package']
                data = []
                for index, value in enumerate(values[1:]):
                    data.append(value.get_text())
                for index, value in enumerate(data):
                    blank[field_names[index]] = value
                    if index == 1:
                        blank[field_names[index]] = value + ' кг'
                    if index == 2:
                        blank[field_names[index]] = value + ' шт'
                goods.append(blank)
                del blank, field_names, data
            if part_name == TYPES_GOODS[1]:
                field_names = ['weigh', 'fishing_type', 'length', 'country',
                               'bait_type', 'package', 'bait_shape', 'color']
                data = []
                for index, value in enumerate(values[1:]):
                    data.append(value.get_text())
                data.insert(1, data.pop(1) + ', ' + data.pop(1))
                for index, value in enumerate(data):
                    blank[field_names[index]] = value # noqa
                    if index == 0:
                        blank[field_names[index]] = value + ' гр'
                    if index == 2:
                        blank[field_names[index]] = value + ' см'
                    elif index == 5:
                        blank[field_names[index]] = value + ' шт'
                goods.append(blank)
                del blank, field_names, data
            if part_name == TYPES_GOODS[2]:
                field_names = ['size', 'package']
                data = []
                for index, value in enumerate(values[1:]):
                    data.append(value.get_text())
                for index, value in enumerate(data):
                    blank[field_names[index]] = value # noqa
                    if index == 1:
                        blank[field_names[index]] = value + ' шт'
                goods.append(blank)
                del blank, field_names, data
    return goods
