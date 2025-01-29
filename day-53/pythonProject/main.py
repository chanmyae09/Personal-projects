import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import actions
from selenium.webdriver.common import keys
import time
GOOGLE_FORM_LINK="https://forms.gle/v4NYo8xaWr8sD5aR6"
URL="https://appbrewery.github.io/Zillow-Clone/"

response=requests.get(URL,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                                   "Accept-Language":"en-US,en;q=0.9"})

data=response.text
soup = BeautifulSoup(data,'html.parser')
# Create a list of all the links on the page using a CSS Selector
all_links = soup.select(".StyledPropertyCardDataWrapper a")
print(f"There are {len(all_links)} links to the individual elements in this website\n")
link_list=[link['href']for link in all_links]
prices = soup.select(".PropertyCardWrapper span")
price_list=[price.text.split('+')[0].split('/mo')[0] for price in prices]
addresses=soup.select(".StyledPropertyCardDataWrapper address")
address_list=[address.text.strip() for address in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver=webdriver.Chrome(chrome_options)
driver.get(GOOGLE_FORM_LINK)


for n in range(len(all_links)):
    # TODO: Add fill in the link to your own Google From
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(5)
    addy = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addy.send_keys(address_list[n])
    price = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(price_list[n])
    link = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(link_list[n])
    submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()