import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 폰트 설정
font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 경고 메시지 숨기기
warnings.filterwarnings('ignore', category=FutureWarning)

# requests.get()를 사용하여 웹 페이지 정보 요청
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

url = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"

r = requests.get(url, headers=headers)
r.status_code

# BeautifulSoup()를 사용해 웹 페이지 분석 준비
soup = BeautifulSoup(r.content, 'html.parser')
# r.content 대신 r.text도 사용 가능

# 7개 정보를 담을 빈 리스트 만들기: 번호, 이름, 포지션, 나이, 국적, 소속 팀, 시장 가치
number = []
name = []
position = []
age = []
nation = []
team = []
value = []

for i in range(1,3):
    url = f'https://www.transfermarkt.com/marktwertetop/wertvollstespieler?page={i}'
    r = requests.get(url,headers = headers)
    soup = BeautifulSoup(r.content,'html.parser')
    player_info = soup.find_all('tr',{'class':['odd','even']})

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

# 'xlsxwriter' 엔진을 사용하여 'utf-8'로 인코딩하여 저장
with pd.ExcelWriter('C:/Users/yth21/Desktop/TH/data/Football/datas/transfermarkt/transfermarkt25.xlsx', engine='xlsxwriter', options={'encoding': 'utf-8'}) as writer:
    df.to_excel(writer, index=False)

df = pd.read_excel('C:/Users/yth21/Desktop/TH/data/Football/datas/transfermarkt/transfermarkt25.xlsx')

nationality_counts = df['국적'].value_counts()
position_counts = df['포지션'].value_counts()
age_counts = df['나이'].value_counts()
team_counts = df['소속 팀'].value_counts()

# 국적별 선수 수가 3% 이하인 국가들을 '기타'로 합치기 전에 출력
once = False

total_players = len(df)
print("국적별 선수 수\n")
for nation, count in nationality_counts.items():
    percentage = count / total_players * 100
    
    if percentage < 4 and not once:
        print('\n기타 국가')
        once = True
    
    print(f'{nation}: {count} 명, {percentage:.1f}%')

# 국적별 선수 수가 3% 이하인 국가들을 '기타'로 합치기
percentage_threshold = 3.0
nationality_counts['기타'] = nationality_counts[nationality_counts / total_players * 100 < percentage_threshold].sum()
nationality_counts = nationality_counts[nationality_counts / total_players * 100 >= percentage_threshold]

# 그래프 색상 설정
colors = [plt.cm.Paired(i) for i in range(len(nationality_counts))]

# 국적별 선수 수 시각화
plt.figure(figsize=(8, 8))
plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('국적별 선수 수', fontsize = 20)
plt.axis('equal')  # 원형 그래프를 원형으로 유지
plt.tight_layout()
plt.show()
