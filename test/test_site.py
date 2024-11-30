from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    product_page = ProductPage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.products_count(2)

    # driver.get('https://demoblaze.com/')
    # monitor_link = driver.find_element(By.CSS_SELECTOR,'''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    # monitors = driver.find_elements(By.CSS_SELECTOR,'.card')
    # assert len(monitors) == 2