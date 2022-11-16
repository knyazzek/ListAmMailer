import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from time import sleep

import config
from post import Post


def get_html_response(url):
    request = requests.get(url, headers=config.REQUEST_HEADER)

    if request.status_code != 200:
        print("Not 200")
        return None
    else:
        return BeautifulSoup(request.text, 'html.parser')


def get_new_posts(last_check_datetime, last_post_urls):
    page_html = get_html_response(config.TARGET_URL)
    if not page_html:
        return None

    posts_html = page_html.body.find(id='contentr').contents[1].contents[1:-2]
    new_posts = []

    for post_html in posts_html:
        post = Post.from_html(post_html)

        if post:
            if not post.is_actual(last_check_datetime, last_post_urls):
                break
            elif post.is_valid():
                new_posts.append(post)

    return new_posts


def send_updates(posts):
    if posts:
        print("Start sending....")

        for post in posts:
            print(post)

        print("Sending end!")
    else:
        print("Nothing to send...")


def main():
    last_check_datetime = datetime.now() - timedelta(seconds=config.REQUESTS_INTERVAL_SEC)
    last_post_urls = []

    while True:
        new_posts = get_new_posts(last_check_datetime, last_post_urls)

        # Update last check data
        last_post_urls = [post.url for post in new_posts]
        last_check_datetime = datetime.now()

        send_updates(new_posts)

        sleep_duration = config.REQUESTS_INTERVAL_SEC - 30
        print(f"Sleep {sleep_duration} seconds...")
        sleep(sleep_duration)


if __name__ == '__main__':
    main()
