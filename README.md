# VK to Yandex Disk Photo Uploader

## Описание
Данная программа предназначена для автоматического получения фотографий профиля пользователя из социальной сети ВКонтакте и загрузки их на Яндекс.Диск. Программа получает 5 фотографий максимального размера, сохраняет их на Яндекс.Диск в отдельную папку, а также создает JSON-файл с информацией о загруженных фотографиях.

## Используемые технологии
- Python 3
- requests
- tqdm (для отображения прогресса загрузки)
- configparser
- json
- datetime

## Настройка и запуск
1. **Установите необходимые библиотеки:**
   ```bash
   pip install requests tqdm
   ```
2. **Создайте файл настроек `settings.ini` в корне проекта:**
   ```ini
   [Tokens]
   vk_token = <ваш_токен_ВКонтакте>
   jd_token = <ваш_токен_Яндекс_Диска>
   ```
3. **Запустите программу:**
   ```bash
   python API_Vk.py
   ```
4. **Введите ID пользователя ВКонтакте** по запросу в консоли.

## Описание работы программы
- Программа запрашивает у пользователя ID профиля ВКонтакте.
- С помощью VK API получает информацию о 5 фотографиях профиля максимального размера.
- Для каждой фотографии формируется уникальное имя файла на основе количества лайков и текущей даты/времени.
- Создается папка `VK_photos` на Яндекс.Диске (если она еще не существует).
- Каждая фотография загружается на Яндекс.Диск с отображением прогресса загрузки.
- После завершения загрузки создается файл `vk_api_photos.json` с информацией о загруженных фотографиях (имя файла, размер, ссылка).

## Структура проекта
- `API_Vk.py` — основной скрипт программы
- `settings.ini` — файл с токенами доступа
- `vk_api_photos.json` — файл с информацией о загруженных фотографиях (создается автоматически)

## Примечания
- Для работы программы необходимы действующие токены VK и Яндекс.Диска.
- Программа загружает только 5 последних фотографий профиля пользователя.
- Все загруженные фотографии сохраняются в папку `VK_photos` на вашем Яндекс.Диске. 
