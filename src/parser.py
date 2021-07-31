import utils


def main():
    max_pages = utils.analysis_pagination()
    goods = utils.take_goods(max_pages)


if __name__ in '__main__':
    main()