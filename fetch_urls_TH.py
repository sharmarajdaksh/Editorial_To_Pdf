import subprocess
import os
import datetime
import requests
from bs4 import BeautifulSoup
from article_to_pdf import save_article_as_pdf

url = "https://www.thehindu.com/todays-paper/tp-opinion/"
date = str(datetime.datetime.now().date())
basepath = 'D:\\Work\\UPSC\\Editorials\\TheHindu\\' + date


def fetch_urls_and_save_TH():

    global url
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    a_elements = soup.find_all("ul", class_="archive-list")[0].find_all('a')

    if not os.path.exists(basepath):
        os.makedirs(basepath)

    for link in a_elements:
        save_article_as_pdf(link.get('href'), basepath + '\\' + '-'.join(link.text.split()))

if __name__ == "__main__":
    fetch_urls_and_save_TH()
