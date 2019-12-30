import requests

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

email = ""
password = ""


def crawl_blog():
    res = requests.get("https://fedoramagazine.org/",
                       headers={'User-agent': 'Mozilla/5.0'})
    res = res.text.split("<h2 class=\"post-title\"><a href=\"")
    urls = list()
    for i in range(1, len(res)):
        urls.append(res[i].split("\" title=")[0])
    return urls


def login():
    element = driver.find_element_by_class_name("js-username-field")
    element.send_keys(email)
    element = driver.find_element_by_class_name("js-password-field")
    element.send_keys(password)
    element.submit()


def send(url):
    driver.get("https://twitter.com/compose/tweet")
    time.sleep(1)
    element = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
    ActionChains(driver).move_to_element(element).send_keys(url).perform()
    element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid = 'tweetButton']")))
    element.click()


def main():
    urls = crawl_blog()
    login()
    for url in urls:
        send(url)


if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://twitter.com/login")
    main()
    driver.close()