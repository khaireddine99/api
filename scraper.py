from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def scrape():
    raw = urlopen("https://www.tunisianet.com.tn/301-pc-portable-tunisie")
    html = BeautifulSoup(raw, features="lxml")

    articles = html.find_all("div", {"class": "thumbnail-container text-xs-center"})

    article_list = []  # Initialize an empty list

    for article in articles:
        name = article.find("h2", {"class": "h3 product-title"})
        name_raw = name.find("a").text.split("/")
        article_name = name_raw[0].strip()  # Use strip() to remove extra spaces

        price_raw = article.find("div", {"class": "product-price-and-shipping"})
        article_price = price_raw.find("span").text.strip()  # Use strip() to remove extra spaces

        # Create a dictionary for each article and append it to the list
        article_dict = {"name": article_name, "price": article_price}
        article_list.append(article_dict)

    # Open a file in write mode and save the data as JSON
    with open("data.json", "w") as file:
        json.dump(article_list, file, indent=4)

    return article_list

if __name__ == '__main__':
    scrape()

    
    






