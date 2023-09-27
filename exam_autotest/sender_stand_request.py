import requests

import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.body, headers=data.headers)

def get_order_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER_PATH + "?t=" + str(track_number))