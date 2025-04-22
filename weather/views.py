from django.shortcuts import render
import requests

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        api_key = "82bb6a81c10f2aa6b64b7c97f6fa1624"
        source = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

        try:
            list_of_data = requests.get(source).json()
            if list_of_data.get("cod") != 200:
                data = {"error": f"City '{city}' not found!"}
            else:
                data = {
                    "country_code": str(list_of_data.get('sys', {}).get('country', 'N/A')),
                    "coordinate": f"{list_of_data.get('coord', {}).get('lon', 'N/A')} {list_of_data.get('coord', {}).get('lat', 'N/A')}",
                    "temp": list_of_data.get('main', {}).get('temp', 'N/A'),
                    "pressure": list_of_data.get('main', {}).get('pressure', 'N/A'),
                    "humidity": list_of_data.get('main', {}).get('humidity', 'N/A')
                }
        except requests.exceptions.RequestException as e:
            data = {"error": "Weather API request failed!"}
    else:
        data = {}

    return render(request, "weather.html", data)
