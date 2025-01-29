from sys import api_version

import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY="MW6IIQTOI2IGQIAM"
NEWS_API_Key="c6e7a99f72694b52b0f7d447c8d85556"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}
news_params ={
    "from":"2024-11-08",
    "q":"tesla",
    "sortBy":"publishedAt",
    "apiKey":NEWS_API_Key
}

# response = requests.get(STOCK_ENDPOINT,params=stock_params)
# data = response.json()['Time Series (Daily)']
# data_list = [value for (key,value) in data.items()]
#
# difference= abs(float(data_list[3]['4. close'])-float(data_list[2]['4. close']))
# print(difference)
# yesterday_5_percent = float(data_list[2]['4. close'])/20

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
data=news_response.json()['articles'][:3]
print(data)





## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""




