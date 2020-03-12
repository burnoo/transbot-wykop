from datetime import datetime, timedelta
import wykop
import pytz
import yaml
from ignored_domains import ignored_domains

config = yaml.safe_load(open('config.yaml'))
api = wykop.WykopAPI(config['app_key'], config['secret_key'])
tz = pytz.timezone("Europe/Warsaw")


def filter_url(url):
    domain = url.split("/")[2]
    return domain[-3:] != ".pl" and all([i not in domain for i in ignored_domains])


def filter_in_interval(date, interval_minutes, now):
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz)
    return now - dt < timedelta(minutes=interval_minutes)


def get_links(interval_minutes):
    api.authenticate(config['account_login'], config['account_key'])

    now = datetime.now(tz).replace(tzinfo=tz)

    links = api.get_links_upcoming()
    links_filtered = [
        link
        for link in links
        if filter_url(link.source_url)
        and filter_in_interval(link.date, interval_minutes, now)
    ]
    return links_filtered


def add_comment(link_id, comment):
    api.add_comment(link_id=link_id, comment_id=None, body=comment)
