from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_frontend_sentiment():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://16.16.226.86:5000")

        driver.find_element(
            By.ID,
            "text-input"
        ).send_keys("This is a wonderful product")

        driver.find_element(
            By.ID,
            "submit-btn"
        ).click()

        time.sleep(3)

        result = driver.find_element(
            By.ID,
            "result-output"
        ).text

        assert result != ""

        assert (
            "POSITIVE" in result or
            "NEGATIVE" in result or
            "Confidence" in result
        )

    finally:
        driver.quit()