import requests
import configparser
from tqdm import tqdm
import json


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

        response = requests.get(url, params=params).json()
        image = response.get("response", {}).get("items", [])

        image_info = []
        for img in image:
            max_size_photo = max(img["sizes"], key=lambda x: x["type"] == "z")
            photo_url = max_size_photo["url"]
            file_name_likes = img["likes"]["count"]

            image_info.append({
                "file_name": file_name_likes,
                "size": max_size_photo["type"]
            })
            
        return image_info


class JdAPI:
    def __init__(self, token):
        self.base_url = "https://cloud-api.yandex.net/v1/disk/"
        self.headers = {"Authorization": f"OAuth {jd_token}"}

    """Создение папки на Яндекс Диске"""
    def create_folder(self):
        url = f"{self.base_url}resources"
        params = {"path": "VK_photos"}

        response = requests.put(url, params=params, headers=self.headers)
        return response.status_code

    """Загрузка фото на Яндекс Диск с использованием модуля прогресс-бар"""
    def upload_photos(self, file_name_likes):
        url = f"{self.base_url}resources/upload"
        file_name = f"{file_name_likes}_likes.jpg"
        params = {"path": f"VK_photos/{file_name}"}

        with tqdm(desc=f"Загрузка {file_name}", unit="B", unit_scale=True, unit_divisor=1024) as progress_bar:
            response = requests.post(url, params=params, headers=self.headers, stream=True)
            
            if response.status_code == 202:
                for resp in response.iter_content(1024):
                    progress_bar.update(len(resp)) 
                return f"Фото {file_name} успешно загружено"
            else:
                return f"Ошибка {response.status_code}: {response.text}"


vk_api = VkAPI(vk_token)
jd_api = JdAPI(jd_token)

user_id = int(input("Введите ID пользователя: "))
vk_api.get_photos(user_id)

jd_api.create_folder()
jd_api.upload_photos()

