import requests
import json  # Добавим библиотеку для работы с JSON


def get_weather(city, api_key):
    # Укажите базовый URL для OpenWeatherMap (или другого сервиса)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Формируем полный URL запроса с параметрами
    # Для OpenWeatherMap: q - название города, appid - ваш API-ключ
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric&lang=ru"

    # Отправляем GET-запрос
    response = requests.get(complete_url)

    # Получаем данные в формате JSON
    data = response.json()

    # Проверяем, что запрос прошел успешно
    if data["cod"] != "404":
        # Извлекаем нужные данные
        main_data = data["main"]
        temperature = main_data["temp"]
        feels_like = main_data["feels_like"]
        description = data["weather"][0]["description"]
        print(data)
        # Выводим результат
        print(f"Температура в городе {city}: {temperature}°C")
        print(f"Ощущается как: {feels_like}°C")
        print(f"Погодные условия: {description}")
    else:
        print(f"Не удалось найти информацию о погоде для города {city}")


# Пример использования
if __name__ == "__main__":
    your_api_key = "cd033557f7f20b0b67ab72dde410b81e"  # Вставьте сюда ваш ключ
    city_name = input("Введите название города: ")
    get_weather(city_name, your_api_key)