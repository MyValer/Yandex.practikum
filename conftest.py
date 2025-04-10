import pytest
import requests
import logging
import os

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='/var/www/backend/logs/error.log' if os.path.exists('/var/www/backend/logs') else 'error.log'
)

@pytest.fixture
def api_url():
    """Фикстура возвращает базовый URL тестируемого API"""
    return " https://2b96f650-001e-414a-8d36-5528472bdcfa.serverhub.praktikum-services.ru"  