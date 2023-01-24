import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

# self.url = url
# url = "https://kabuoji3.com/stock/6501/2019/"
url = "https://www.w-index.com/"

# URLを指定する
html = urllib.request.urlopen(url)
# URLを開く
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く
# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
tag = "color: rgb(34, 34, 34); text-shadow: rgb(255, 255, 255) 0px 0px 10px"

aaa = soup.select("b")
# news_tag = soup.select(".newsFeed_item_title") ###
# news_tag = soup.select(".newsFeed_item_date") ###
# news_tag_2 = soup.select(".newsFeed_item")
# print (news_tag)


for i in range(len(aaa)):
    print(aaa[i])


# for i in range(len(news_tag)):
#     news_tag[i] = str(news_tag[i]).replace("<div class=\"newsFeed_item_title\">", "").replace("</div>", "")
#     # news_tag[i] = str(news_tag[i]).replace("<div class=\"newsFeed_item_date\">", "").replace("</div>", "")
#     # print(news_tag[i])
#     return news_tag
