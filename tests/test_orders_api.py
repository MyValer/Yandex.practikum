import pytest
import requests

def test_order_creation_and_retrieval(api_url):
    """Тест создания заказа и получения по трек-номеру"""
    # 1. Подготовка данных заказа
    order_data = {
        "firstName": "John",
        "lastName": "Doe",
        "address": "Moscow",
        "metroStation": 4,
        "phone": "+7 123 456 78 90",
        "rentTime": 5,
        "deliveryDate": "2025-04-15",
        "comment": "Test order",
        "color": ["BLACK"]
    }
    
    # 2. Создание заказа (POST)
    create_response = requests.post(
        f"{api_url}/api/v1/orders", 
        json=order_data,
        headers={'Content-Type': 'application/json'}
    )
    assert create_response.status_code == 201, f"Ошибка создания: {create_response.text}"
    
    # 3. Получение трек-номера
    track_number = create_response.json()["track"]
    assert track_number is not None, "Трек-номер не получен"
    
    # 4. Получение заказа по треку (GET)
    get_response = requests.get(f"{api_url}/api/v1/orders/track?t={track_number}")
    assert get_response.status_code == 200, f"Ошибка получения: {get_response.text}"
    
    # 5. Проверка данных (опционально)
    order = get_response.json()["order"]
    assert order["firstName"] == "John", "Неверное имя в ответе"
