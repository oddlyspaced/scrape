import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/s?k=oneplus+buds"
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.text, 'lxml')

# Amazon search results have 2 things in common
# data-asin (usually some code)
# data-cel-widget (normally as search_result_23 etc)

item_names = []
item_prices = []

div_elements = soup.find_all("div", {"class": "s-main-slot s-result-list s-search-results sg-row"})
print(len(div_elements))

if (len(div_elements) == 0):
    exit()

search = div_elements[0].find_all("div", {"class" : "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"})
print(len(search))

for elem in search :
    name = elem.find_all("span", {"class" : "a-size-medium a-color-base a-text-normal"})
    price = elem.find_all("span", {"class" : "a-price-whole"})
    item_names.append(name[0].text)    
    item_prices.append(price[0].text)

print(item_names)
print(item_prices)