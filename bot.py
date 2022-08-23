from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys, os
from time import sleep

def main():
    # Set up Facebook login account name and password
    account = "{CHANGE-ME}"
    password = "{CHANGE-ME}"

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/{CHANGE-ME}", "https://www.facebook.com/groups/{CHANGE-ME}"
    ]

    # Set up text content to post
    message = "THIS IS AN AUTOMATED TEST"

    # Set up paths of images to post
    images_list = ['/Users/PATH/TO/IMAGE.png','/Users/PATH/TO/IMAGE.jpeg']

    # Login Facebook
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com')
    emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
    emailelement.send_keys(account)
    passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
    passelement.send_keys(password)
    loginelement = driver.find_element(By.NAME, "login")
    loginelement.click()

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH,'//span[normalize-space()="Write something..."]').click()
            time.sleep(2)
            post_box = driver.switch_to.active_element
            post_box.send_keys(message)
            time.sleep(2)

        # Catch any errors    
        except:
            print("Something went wrong, exiting script to avoid conflicts"))

        # --------WORKING BUT WON'T INTERACT--------- 
        time.sleep(5)
        for photo in images_list:
            print(os.path.abspath(photo))
            driver.find_element(By.XPATH,'//html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]')
            time.sleep(2)
            photo_element = driver.switch_to.active_element
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(os.path.sep, ROOT_DIR,'images'+ os.sep)
            print(image_path)
            photo_element.send_keys(image_path)
            time.sleep(1)
        time.sleep(6)

        # Click post button 
        post_button = driver.find_element(By.XPATH,"//div[@aria-label='Post']")
        clickable = False
        while not clickable:
            cursor = post_button.find_element(By.TAG_NAME, "span").value_of_css_property("cursor")
            if cursor == "pointer":
                clickable = True
            break
        post_button.click()
        time.sleep(5)
    print('Post published successfully!')    
    # Close driver
    driver.close()

if __name__ == '__main__':
  main()
