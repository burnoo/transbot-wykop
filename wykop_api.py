from datetime import datetime, timedelta
import wykop
import pytz
import yaml

config = yaml.safe_load(open("config.yaml"))
api = wykop.WykopAPI(config["app_key"], config["secret_key"])
tz = pytz.timezone("Europe/Warsaw")

def authenticate_api():
    api.authenticate(config["account_login"], config["account_key"])

def filter_url(url):
    domain = url.split("/")[2]
    ignored_domains = yaml.safe_load(open("ignored_domains.yaml"))
    return domain[-3:] != ".pl" and all([i not in domain for i in ignored_domains])


def filter_in_interval(date, interval_minutes, now):
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz)
    return now - dt < timedelta(minutes=interval_minutes)


def get_links(interval_minutes):
    now = datetime.now(tz).replace(tzinfo=tz)

    links = api.get_links_upcoming()
    links_filtered = [
        link
        for link in links
        if filter_url(link.source_url)
        and filter_in_interval(link.date, interval_minutes, now)
    ]
    return links_filtered


comment = """**Transbot v0.0.1** - bot tłumaczący artykuły przy pomocy deepl.com | [GitHub](https://github.com/burnoo/transbot-wykop)
_Przetłumaczony artykuł:_

{}

P.S. Proszę administrację o odblokowanie dostępu do dodawania nowych aplikacji API dla [konta bota](http://www.wykop.pl/ludzie/transbot) - wolałbym żeby to z niego były pisane komentarze. Przez panel kontaktowy niestety się nie udało :("""


def add_comment(link_id, text):
    api.add_comment(link_id=link_id, comment_id=None, body=comment.format(text))
