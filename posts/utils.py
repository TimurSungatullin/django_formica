import requests

from django_formica.settings import API_KEY


def get_temp():
    url = 'https://api.weather.yandex.ru/v2/informers?lat=55.7887&lon=49.1221'
    headers = {'X-Yandex-API-Key': API_KEY}
    res = requests.get(url, headers=headers)
    try:
        return res.json()['fact']['temp']
    except Exception:
        return 0
