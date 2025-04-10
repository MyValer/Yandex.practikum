# Автоматизированные тесты API

Этот проект содержит автоматизированные тесты для API заказов.

## Требования
- Python 3.8+
- pip

## Установка
1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте его:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`

## Запуск тестов
Выполните команду: `pytest tests/ -v`

## Логи
Логи приложения находятся в `/var/www/backend/logs/error.log`