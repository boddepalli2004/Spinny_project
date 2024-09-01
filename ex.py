from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

driver = webdriver.Chrome()

# Navigate to Spinny.com
driver.get("https://www.spinny.com/")
#for location
driver.find_element(By.XPATH, "//*[@class='styles__desktopHeaderCitySection styles__forGTM styles__homePageHeaderCitySection']").click()
time.sleep(2)
#Hyderabad
driver.find_element(By.XPATH, "//div[@class='styles__desktopHeaderCitySelectorContentSection']/div[3]").click()
time.sleep(5)
#Buy Car
driver.find_element(By.XPATH,"//*[@class='styles__desktopNavItem']").click()
time.sleep(5)
#Spinny Budget
driver.find_element(By.XPATH,"//*[text()='Spinny Budget']").click()
time.sleep(10)
# driver.execute_script('window.scrollBy(0,10000)')

driver.find_element(By.XPATH,"//*[text()='2008 & above']").click()
time.sleep(5)
# driver.execute_script('window.scrollBy(0,5000)')

driver.find_element(By.XPATH,"//*[text()='1,50,000 kms or less']").click()
time.sleep(5)
# Wait for some time to let the page load
urls = []
model = []
brand = []
years = []
km_driven = []
trans = []
transmission = []
fuel_type = []
Engine_type = []
mileage = []
prices = []
sell_price = []
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
while True:
    prod_click = driver.find_elements(By.XPATH, "//div[@class='styles__carDetailContainer']/a[@class='styles__carDetailSection']")

    for a in prod_click:
        urls.append(a.get_attribute('href'))

    scroll_down()
    new_prod_click = driver.find_elements(By.XPATH, "//div[@class='styles__carDetailContainer']/a[@class='styles__carDetailSection']")
    if len(new_prod_click) == len(prod_click):
        break
print(len(urls))
for i in urls:
    driver.get(i)
    booked_found = False
    booked = 0
    for i in driver.find_elements( By.XPATH, "//div[@class='styles__floatingBadge styles__bookedBadge']/span" ):
        try:
            if i.text == 'BOOKED':
                # If 'BOOKED' is found, break out of the loop
                booked += 1
                booked_found = True
                break
        except NoSuchElementException:
            # Handle the case where i.text is not present
            pass
    if not booked_found:
        for a in driver.find_elements( By.XPATH, "//div/h1" ):
            model.append( a.text )
        # for a in driver.find_elements( By.XPATH, "//div[@class='DesktopOverview__overviewItemList']/div[1]/div[2]" ):
        #     years.append( a.text )
        for a in driver.find_elements( By.XPATH,"//div[@class='DesktopRightSection__otherDetailSection DesktopRightSection__perceptionOtherDetails']/div/span[1]" ):
            km_driven.append( a.text )
        for a in driver.find_elements( By.XPATH,"//div[@class='DesktopRightSection__otherDetailSection DesktopRightSection__perceptionOtherDetails']/div/span[2]" ):
            fuel_type.append( a.text )
        for a in driver.find_elements( By.XPATH,"//div[@class='DesktopRightSection__otherDetailSection DesktopRightSection__perceptionOtherDetails']/div/span[3]" ):
            trans.append( a.text )
        for a in driver.find_elements( By.XPATH, "//*[text()='kmpl']" ):
            mileage.append( a.text )
        for a in driver.find_elements( By.XPATH,"//*[@class='LoanBreakupGraph__loanBreakUpValueContainer']/div[3]/div[2]" ):
            prices.append( a.text )

for string in model:
    # Split the string into words
    words = string.split()
    if len( words ) >= 2:
        years.append(2023 - int(words[0]))
        brand.append(words[1])
for string in fuel_type:
    # Split the string into words
    words = string.split()
    Engine_type.append(words[1])
for string in trans:
    # Split the string into words
    words = string.split()
    transmission.append(words[1])
for string in prices:
    sell_price.append(int(string[1:].replace(',', '')))
dic = {
    'Model':brand,
    'Year' : years,
    'Km_Driven' : km_driven,
    'Engine_Type' : Engine_type,
    'Transmission' : transmission,
    'Mileage' : mileage,
    'Price' : sell_price
}
df = pd.DataFrame(dic)
df.to_csv("spinny.csv")