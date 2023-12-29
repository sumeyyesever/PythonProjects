from bs4 import BeautifulSoup
import requests

web_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(web_url)
web_page_html = response.text
soup = BeautifulSoup(web_page_html, "html.parser")

film_lines = soup.find_all(name="h3", class_="title")

for film_line in film_lines[::-1]:
    name = film_line.getText()
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{name} \n")







