# Анастасия Моругина , 11-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

#Тестируем создание заказа
def test_make_order():
    make_response = sender_stand_request.post_new_order(data.order_body)
    track = make_response.json()["track"]
    order_response = sender_stand_request.get_new_order_track(track)
    assert order_response.status_code == 200