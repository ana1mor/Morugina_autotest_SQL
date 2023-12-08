import configuration
import requests

#Создаем заказ:
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
#Получаем трек-номер заказа:
def get_new_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK,
                        params={"t": track})
