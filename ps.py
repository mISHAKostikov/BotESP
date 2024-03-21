import requests

mapa = {
    "temp"   : "http://iocontrol.ru/api/readData/VentESP/temperature?key=0pzst015nbqz4ylj9hi4",
    "hum"    : "http://iocontrol.ru/api/readData/VentESP/humidity?key=0pzst015nbqz4ylj9hi4",
    "lpg"    : "http://iocontrol.ru/api/readData/VentESP/lpg?key=0pzst015nbqz4ylj9hi4",
    "co"     : "http://iocontrol.ru/api/readData/VentESP/co?key=0pzst015nbqz4ylj9hi4",
    "alco"   : "http://iocontrol.ru/api/readData/VentESP/Alchogol?key=0pzst015nbqz4ylj9hi4",
    "propane": "http://iocontrol.ru/api/readData/VentESP/Propane?key=0pzst015nbqz4ylj9hi4"
}

def rq(url:str):
    r = requests.get(url)
    #print(r.json())
    return r.json()

def get_data(req: map):
    return req["value"]


def get_values():
    maper = {}
    for i in mapa.keys():
        maper.update({i: get_data(rq(mapa[i]))})
    return maper



