## Утилита для обработки CSV-файлов с возможностью фильтрации и агрегации данных ##

## Начало работы ##

**Клонировать репозиторий и перейти в него в командной строке:**
git clone https://github.com/Egor-lazarev/processor_csv.git  
**или**
git clone git@github.com:Egor-lazarev/processor_csv.git  
**Переходим в директорию проекта:**
cd processor_crv/  

**Виртуальное окружение:**
**Создать:** python3 -m venv venv  
**Активировать:** source venv/bin/activate  

**Установить зависимости из файла requirements.txt:**
pip install -r requirements.txt  
**Обновить PIP**
python3 -m pip install --upgrade pip  

## Тесты ##

**Запуск тестов:**
pytest  
**Проверить покрытие тестами:**
pytest --cov=.  
**Общее покрытие тестами составляет - 97%**  

**Команды:** 
python main.py --file products.csv --where 'brand=xiaomi'  
python main.py --file products.csv --aggregate 'rating=max'  
python main.py --file products.csv --where 'brand=xiaomi' --aggregate 'rating=max' (комбинированный)  

## Автор: ##
_Лазарев Егор Антонович_
