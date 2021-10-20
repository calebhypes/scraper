import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# setup environment variable access
load_dotenv()

s = requests.Session()


def get_categories():
    print('📬 Sending Category request')
    result = s.get(os.getenv('BASE_URL'))

    print('📫 Response Status:')
    if result.status_code == 200:
        print('📨 Result Received - ' + str(result.status_code))
    else:
        print('📭 Could not retrieve data')
        pass

    content = result.content

    soup = BeautifulSoup(content, features='lxml')
    links = soup.find_all("a", "leftbar_catLink")
    cat_links = [{"title": link.get_text(), "url": link.get("href")}
                 for link in links]
    return cat_links


def get_subcategories(categories):
    count = 1
    sub_links = []
    for category in categories:
        print('🔗 Sending Sub Category Request # ' + str(count))
        count += 1
        cat_url = category["url"].lstrip("/")
        result = s.get(os.getenv('BASE_URL') + cat_url)

        print('📫 Response Status:')
        if result.status_code == 200:
            print('📨 Result Received - ' + str(result.status_code))
        else:
            print('📭 Could not retrieve data')
            pass

        content = result.content

        soup = BeautifulSoup(content, features='lxml')
        links = soup.find_all("a", "subCatLink")
        category_subs = [link.get("href") for link in links]
        sub_links.extend(category_subs)
    return sub_links

# TODO: Setup product pages function
    # iterate through sub_categories
    # find and return total pages per sub_category

# TODO: Setup Generate links function
    # get total pages per sub category from pages function
    # if pages == 1
    # find total products on page
    # if pages > 1
    # iterate through total pages
    # if current page is not the last page
    # max products displayed on page is 50
    # get links for all products on page
    # if current page is the last page
    # get total number of products
    # get links for each product
    # return product links
    # generate full valid product URL list and return