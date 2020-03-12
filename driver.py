from selenium import webdriver


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--lang=pl")
    options.add_argument("window-size=1920x1080")
    options.add_argument(
        "--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'"
    )
    return webdriver.Chrome("chromedriver", options=options)
