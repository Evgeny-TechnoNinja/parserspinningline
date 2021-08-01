# Parser Spinningline

```
    ┌─┐┌─┐┬─┐┌─┐┌─┐┬─┐  ┌─┐┌─┐┬┌┐┌┌┐┌┬┌┐┌┌─┐┬  ┬┌┐┌┌─┐
    ├─┘├─┤├┬┘└─┐├┤ ├┬┘  └─┐├─┘││││││││││││ ┬│  ││││├┤ 
    ┴  ┴ ┴┴└─└─┘└─┘┴└─  └─┘┴  ┴┘└┘┘└┘┴┘└┘└─┘┴─┘┴┘└┘└─┘
```

Парсер интернет-магазина [spinningline.ru](https://spinningline.ru/)

## Что делает

Заберает из интерент-магазина всю продукцию Yummy. 
Сортирует товар по категориям и записывет в электронные таблицу Excel.

## Как пользоваться

_Предварительно должен быть установлен Python, Pip, и система управления версиями Git_

**Приступаем!**
1. `git clone https://github.com/Evgeny-TechnoNinja/parserspinningline.git`
2. `cd parserspinningline`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `cd src`
7. `python parser.py`

Результат работы смотреть в каталоге output, который появиться в каталоге parserspinningline
