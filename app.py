from driver import create_driver
from article import get_article
from translation import get_translation
from wykop_api import authenticate_api, get_links, add_comment
import time

interval_minutes = 3
driver = None

def handle_links(links):
    for link in links:
        print("### title:", link.title)
        print("### url:", link.source_url)
        driver = create_driver()
        article = get_article(driver, link.source_url)
        if article:
            translation = get_translation(driver, article)
            if translation:
                print(translation)
                # TODO: add_comment(link.id, "tresc")
            else:
                print(
                    "###",
                    "polish article"
                    if translation == None
                    else "translation not found (timeout?)",
                )
        else:
            print("### scraping article failed")
        driver.close()

while True:
    print("### fetching new links")
    try:
        authenticate_api()
        links = get_links(interval_minutes)
        print("### number of matching links: " + str(len(links)))
        handle_links(links)
    except Exception as e:
        print("### something went wrong:")
        print(str(e))
    finally:
        if driver:
            driver.quit()
            driver = None
    print("### sleeping...")
    time.sleep(interval_minutes * 60)
