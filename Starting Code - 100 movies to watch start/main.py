import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
movies_webpage = response.text
soup= BeautifulSoup(movies_webpage,'html.parser')
movies = soup.find_all(name="h3",class_="title")
movies_list = []
for movie in reversed(movies):
    movie_text = movie.getText()
    movies_list.append(movie_text)

with open('file.txt', 'a') as file:
    file.writelines(movie + "\n" for movie in movies_list )


