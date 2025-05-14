import configuration
import requests
import data


# Создание клиентом нового заказа
def post_new_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=orders_body) 


# Проверяется, что по треку заказа можно получить данные о заказе.
def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))