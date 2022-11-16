DISTRICTS = ['Арабкир', 'Кентрон']
MIN_PRICE = 200000
MAX_PRICE = 300000
MIN_ROOMS = 2
MAX_ROOMS = 3

LIST_AM_URL = 'https://www.list.am'
TARGET_URL = f'https://www.list.am/ru/category/56?cmtype=1&pfreq=1&po=1&n=1&' \
             f'price1={MIN_PRICE}&price2={MAX_PRICE}&crc=0&gl=2'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/107.0.0.0 Mobile Safari/537.36 '
REQUEST_HEADER = {'User-Agent': USER_AGENT}

RECIPIENTS = ['Liza20002', 'giorgioooo_armani']
REQUESTS_INTERVAL_SEC = 100000
