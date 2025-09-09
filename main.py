import requests


def get_city_coordinates(city_name, api_key):
    url = "http://api.openweathermap.org/geo/1.0/direct"

    params = {
        'q': city_name,
        'limit': 5,
        'appid': api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Вызовет исключение для кодов 4xx/5xx

        data = response.json()

        if not data:
            print("Город не найден")
            return None

        return data

    except requests.exceptions.HTTPError as err:
        print(f"HTTP ошибка: {err}")
    except requests.exceptions.ConnectionError as err:
        print(f"Ошибка подключения: {err}")
    except requests.exceptions.Timeout as err:
        print(f"Таймаут: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка запроса: {err}")

    return None


# Использование
API_KEY = "c820e17840890e49f819d03eaff8532c"  # Получите на openweathermap.org
city_data = get_city_coordinates("London", API_KEY)

if city_data:
    for city in city_data:
        print(f"{city['name']}, {city['country']}: {city['lat']}, {city['lon']}")