import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
r = requests.get('https://asianc.sh/')


# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('ul', class_='switch-block list-episode-item')
movie_title = s.find_all('h3')
sub_type = s.find_all('span', class_=["type RAW", "type SUB"])
realise_time = s.find_all('span', class_="time")

# for i in content:
#     print(i.text)

data = []
fields = ["No", "Title", "Subtitle", "Realise Time"]

for i in range(len(movie_title)):
    dic = {
        "No": i+1,
        "Title": movie_title[i].text,
        "Subtitle": sub_type[i].text,
        "Realise Time": realise_time[i].text
    }

    data.append(dic)

filename = "daramacool_movies.csv"

with open(filename, 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames= fields)

    writer.writeheader()
    writer.writerows(data)


    