from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(
    By.CSS_SELECTOR, ' button[class="btn class3 btn-primary btn-test"]')
blue_button.click()

# РЅР°Р¶Р°С‚СЊ РЅР° РєРЅРѕРїРєСѓ "РћРє" РІСЃРїР»С‹РІР°СЋС‰РµРіРѕ РѕРєРЅР° РІ СЂСѓС‡РЅСѓСЋ
sleep(2)

blue_button = driver.find_element(
    By.CSS_SELECTOR, ' button[class="btn class3 btn-primary btn-test"]')
blue_button.click()
# РЅР°Р¶Р°С‚СЊ РЅР° РєРЅРѕРїРєСѓ "РћРє" РІСЃРїР»С‹РІР°СЋС‰РµРіРѕ РѕРєРЅР° РІ СЂСѓС‡РЅСѓСЋ
sleep(2)

blue_button = driver.find_element(
    By.CSS_SELECTOR, ' button[class="btn class3 btn-primary btn-test"]')
blue_button.click()

driver.quit()
