from selenium import webdriver
from utils.ublock import setup_driver
import os
from pyvirtualdisplay import Display

dir_path = os.path.dirname(os.path.realpath(__file__))
extension_path = os.path.join(dir_path, "ublock.crx")

display = Display(visible=0, size=(1920, 1080))
display.start()

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_extension(extension_path)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--lang=pl")
    options.add_argument("window-size=1920x1080")
    options.add_argument(
        "--user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'"
    )
    driver = webdriver.Chrome("chromedriver", options=options)
    setup_driver(driver)
    return driver
