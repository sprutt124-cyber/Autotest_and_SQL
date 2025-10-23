import sender_stand_request
import data

def test_get_order_by_track():
    # 1. Создаём заказ
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201  # проверяем, что заказ создан

    # 2. Сохраняем трек
    track = response.json()["track"]

    # 3. Проверяем заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200  # заказ найден
