#import the necassary modules
from selenium import webdriver
from selenium.webdriver.common.by import By


#open Chrome web browser and maximize the window
driver = webdriver.Chrome()
driver.maximize_window()


#navigate the website
driver.get("https://www.canadianctb.ca/")


#check if title and url are correct
if driver.title == "CCTB | Canadian College of Technology and Business":
    print("Page title is correct.")
else:
    print("Page title is incorrect.")

if driver.current_url == "https://www.canadianctb.ca/":
    print("Page URL is correct.")
else:
    print("Page URL is incorrect.")


# Click on the Virtual Student Lounge link
lounge_link = driver.find_element(By.LINK_TEXT, 'Virtual Student Lounge')
lounge_link.click()


#check if title and url are correct
if driver.title == "Virtual Student Lounge | CCTB":
    print("Page title is correct.")
else:
    print("Page title is incorrect.")
    
if driver.current_url == "https://www.canadianctb.ca/virtual-student-lounge":
    print("Page URL is correct.")
else:
    print("Page URL is incorrect.")


input()
driver.close()
