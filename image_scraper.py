import shutil
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pyautogui
import time
import BrowsersClosedExpectedCondition as browsersEC
import RedirectionExpectedCondition as redirectEC
import insert_scraped_images

def make_url_query(query):
    return query.replace(" ", "+")

print("Welcome to the Image Scraper!\nPlease enter your image query: ")
query = input()
print("How many images would you like scraped? (Click enter if you do not want to specify): ")
num_of_images = input()
if(num_of_images == ""):
    num_of_images = "100"
num_of_images = int(num_of_images)

url_query = make_url_query(query)
print(url_query)
url = "https://www.google.com/search?q="+url_query+"&source=lnms&tbm=isch"

driver = webdriver.Chrome()
driver.get(url)

images = driver.find_elements(By.XPATH, "//div[@class='islrc']//img")
image_srcs = []

for i in range(0,num_of_images):
    print(i)
    try:
        actions = ActionChains(driver)
        actions.move_to_element(images[i]).click(images[i]).perform()
        new_url = driver.current_url
        curr=driver.current_window_handle

        try:
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                response = WebDriverWait(driver, 10).until(
                    browsersEC.browsers_are_closed()
                )
            else:
                time.sleep(2)
                print("Clicking...")
                big_image = driver.find_elements(By.XPATH, "//div[@class='tvh9oe BIB1wf']//div[@class='OUZ5W']//img")
                
                src = big_image[0].get_attribute("src")
                print(src)
                image_srcs.append(src)
                driver.get(url)
                try:
                    element = WebDriverWait(driver, 10).until(
                        redirectEC.url_has_redirected(url_query)
                    )
                except:
                    driver.quit()
            div = driver.find_elements(By.CSS_SELECTOR, "div.islrc")
            images = div[0].find_elements(By.CSS_SELECTOR, "img")
        except Exception as e:
            print(e)
    except:
        print("Can't click!")

print(len(image_srcs))