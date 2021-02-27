import json
import requests
import datetime as DT


class Voronezh1():
    
    def Voronezh1_departure():
        text_departure = ""
        current_date = DT.date.today()
        link = f"https://api.rasp.yandex.net/v3.0/schedule/?apikey=f3a6c277-5bcc-48d9-95ed-6373ba1b6fa5&station=s2014001&transport_types=train,suburban&direction=departure&date={current_date}"
        r = requests.get(link)
        trains = r.json()
        for train in trains["schedule"]:
            departure = train['departure']
            departure = DT.datetime.fromisoformat(departure)
            if departure < DT.datetime.now(departure.tzinfo):
                continue
            

            text_departure+=f"🚉 Станция: {trains['station']['title']}\n"
            text_departure+=f"🚦 Отправка в {departure}\n"
            text_departure+=f"#️⃣ Номер поезда: {train['thread']['number']}\n"
            text_departure+=f"🟢 Направление: {train['thread']['title']}\n"

            text_departure+='\n' + '-' * 10 + '\n'
        return text_departure


    def Voronezh1_arrival():
        text_arrival = ""
        current_date = DT.date.today()
        link = f"https://api.rasp.yandex.net/v3.0/schedule/?apikey=f3a6c277-5bcc-48d9-95ed-6373ba1b6fa5&station=s2014001&transport_types=train,suburban&event=arrival&date={current_date}"
        r = requests.get(link)
        trains = r.json()
        for train in trains["schedule"]:
            arrival = train['arrival']
            arrival = DT.datetime.fromisoformat(arrival)
            if arrival < DT.datetime.now(arrival.tzinfo):
                continue
            

            text_arrival+=f"🚉 Станция: {trains['station']['title']}\n"
            text_arrival+=f"🏁 Прибытие {arrival}\n"
            text_arrival+=f"#️⃣ Номер поезда: {train['thread']['number']}\n"
            text_arrival+=f"🟢 Направление: {train['thread']['title']}\n"

            text_arrival+='\n' + '-' * 10 + '\n'
        return text_arrival


    def Voronezh1_get_content():
        ARR=Voronezh1.Voronezh1_arrival()
        DEP=Voronezh1.Voronezh1_departure()
        return ARR+DEP


class Pridacha():

    def Pridacha_departure():
        text_departure = ""
        current_date = DT.date.today()
        link = f"https://api.rasp.yandex.net/v3.0/schedule/?apikey=f3a6c277-5bcc-48d9-95ed-6373ba1b6fa5&station=s9605143&transport_types=train,suburban&direction=departure&date={current_date}"
        r = requests.get(link)
        trains = r.json()
        for train in trains["schedule"]:
            departure = train['departure']
            departure = DT.datetime.fromisoformat(departure)
            if departure < DT.datetime.now(departure.tzinfo):
                continue
            

            text_departure+=f"🚉 Станция: {trains['station']['title']}\n"
            text_departure+=f"🚦 Отправка в {departure}\n"
            text_departure+=f"#️⃣ Номер поезда: {train['thread']['number']}\n"
            text_departure+=f"🟢 Направление: {train['thread']['title']}\n"

            text_departure+='\n' + '-' * 10 + '\n'
        return text_departure


    def Pridacha_arrival():
        text_arrival = ""
        current_date = DT.date.today()
        link = f"https://api.rasp.yandex.net/v3.0/schedule/?apikey=f3a6c277-5bcc-48d9-95ed-6373ba1b6fa5&station=s9605143&transport_types=train,suburban&event=arrival&date={current_date}"
        r = requests.get(link)
        trains = r.json()
        for train in trains["schedule"]:
            arrival = train['arrival']
            arrival = DT.datetime.fromisoformat(arrival)
            if arrival < DT.datetime.now(arrival.tzinfo):
                continue
            

            text_arrival+=f"🚉 Станция: {trains['station']['title']}\n"
            text_arrival+=f"🏁 Прибытие в {arrival}\n"
            text_arrival+=f"#️⃣ Номер поезда: {train['thread']['number']}\n"
            text_arrival+=f"🟢 Направление: {train['thread']['title']}\n"

            text_arrival+='\n' + '-' * 10 + '\n'
        return text_arrival


    def Pridacha_get_content():
        ARR=Pridacha.Pridacha_arrival()
        DEP=Pridacha.Pridacha_departure()
        return ARR+DEP



