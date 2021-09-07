import requests
from bs4 import BeautifulSoup
import chardet
import re
import pandas as pd
import tabula

from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

def get_tags(soup):
    for tag in soup.find_all(surrounded_by_strings):
        print(tag.name)

def get_title(soup):
    title = soup.find('title').get_text()
    return title


def get_class(soup, word):
    txt=soup.find_all(string=word)
    # <ul class="m-list"> が 無痛分娩に関する通知

    return "m-list"

def create_list(soup, cls):
    tmp_list=[]
    for ul in soup.find_all(attrs={"class": cls}):
        print(ul.find_all("span", limit=2)[1])
        # リンク一覧の生成
        for li in ul.find_all(href=re.compile("/10800000/")):
            #print(li.get_text(), "=", li.get("href"))
            tmp_list.append(li)
    return tmp_list

if __name__ == "__main__":
    BASE_URL='https://www.mhlw.go.jp'
    URL='https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000186912.html'
    word='無痛分娩に関する通知'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    title=get_title(soup)
    cls=get_class(soup, word)
    a_list=create_list(soup, cls)
    print("------------------")
    for a_tag in a_list:
        print(a_tag.get_text(), ":")
        print(BASE_URL+a_tag.get("href"))
        dfs = tabula.read_pdf(BASE_URL+a_tag.get("href"), lattice=True)

        for df in dfs:
            print(df)

    print("------------------")
