from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=options
    )
    driver.get("https://cn.bing.com")
    assert "Bing" in driver.title
    driver.quit()
