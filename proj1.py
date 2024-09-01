# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
#
# driver.get("https://www.spinny.com/")
# driver.find_element(By.XPATH, "//*[@class='styles__desktopHeaderCitySection styles__forGTM styles__homePageHeaderCitySection']").click()
# time.sleep(5)
#
# driver.find_element(By.XPATH, "//*[@class='Ripple__container']").click()
# time.sleep(5)
#
# driver.find_element(By.XPATH,"//*[@class='styles__desktopNavItem']").click()
# time.sleep(5)

# driver.find_element(By.XPATH,"//*[text()='Spinny Budget']").click()
# time.sleep(10)

# driver.find_element(By.XPATH,"//*[text()='Honda']").click()
# time.sleep(10)

# driver.find_element(By.XPATH,"//*[text()='2018 & above']").click()
# time.sleep(10)
# car_elements = driver.find_elements(By.XPATH, "//a[@class = 'styles__carDetailSection']")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Assuming you have already initialized the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get( "https://www.spinny.com/" )
driver.find_element(By.XPATH, "//*[@class='styles__desktopHeaderCitySection styles__forGTM styles__homePageHeaderCitySection']").click()
time.sleep(2)
#Hyderabad
driver.find_element(By.XPATH, "//div[@class='styles__desktopHeaderCitySelectorContentSection']/div[3]").click()
time.sleep(3)
#Buy Car
driver.find_element(By.XPATH,"//*[@class='styles__desktopNavItem']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[text()='Spinny Budget']").click()
time.sleep(5)
# driver.execute_script('window.scrollBy(0,10000)')

driver.find_element(By.XPATH,"//*[text()='2016 & above']").click()
time.sleep(5)
# driver.execute_script('window.scrollBy(0,5000)')

driver.find_element(By.XPATH,"//*[text()='1,00,000 kms or less']").click()
time.sleep(5)
urls = []

# Function to scroll down and load more elements
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust the sleep duration as needed

# Scroll down in a loop until all elements are loaded
while True:
    # Find elements based on the given XPath
    prod_click = driver.find_elements(By.XPATH, "//div[@class='styles__carDetailContainer']/a[@class='styles__carDetailSection']")

    # Extract URLs from the found elements
    for a in prod_click:
        urls.append(a.get_attribute('href'))

    # Scroll down to load more elements
    scroll_down()

    # Check if no new elements are loaded, and exit the loop if so
    new_prod_click = driver.find_elements(By.XPATH, "//div[@class='styles__carDetailContainer']/a[@class='styles__carDetailSection']")
    if len(new_prod_click) == len(prod_click):
        break
model = []
for i in urls:
    driver.get(i)
    for a in driver.find_elements( By.XPATH, "//div/h1" ):
        model.append( a.text )

# Print the total number of URLs collected
print(len(urls))
print(model,len(model))

# Close the WebDriver when done
driver.quit()

# Close the WebDriver when done
driver.quit()

# print(car_name)
# year = []
# brand = []
# model = []
# fuel_type = []
# KM_driven = []
# selling_price=[]
# cost_price = []
# for car_element in car_elements:
#     for i in car_element.find_element(By.XPATH,"//a[@class = 'styles__carDetailSection']/div/h3/p").text :
#         print(i)


