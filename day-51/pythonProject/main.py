from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import actions
from selenium.webdriver.common import keys
import time

PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH ="/Users/charlesaung/.cache/selenium/chromedriver"
TWITTER_EMAIL = "charles2002mdy@gmail.com"
TWITTER_PASSWORD = "T@keachill09"




class InternetSpeedTwitterBot:
    def __init__(self,):
        self.down=0
        self.up =0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")

        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go.click()

        time.sleep(10)
        button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        button.click()
        time.sleep(80)
        self.down = self.driver.find_element(By.XPATH,value = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH,value = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')



    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(8)
        input_ =self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        input_.send_keys(TWITTER_EMAIL)

        next = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]')
        next.click()

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()