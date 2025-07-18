# Обработка банковских операций
## Описание:
Модуль для фильтрации и сортировки банковских операций по статусу и дате выполнения.
## Установка:
### 1. Клонируйте репозиторий:
- git clone https://github.com/ваш-username/bank-operations.git
### 2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
### Основные функции модуля:

### 1. Фильтрация операций по статусу:
```
from src.processing import filter_by_state
executed_operations = filter_by_state(operations_list)
```
### 2.Сортировка операций по дате:
```
from src.processing import sort_by_date
sorted_operations = sort_by_date(operations_list)
```
## Пример данных:
Для тестирования можно использовать следующий формат данных:
```
operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]
```
## Проверка качества кода:
Проект использует следующие инструменты:
+ flake8 - проверка стиля кода
+ mypy - проверка типов
+ black - автоматическое форматирование
+ pytest - запуск тестов
## Документация:
Полная документация по функциям доступна в docstrings модуля processing.py.
## Лицензия:
Этот проект лицензирован по ***лицензии MIT***.