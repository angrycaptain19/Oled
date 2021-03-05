import requests
import socket

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"
}

Q = {
    "key": "81d70d330760407b9102184d47874d2d",
    "location": "101190112"
}

L = {
    "key": "81d70d330760407b9102184d47874d2d",
    "location": "101280106"
}

url = "https://devapi.qweather.com/v7/weather/now"


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_weather(name):
    param = Q if name == "Q" else L
    res = ""
    try:
        response = requests.get(
        url=url,
        params=param,
        headers=headers,
        timeout=2.0
        )
        if response.status_code == 200:
            weather = response.json()["now"]
            res = "{0}:{1}/{2}/{3}%/{4}".format(
                name,
                weather["temp"],
                weather["feelsLike"],
                weather["humidity"],
                weather["text"]
            )
        else:
            res = "ERROR: {}".format(response.status_code)
    except requests.Timeout:
        res = "ERROR: TIMEOUT"

    return res