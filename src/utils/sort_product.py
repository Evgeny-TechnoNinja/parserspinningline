from config import TYPES_GOODS  # noqa


def sort_product(goods):
    """Sorts the product, making a group of products from it.
    :param goods: goods from the store
    :return: product by category
    """
    data = {'swivel': [], 'bait': [], 'corkscrew': []}
    for item in goods:
        name = item.get('product_name').split()[0]
        if name == TYPES_GOODS[0]:
            data['swivel'].append(item)
        elif name == TYPES_GOODS[1]:
            data['bait'].append(item)
        elif name == TYPES_GOODS[2]:
            data['corkscrew'].append(item)
    return data
