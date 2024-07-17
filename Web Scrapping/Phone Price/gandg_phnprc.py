import requests
from bs4 import BeautifulSoup
import pandas as pd


r = requests.get('https://gadgetandgear.com/category/phone')


# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

base_class = soup.find('div', class_="ProductList_productRow__Q4VMB")
# base_class = soup.find_all('p', class_="ProductCard_CardPriceTag__SRo_X ProductCard_cardPriceTag__3nqTU")


# product_row = base_class.find_all('div', class_="ProductList_productRow__Q4VMB")
# product_card = product_row.find('div', class_="ProductCard_ProductCard___Lbvt ProductCard_sm__BA3zF")
# product_card2 = product_card.find('div', class_="ProductCard_cardBody__8nPmw")
model = base_class.find_all('h4').text

print(model)
# print(product_card)
# print(soup)