#Павел Думнов, 36-я когорта - Финальный проект. Инженер по тестированию плюс
import configuration
import requests 
import data 
def post_new_order(body):
    return requests.post(configuration.URL+ configuration.PATHS["orders"],
                         json=body,
                         headers=data.headers) 
def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL + configuration.PATHS["track"], 
                        params=params)
