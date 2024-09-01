from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()

try:
    # Navigate to Spinny.com
    driver.get("https://www.spinny.com/")

    # Click on the city section
    city_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='styles__desktopHeaderCitySection styles__forGTM styles__homePageHeaderCitySection']"))
    )
    city_section.click()

    # Click on the Ripple container
    ripple_container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='Ripple__container']"))
    )
    ripple_container.click()

    # Click on the desktop nav item
    nav_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='styles__desktopNavItem']"))
    )
    nav_item.click()

    # Click on "Spinny Budget"
    spinny_budget = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Spinny Budget']"))
    )
    spinny_budget.click()

    # Click on "2018 & above"
    year_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='2018 & above']"))
    )
    year_filter.click()

    # Click on "10,000 kms or less"
    mileage_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='10,000 kms or less']"))
    )
    mileage_filter.click()

    # Extract data
    urls = []
    model = []
    prod_click = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[@class='styles__carDetailSection']"))
    )
    for a in prod_click:
        urls.append(a.get_attribute('href'))

    for url in urls:
        driver.get(url)
        try:
            model_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div/h1"))
            )
            model.append(model_element.text)
        except (NoSuchElementException, TimeoutException):
            model.append('-')

    print(model)

finally:
    # Close the browser window
    driver.quit()
