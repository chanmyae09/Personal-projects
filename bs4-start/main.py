from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
yc_web_page= response.text
soup= BeautifulSoup(yc_web_page,'html.parser')
articles= soup.find_all(name="span",class_="titleline")
article_texts = []
article_links = []

for article_tags in articles:
    a_tag = article_tags.find('a')
    article_text = a_tag.getText()
    article_texts.append(article_text)
    article_link= a_tag.get("href")
    article_links.append(article_link)

article_upvotes =[int(score.getText().split(" ")[0]) for score in  soup.find_all(name="span",class_="score")]
# print(article_texts)
# print(article_links)
print(article_upvotes)
max_index = article_upvotes.index(max(article_upvotes))
text = article_texts[max_index]
link = article_links[max_index]












