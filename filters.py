import json


def weather(data):
    'filter weather api data'

    d = data["forecastTimestamps"][0]

    return (f"weather in {data['place']['name']} is {d['conditionCode']}, "
            f"temperature: {d['airTemperature']} C\N{DEGREE SIGN}, "
            f"wind speed: {d['windSpeed']} m/s, "
            f"wind gusts: {d['windGust']} m/s, "
            f"wind direction: {d['windDirection']}\N{DEGREE SIGN}, "
            f"coulds: {d['cloudCover']} %, "
            f"preasure: {d['seaLevelPressure']} mbar, "
            f"humidity: {d['relativeHumidity']} %, "
            f"precipitation: {d['totalPrecipitation']} mm")


def filter_cities_file():
    'one time file filtering function'
    new = []
    with open('locations.json') as json_file:
        f = json.load(json_file)
        for list in f.items():
            for l in list[1]:
                new.append({
                    'code': l['code'],
                    'country': l['countryCode']
                })
    # print(len(new))

    with open('list.json', 'w') as outfile:
        json.dump(new, outfile)
