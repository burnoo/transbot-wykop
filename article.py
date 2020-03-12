from newspaper import Article
import re


def get_article(driver, url):
    driver.get(url)

    article = Article("")
    article.set_html(driver.page_source)
    article.parse()

    text = article.text
    text = re.sub(r"[\n ]+", " ", text, flags=re.M)

    return text
