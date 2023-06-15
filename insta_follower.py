from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower:
    """
    To automate the process of following someone else followers on instagram.

    Methods:
    login: This method help to login into your instagram account
    find_followers: To reach someone else instagram profile and scroll down the complete list of followers.
    follow: To follow all the followers present in the follower list.
    """
    def __init__(self) -> None:
        # drive_path
        self.drive_path = 'YOUR DRIVE PATH'

        # for holding the website
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('detach',True)

        # opening the website
        self.drive = webdriver.Chrome(options=self.option,service=Service(self.drive_path))
        self.drive.get('https://www.instagram.com/')

        # waiting time
        self.short_time = ui.WebDriverWait(self.drive,20)
        self.long_time = ui.WebDriverWait(self.drive,60)

    def login(self,user_name,password):
        # username input to login
        self.long_time.until(EC.presence_of_all_elements_located((By.XPATH,'//input[@name="username"]')))
        user_name_input = self.drive.find_element(By.XPATH,'//input[@name="username"]')
        user_name_input.send_keys(user_name)

        # password input to login
        self.short_time.until(EC.presence_of_all_elements_located((By.XPATH,'//input[@name="password"]')))
        password_input = self.drive.find_element(By.XPATH,'//input[@name="password"]')
        password_input.send_keys(password)
        
        # login button to login the account
        self.short_time.until(EC.presence_of_all_elements_located((By.XPATH,'//button[@type="submit"]')))
        login_button = self.drive.find_element(By.XPATH,'//button[@type="submit"]')
        login_button.click()

        # stop the svaing of account details
        self.long_time.until(EC.presence_of_all_elements_located((By.XPATH,'//div[text()="Not Now"]')))
        not_saving_detail_button = self.drive.find_element(By.XPATH,'//div[text()="Not Now"]')
        not_saving_detail_button.click()

        # turn of notifcations
        self.short_time.until(EC.presence_of_all_elements_located((By.XPATH,"//button[text()='Not Now']")))
        no_notification_button = self.drive.find_element(By.XPATH,"//button[text()='Not Now']")
        no_notification_button.click()

    def find_followers(self):
        #Go to the page of person with the followers
        self.drive.get(f"ANY INSTAGRAM ACCOUNT PROFILE LINK")

        # show the followers list
        self.long_time.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@role='link' and text()=' followers']")))
        followers_check = self.drive.find_element(By.XPATH,"//a[@role='link' and text()=' followers']")
        followers_check.click()

        # follow all the followers in the follower list
        self.short_time.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'_aano')))
        for i in range(10):
            time.sleep(7)
            modal = self.drive.find_element(By.CLASS_NAME,'_aano')
            self.drive.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)         



    def follow(self):
        # follow the followers
        all_buttons = self.drive.find_elements(By.CSS_SELECTOR,'._aano button')
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                self.short_time.until(EC.presence_of_all_elements_located((By.XPATH,"//button[text()='Cancel']")))
                cancel_button = self.drive.find_element(By.XPATH,"//button[text()='Cancel']")
                cancel_button.click()
                


            
        

