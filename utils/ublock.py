import time

modules_to_enable = [
    "adguard-annoyance",
    "adguard-social",
    "fanboy-thirdparty_social",
    "fanboy-cookiemonster",
    "fanboy-annoyance",
    "fanboy-social",
    "ublock-annoyances",
]


def setup_driver(driver):
    driver.get("chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/3p-filters.html")
    time.sleep(0.3)
    module_groups = driver.find_elements_by_class_name("geDetails")
    [driver.execute_script("arguments[0].click()", mg) for mg in module_groups]
    time.sleep(0.3)
    [
        driver.find_element_by_css_selector(
            "li[data-listkey='{}'] > input".format(module_name)
        ).click()
        for module_name in modules_to_enable
    ]
    time.sleep(0.3)
    driver.find_element_by_id("buttonApply").click()
    time.sleep(0.3)
