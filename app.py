from driver import create_driver
from article import get_article
from translation import get_translation
from wykop_api import authenticate_api, get_links, add_comment
import time

interval_minutes = 5
driver = None

def log(*messages):
    log = open("transbot.log", "a")
    for message in messages:
        log.write(message + "\n")
        print(message)

def handle_links(links):
    for link in links:
        log("### title:", link.title)
        log("### url:", link.source_url)
        driver = create_driver()
        article = get_article(driver, link.source_url)
        if article:
            translation = get_translation(driver, article)
            if translation:
                log(translation)
                add_comment(link.id, translation)
            else:
                log(
                    "###",
                    "polish article"
                    if translation == None
                    else "translation not found (timeout?)",
                )
        else:
            log("### scraping article failed")
        driver.close()

while True:
    log("### fetching new links")
    try:
        authenticate_api()
        links = get_links()
        log("### number of matching links: " + str(len(links)))
        handle_links(links)
    except Exception as e:
        log("### something went wrong:")
        log(str(e))
    finally:
        if driver:
            driver.quit()
            driver = None
    log("### sleeping...")
    time.sleep(interval_minutes * 60)
