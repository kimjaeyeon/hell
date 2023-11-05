import requests
from bs4 import BeautifulSoup

# 사이트에 포함된 모든 데이터를 긁어온다.
데이터 = requests.get('https://finance.naver.com/');

# print(데이터.content);


soup = BeautifulSoup(데이터.content,'html.parser');

print(soup.find_all());