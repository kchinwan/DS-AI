# packages need

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# fuction to extract Prodyct Tittle
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})

        title_value = title.text

        title_string = title_value.strip()
    except:
        title_string = ""

    return title_string

#Function to extrct Product Price
def get_price(soup):
    try:
#    price = soup.find("span", attrs={"class":'a-price-whole'}).find("span",attrs={"class":'a-offscreen'}).string.strip()
        price = soup.find("span", attrs={"class": 'a-offscreen'})
        price_value = price.string.strip()
    

    except AttributeError:
        try:
            price_value = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except :
            price_value = ""

    return price_value


# function to extract Product rating
def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
        
    except AttributeError :
        try:
            rating = soup.find("span", attrs={"class":'a-icon-alt'}).string.strip()
        except:
            rating =""
    return rating


if __name__ == '__main__' :
    URL = "https://www.amazon.in/s?k=LAPTOP&rh=n%3A1375424031&ref=nb_sb_noss"
#header for requests
    HEADERS = ({'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})
 
 #HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

#   print(type(webpage.content))

#SOUP Objct contaning all data
    soup = BeautifulSoup(webpage.content, "html.parser")

#Fetch links as List of Tag Object
#   links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    links_list = []
    for link in links:
        links_list.append(link.get('href'))
    d = {"title":[], "price":[], "ratings":[]}
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.in/"  +link, headers = HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['ratings'].append(get_rating(new_soup))


    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('',np.nan, inplace=True)
    amazon_df.to_csv("amazon_data.csv",header=True,index=False)
