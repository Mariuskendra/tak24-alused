import urllib3
from bs4 import BeautifulSoup

url = "https://editorial.rottentomatoes.com/guide/best-1994-movies/"
http = urllib3.PoolManager()
page = http.request('GET', url).data
soup = BeautifulSoup(page, "lxml")

movies = soup.findAll('div', attrs={'class': 'countdown-item'})

for movie in movies:
    index_tag = movie.find('div', attrs={'class': 'countdown-index-responsive'})
    movie_title_tag = movie.find('div', attrs={'class': "article_movie_title"})
    score_tag = movie.find('span', attrs={'class': 'tMeterScore'})

    index = index_tag.get_text(strip=True) if index_tag else "N/A"
    movie_title = movie_title_tag.find('a').get_text(strip=True) if movie_title_tag else "Unknown"
    score = score_tag.get_text(strip=True) if score_tag else "No Score"
    print(f"{index}. {movie_title} - Score {score}")