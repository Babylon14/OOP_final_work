import requests
import configparser
from tqdm import tqdm
import json
from pprint import pprint


config = configparser.ConfigParser()
config.read("settings.ini")

vk_token = config["Tokens"]["vk_token"]
jd_token = config["Tokens"]["jd_token"]


"""Получение инфо о 5-ти фото профиля максимального размера"""
class VkAPI:
    def __init__(self, token, version="5.199"):
        self.base_url = "https://api.vk.com/method/"
        self.base_params = {"access_token": token, "v": version}


    def get_photos(self, user_id, count=5):
        url = f"{self.base_url}photos.get"

        params = {
            "owner_id": user_id,
            "album_id": "profile",
            "rev": 1,
            "extended": 1,
            "photo_sizes": 1,
            "count": count
        }
        params.update(self.base_params)

        response = requests.get(url, params=params)
        return response.json()
    

vk_api = VkAPI(vk_token)
pprint(vk_api.get_photos())