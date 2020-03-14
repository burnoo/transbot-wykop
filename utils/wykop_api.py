import wykop
import yaml
import pickle
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
checked_path = os.path.join(dir_path, "checked.pickle")
ignored_domains_path = os.path.join(dir_path, "ignored_domains.yaml")
config = yaml.safe_load(open("config.yaml"))
api = wykop.WykopAPI(config["app_key"], config["secret_key"])


def get_checked():
    if os.path.exists(checked_path):
        with open(checked_path, "rb") as file:
            return pickle.load(file)
    else:
        return []


def update_checked(old_checked, new_checked):
    checked = old_checked + new_checked
    with open(checked_path, "wb") as file:
        pickle.dump(checked, file)


def authenticate_api():
    api.authenticate(config["account_login"], config["account_key"])


def filter_url(url):
    domain = url.split("/")[2]
    ignored_domains = yaml.safe_load(open(ignored_domains_path))
    return domain[-3:] != ".pl" and all([i not in domain for i in ignored_domains])


def get_links():
    checked = get_checked()
    links = api.get_links_promoted() + api.get_links_upcoming()
    links_filtered = [
        link for link in links if filter_url(link.source_url) and link.id not in checked
    ]
    update_checked(checked, [link.id for link in links_filtered])
    return links_filtered


comment = """**Transbot v0.0.1** - bot tłumaczący artykuły przy pomocy deepl.com | [GitHub](https://github.com/burnoo/transbot-wykop)
_Przetłumaczony artykuł:_

{}

P.S. Proszę administrację o odblokowanie dostępu do dodawania nowych aplikacji API dla [konta bota](http://www.wykop.pl/ludzie/transbot) - wolałbym żeby to z niego były pisane komentarze. Przez panel kontaktowy niestety się nie udało :("""


def add_comment(link_id, text):
    api.add_comment(link_id=link_id, comment_id=None, body=comment.format(text))
