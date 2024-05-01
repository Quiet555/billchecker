import requests
import re
from bs4 import BeautifulSoup
url='https://invoice.etax.nat.gov.tw/index.html'
result=requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
result.encoding='utf-8'
number=str(soup.find_all('span',class_='font-weight-bold'))
numbers=re.findall(r'\d+',number)

specilward=numbers[0]
spward=numbers[1]
headward1=numbers[2]+numbers[3]
headward2=numbers[4]+numbers[5]
headward3=numbers[6]+numbers[7]

flag=True

while flag:
    urbill=input('您的發票號碼:')
    if urbill=='-1':
        print('結束程式')
        flag=False
        break


    if len(urbill)!=8 or urbill.isdigit() :
        print('發票格式錯誤!')
        continue

    if urbill==specilward:
        print('恭喜你獲得特別獎1000萬元!')
        continue
    elif urbill==spward:
        print('恭喜你獲得特獎200萬元!')
        continue
    elif urbill==headward1 or urbill==headward2 or urbill==headward3:
        print('恭喜你獲得頭獎20萬元!')
        continue
    elif urbill[-7:]==headward1[-7:] or urbill[-7:]==headward2[-7:] or urbill[-7:]==headward3[-7:]:
        print('恭喜你獲得二獎4萬元')
        continue
    elif urbill[-6:]==headward1[-6:] or urbill[-6:]==headward2[-6:] or urbill[-6:]==headward3[-6:]:
        print('恭喜你獲得三獎1萬元')
        continue
    elif urbill[-5:]==headward1[-5:] or urbill[-5:]==headward2[-5:] or urbill[-5:]==headward3[-5:]:
        print('恭喜你獲得四獎4000元')
        continue
    elif urbill[-4:]==headward1[-4:] or urbill[-4:]==headward2[-4:] or urbill[-4:]==headward3[-4:]:
        print('恭喜你獲得五獎1000元')
        continue
    elif urbill[-3:]==headward1[-3:] or urbill[-3:]==headward2[-3:] or urbill[-3:]==headward3[-3:]:
        print('恭喜你獲得六獎200元')
        continue
    else:
      print('可惜沒中!')
      continue
