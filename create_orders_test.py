import sender_stand_request
import data
import requests

# Наталья Бушуева, 29-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест 1. Проверка номера трека заказа
def test_create_orders():
    # В переменную response сохраняется результат запроса на  создание заказа
    response = sender_stand_request.post_new_orders(data.orders_body)
    # В переменную track, сохраняется номер трека
    track = response.json()["track"]
    # В переменную response сохраняется результат выполнения запроса на получения заказа по треку заказа
    response = sender_stand_request.get_orders_track(track)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200