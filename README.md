# Parser Spinningline

Парсинг интернет-магазина  [spinningline.ru](https://spinningline.ru/)

## Что делает

Забирает из интернет-магазина всю продукцию Yummy. 
Сортирует товар по категориям и  записывает в электронные таблицы Excel.

## Как пользоваться
⚠️ _В связи с обстановкой, доступ к интернет-магазину из некоторых регионов может быть заблокирован. 
Что бы парсер работал, как вариант можете пустить свой трафик через анонимную сеть Tor. После чего можно приступать к парсингую_

_Предварительно должен быть установлен Python, Pip, система управления версиями Git_

**Приступаем!**
1. `git clone https://github.com/Evgeny-TechnoNinja/parserspinningline.git`
2. `cd parserspinningline`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt` 
6. `pip install --upgrade pip`
7. `cd src`
8. `python parser.py`

Результат работы смотреть в каталоге output, который появится в каталоге parserspinningline
