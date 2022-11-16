from dataclasses import dataclass
from datetime import datetime
import re

import config
from config import LIST_AM_URL
from datetime_utils import convert_to_datatime


@dataclass
class Post:
    url: str
    price: int
    district: str
    rooms: int
    datetime: datetime

    def is_actual(self, previous_check_datetime, previous_post_urls):
        if self.datetime < previous_check_datetime or self.url in previous_post_urls:
            return False

        return True

    def is_valid(self):
        if self.price < config.MIN_PRICE or self.price > config.MAX_PRICE:
            return False

        if self.district not in config.DISTRICTS:
            return False

        if self.rooms < config.MIN_ROOMS or self.rooms > config.MAX_ROOMS:
            return False

        return True

    @staticmethod
    def from_html(html):
        if ('class' in html.attrs) and ('h' in html['class']):  # h means ad
            return None

        url = LIST_AM_URL + html['href']
        img_url = html.img['data-original']

        content = html.div

        title = content.contents[0].contents[0]
        price_str = content.contents[1].contents[0].contents[0]     # 200,000 ֏ в месяц
        price = int(extract_value('(\d*)\s֏\sв\sмесяц', price_str.replace(',', '')))

        desc = content.contents[2].contents[0]  # Арабкир, 1 ком., 25 кв.м., 1/5 этаж
        district, rooms_str, _, _ = desc.split(", ")
        rooms = int(extract_value('(\d)\sком.', rooms_str))

        datetime_str = content.contents[3].contents[0]
        dt = convert_to_datatime(datetime_str)

        return Post(url, price, district, rooms, dt)

    def __str__(self):
        return f'{self.url}, price: {self.price}, district: {self.district}, data: {self.datetime}'


def extract_value(regex_pattern, string):
    match = re.match(regex_pattern, string)
    if match:
        return match.group(1)
    else:
        return None
