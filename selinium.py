from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the WebDriver executable
chrome_service = Service('C:/Users/neela/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=chrome_service)

# Open a website
driver.get('https://www.cars.com')

# Example: Get the page title
print(driver.title)

# Close the browser
driver.quit()
