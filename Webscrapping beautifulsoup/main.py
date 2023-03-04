from bs4 import BeautifulSoup
import requests


def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})

        title_value = title.string

        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


def get_price(soup):
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()

    except AttributeError:

        try:
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price


def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating


def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count


def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available


if __name__ == '__main__':

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                    'Safari/537.36',
                'Accept-Language': 'en-US'})

    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"

    webpage = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(webpage.content, "lxml")

    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})

    links_list = []

    for link in links:
        links_list.append(link.get('href'))

    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "lxml")

        print("Product Title =", get_title(new_soup))
        print("Product Rating =", get_rating(new_soup))
        print("Number of Product Reviews =", get_review_count(new_soup))
        print("Availability =", get_availability(new_soup))
        print()
        print()
