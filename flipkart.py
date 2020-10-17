import requests
from bs4 import BeautifulSoup

def load_items(page_number):
    URL = "https://www.flipkart.com/search?q=oneplus&page=2"
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.text, 'lxml')

    search_element_main = soup.find_all("div", {"class": "_3O0U0u"})
    search_elements = search_element_main[0].find_all("div", {"class" : "_3liAhj"})

    item_names = []
    item_variant = []
    item_price = []
    item_rating = []
    item_rating_endorsers = []

    for elem in search_elements:
        name = elem.find_all("a", {"class" : "_2cLu-l"})
        price = elem.find_all("div", {"class", "_1vC4OE"})
        variant = elem.find_all("div", {"class" : "_1rcHFq"})
        rating = elem.find_all("div", {"class" : "hGSR34"})
        endorser = elem.find_all("span", {"class": "_38sUEc"})

        try :
            n = name[0].text
            p = price[0].text
            v = variant[0].text
            r = rating[0].text
            re = endorser[0].text
            item_names.append(n)
            item_variant.append(v)
            item_price.append(p)
            item_rating.append(r)
            item_rating_endorsers.append(re)
        except:
            continue
    
    for i in range(0,len(item_names)) :
        print(item_names[i], item_variant[i], item_price[i], item_rating[i], item_rating_endorsers[i])
        print()
    return True

def load_items_new(page_number):
    URL = "https://www.flipkart.com/search?q=oneplus&page=" + str(page_number)
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.text, 'lxml')

    search_element_main = soup.find_all("div", {"class": "_1HmYoV _35HD7C"})
    search_elements = search_element_main[1].find_all("div", {"class" : "bhgxx2 col-12-12"})

    print(len(search_element_main))
    print(len(search_elements))

    item_names = []
    item_variant = []
    item_price = []
    item_rating = []
    item_rating_endorsers = []

    for elem in search_elements:
        name = elem.find_all("div", {"class" : "_3wU53n"})
        price = elem.find_all("div", {"class", "_1vC4OE _2rQ-NK"})
        rating = elem.find_all("div", {"class" : "hGSR34"})
        endorser = elem.find_all("span", {"class": "_38sUEc"})

        try :
            n = name[0].text
            p = price[0].text
            v = ""
            r = rating[0].text
            re = endorser[0].text
            item_names.append(n)
            item_variant.append(v)
            item_price.append(p)
            item_rating.append(r)
            item_rating_endorsers.append(re)
        except:
           continue
    
    for i in range(0,len(item_names)) :
        print(item_names[i], item_variant[i], item_price[i], item_rating[i], item_rating_endorsers[i])
        print()
    return True


page = 1
while True:
    input("Press enter to load next page")
    if load_items_new(page):
        page += 1