# Наталья Шелопугина, 8-а когорта, Венера — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_track_order_get_success_response():

    response = sender_stand_request.post_new_order()
    track_number = response.json()["track"]

    response = sender_stand_request.get_order_by_track_number(track_number)
    assert response.status_code == 200
