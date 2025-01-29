from bs4 import BeautifulSoup
import requests
import smtplib

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

response = requests.get(live_url)

soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML element that contains the price
print(soup)
price = soup.find(name = "span",class_="aok-offscreen")
# name = soup.find(name = "span",
#                  class_="a-size-large product-title-word-break",
#                  id= "productTitle").getText().split("    ")[0].strip()
# print(name)
#
# # Remove the dollar sign using split
print(price)
# price_without_currency = price.split("$")[1]
#
#
# price_as_float = float(price_without_currency)
# print(price_as_float)

my_email = "pythont292@gmail.com"
password= "weteyrklfefckyqk"

# if price_as_float> 100:
#     with  smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email , password =password )
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="pythont292@yahoo.com",
#             msg = f"{name} is ${price_as_float}. {practice_url}")




