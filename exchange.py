import re
import requests
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(valute_name):
    for exc in load_exchange()['Valute']:
        if valute_name == exc:
            return load_exchange()['Valute'][exc]
    return False


# def get_exchanges(ccy_pattern):
#     result = []
#     ccy_pattern = re.escape(ccy_pattern) + '.*'
#     for exc in load_exchange():
#         if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
#             result.append(exc)
#     return result


# print(load_exchange()['Valute'])


print(get_exchange('USD'))