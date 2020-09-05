import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
#url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="
       #https://finance.naver.com/sise/sise_market_sum.nhn?&page=1
url = "https://finance.naver.com/item/sise_day.nhn?code=005930&page="


filename = "삼성전자_일별_주가.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "날짜	종가	전일비	시가	고가	저가	거래량".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1, 609):
    res = requests.get(url + str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    #print(soup)

    #data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    data_rows = soup.find("table", attrs={"class":"type2"}).find("tbody")
    # print(soup.find("table", attrs={"class":"type2"}))
    # print(data_rows)
    #data_rows = soup.find("table", attrs={"class":"type2"}).find("tbody").find_all("tr")
    data_rows = soup.find("table", attrs={"class":"type2"}).find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)
