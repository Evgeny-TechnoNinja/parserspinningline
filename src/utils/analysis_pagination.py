from .get_document import get_document
from bs4 import BeautifulSoup
from config import TARGET_URL, TARGET_PATH, MARKUP_ANALYZER  # noqa


def analysis_pagination():
    """Finds the number of product pages.
    :return: maximum number (last page)
    """
    numbers = []
    document = get_document(TARGET_URL + TARGET_PATH)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    pagination_elements = list(soup.select('div.b-pager__lnk-list')[0])
    for element in pagination_elements:
        numbers.append(int(element['data-page']))
    return max(numbers)

