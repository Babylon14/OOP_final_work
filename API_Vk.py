import requests
import configparser
from tqdm import tqdm


config = configparser.ConfigParser()
config.read("settings.ini")

vk_token = config["Tokens"]["vk_token"]
jd_token = config["Tokens"]["jd_token"]


"""Получение инфо о 5-ти фото профиля максимального размера"""
class VkAPI:
    pass