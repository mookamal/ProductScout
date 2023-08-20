from bs4 import BeautifulSoup
import requests
from termcolor import colored, cprint
# from ebay
def ebay(word):
    store_name = "ebay"
    URL = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2540003.m570.l1313&_nkw={word}&_sacat=0"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # ul all data
    get_li = soup.find_all("li" , class_="s-item")
    list_data = []
    count = 0
    for i in get_li:
        data = {}
        title = i.find("div" , class_="s-item__title").text
        data['title'] = title
        price = i.find("div" , class_="s-item__detail").text
        data['price'] = price
        link = i.find("a" , class_="s-item__link").get("href")
        data['link'] = link
        data['store_name'] = store_name
        list_data.append(data)
        count = count + 1
        if count == 5:
            break
    return list_data

# from etsy
def etsy(word):
    store_name = "etsy"
    URL = f"https://www.etsy.com/search?q={word}&ref=search_bar"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    get_list = soup.find("ol" , class_="tab-reorder-container")
    get_list_links = get_list.find_all("a" , class_="listing-link")
    list_data = []
    count = 0
    for i in get_list_links:
        data = {}
        title = i.find("h3").text.strip()
        data['title'] = title
        price = i.find("span", class_="currency-value").text.strip()
        data['price'] = price
        link = i.get("href")
        data['link'] = link
        data['store_name'] = store_name
        list_data.append(data)
        count = count + 1
        if count == 5:
            break
        





def show(data):
    for i in data:
        title = i['title']
        price = i['price']
        link = i['link']
        store_name = i['store_name']
        format_data = f"""
        ___ Store Name : {store_name} ___
        Title : {title}
        _____________________________________
        Price : {price}
        _____________________________________
        Link : {link}
        """
        text = colored(format_data, "red", attrs=["reverse","bold" , "blink"])
        print(text)
        