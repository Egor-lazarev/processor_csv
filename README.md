## Утилита для обработки CSV-файлов с возможностью фильтрации и агрегации данных ##

## Начало работы ##

Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/Egor-lazarev/processor_csv.git
или
git clone git@github.com:Egor-lazarev/processor_csv.git
cd processor_crv/

Cоздать и активировать виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
python3 -m pip install --upgrade pip

## Тесты ##

Запуск тестов: pytest
Проверить покрытие тестами: pytest --cov=.
Общее покрытие тестами составляет - 97%

## Автор: ##
_Лазарев Егор Антонович_
