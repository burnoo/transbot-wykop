import time
import re
import pyperclip
from selenium.webdriver.common.keys import Keys


def strip_text(text):
    text = text[:text.rindex(' ', 0, 5000)]
    re_pattern = re.compile(u"[^\u0000-\uD7FF\uE000-\uFFFF]", re.UNICODE)
    return re_pattern.sub(u"\uFFFD", text)


def get_translation(driver, text, sleep_seconds=10):
    driver.get("https://www.deepl.com/pl/translator")
    textarea_source = driver.find_element_by_class_name("lmt__source_textarea")
    textarea_translation = driver.find_element_by_class_name("lmt__target_textarea")

    text = strip_text(text)
    
    pyperclip.copy(text)

    textarea_source.clear()
    textarea_source.send_keys(Keys.SHIFT, Keys.INSERT)
    
    time.sleep(sleep_seconds)
    lang = textarea_source.get_attribute("lang")

    return None if lang == "pl" else textarea_translation.get_attribute("value")

