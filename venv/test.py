URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def load_exchange():
    return json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text)