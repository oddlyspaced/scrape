import requests
from bs4 import BeautifulSoup

def load_items(page_number):
    URL = "https://www.amazon.in/s?k=oneplus+buds&page="+str(page_number)
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
    item_ratings = []
    item_rating_endorsers = []

    div_elements = soup.find_all("div", {"class": "s-main-slot s-result-list s-search-results sg-row"})

    if (len(div_elements) == 0):
        return False
    search = div_elements[0].find_all("div", {"class" : "sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"})

    for elem in search :
        name = elem.find_all("span", {"class" : "a-size-medium a-color-base a-text-normal"})
        price = elem.find_all("span", {"class" : "a-price-whole"})
        rating = elem.find_all("span", {"class" : "a-icon-alt"})
        rating_endorsers = elem.find_all("span", {"class" : "a-size-base"})
        try :
            n = name[0].text
            p = price[0].text
            r = rating[0].text
            re = rating_endorsers[0].text
            item_names.append(n)
            item_prices.append(p)
            item_ratings.append(r)
            item_rating_endorsers.append(re)
        except:
            continue

    for i in range(0,len(item_names)):
        print(item_names[i], item_prices[i], item_ratings[i], item_rating_endorsers[i])
        print()
    return True

page = 1
while True:
    input("Press enter to load next page")
    if load_items(page):
        page += 1