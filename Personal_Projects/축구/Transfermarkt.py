import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import warnings

# 경고 메시지 숨기기
warnings.filterwarnings('ignore', category=FutureWarning)

# requests.get()으로 웹 페이지 정보 요청
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

url = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"

r = requests.get(url, headers=headers)
r.status_code

# r.content 대신 r.text도 사용 가능
soup = BeautifulSoup(r.content, 'html.parser')

# 선수 정보가 담긴 태그와 클래스 찾기
player_info = soup.find_all('tr', {'class': ['odd', 'even']})

# 7개 정보를 담을 빈 리스트 만들기: 번호, 이름, 포지션, 나이, 국적, 소속 팀, 시장 가치
number = []
name = []
position = []
age = []
nation = []
team = []
value = []

# player_info에서 'td' 태그만 모두 찾기
for info in player_info:
    player = info.find_all('td')
    # 해당 정보를 찾아서 각 리스트에 .append()로 추가
    number.append(player[0].text)
    name.append(player[3].text)
    position.append(player[4].text)
    age.append(player[5].text)
    nation.append(player[6].img['alt'])
    team.append(player[7].img['alt'])
    value.append(player[8].text.strip())

df = pd.DataFrame(
    {'번호': number,
     '이름': name,
     '포지션': position,
     '나이': age,
     '국적': nation,
     '소속 팀': team,
     '시장 가치': value}
)

# 'xlsxwriter' 엔진으로 'utf-8'로 인코딩해 저장
with pd.ExcelWriter('C:/Users/yth21/Desktop/TH/data/Football/datas/transfermarkt/transfermarkt25.xlsx', engine='xlsxwriter', options={'encoding': 'utf-8'}) as writer:
    df.to_excel(writer, index=False)
  
