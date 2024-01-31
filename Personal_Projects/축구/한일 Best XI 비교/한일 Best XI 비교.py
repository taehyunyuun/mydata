import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 데이터 로드
df_kor = pd.read_excel('대한민국 일본 시장가치.xlsx', sheet_name='korea', header=6)
df_kor = df_kor.iloc[0:11, 4:12]

df_jp = pd.read_excel('대한민국 일본 시장가치.xlsx', sheet_name='japan', header=6)
df_jp = df_jp.iloc[0:11, 4:12]

# 데이터 전처리 및 통계 계산
europe_kor = 0
domestic_kor = 0
etc_kor = 0

europe_jp = 0
domestic_jp = 0
etc_jp = 0

for i in range(len(df_kor)):
    if df_kor['소속 리그'][i] == 'K리그 1':
        domestic_kor += 1
    elif df_kor['소속 리그'][i] == 'J1':
        etc_kor += 1
    else:
        europe_kor += 1

for i in range(len(df_jp)):
    if df_jp['소속 리그'][i] == 'J1':
        domestic_jp += 1
    elif df_jp['소속 리그'][i] == 'K리그 1':
        etc_jp += 1
    else:
        europe_jp += 1

# 라벨과 데이터 리스트 생성
label_kor = ['국내파', '유럽파', '기타 해외파']
label_jp = label_kor.copy()

total_kor = [domestic_kor, europe_kor, etc_kor]
total_jp = [domestic_jp, europe_jp, etc_jp]

# 0이 아닌 값들만 필터링
label_kor = [label for label, total in zip(label_kor, total_kor) if total > 0]
total_kor = [total for total in total_kor if total > 0]

label_jp = [label for label, total in zip(label_jp, total_jp) if total > 0]
total_jp = [total for total in total_jp if total > 0]

# 폰트 설정
font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 원형 그래프 그리기
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].pie(total_kor, labels=label_kor, autopct='%1.1f%%', startangle=90)
ax[0].set_title('대한민국')

ax[1].pie(total_jp, labels=label_jp, autopct='%1.1f%%', startangle=90)
ax[1].set_title('일본')

plt.show()

# 시장가치 비교
total_mean_kor = int(df_kor['시장 가치 (유로)'].mean())
print('대한민국 평균 :', '{:,}'.format(total_mean_kor), '유로')

total_mean_jp = int(df_jp['시장 가치 (유로)'].mean())
print('일본 평균 :', '{:,}'.format(total_mean_jp), '유로')

europe_mean_kor = df_kor[(df_kor['소속 리그'] != 'K리그 1') & (df_kor['소속 리그'] != 'J1')]
print('대한민국 유럽파 평균 :', "{:,}".format(int(europe_mean_kor['시장 가치 (유로)'].mean())), '유로')

europe_mean_jp = df_jp[(df_jp['소속 리그'] != 'J1') & (df_jp['소속 리그'] != 'K리그 1')]
print('일본 유럽파 평균 :', "{:,}".format(int(europe_mean_jp['시장 가치 (유로)'].mean())), '유로')

print('-' * 30)

# 포지션 비교
attacker_kor = df_kor[df_kor['포지션'] == '공격수'].copy()
attacker_kor.loc[:, '골'] = [12, 11, 9]
attacker_kor.loc[:, '어시스트'] = [5, 3, 2]

attacker_jp = df_jp[df_jp['포지션'] == '공격수'].copy()
attacker_jp.loc[:, '골'] = [2, 3, 3]
attacker_jp.loc[:, '어시스트'] = [4, 6, 4]

# 각 팀별 골+어시스트 수 계산
attacker_kor['골+어시스트'] = attacker_kor['골'] + attacker_kor['어시스트']
attacker_jp['골+어시스트'] = attacker_jp['골'] + attacker_jp['어시스트']

# 막대그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))

bar_width = 0.35
bar_positions = [1, 2]  # 두 팀에 대한 막대의 위치
team_labels = ['대한민국', '일본']  # 각 팀에 대한 라벨

# 각 팀의 골과 어시스트 수를 서로 다른 색상으로 겹쳐서 표시
ax.bar(bar_positions, [attacker_kor['골'].sum(), attacker_jp['골'].sum()], width=bar_width, label='골', color='blue')
ax.bar(bar_positions, [attacker_kor['어시스트'].sum(), attacker_jp['어시스트'].sum()], width=bar_width, label='어시스트', color='orange', bottom=[attacker_kor['골'].sum(), attacker_jp['골'].sum()])

ax.set_xticks(bar_positions)
ax.set_xticklabels(team_labels)

ax.set_ylabel('공격포인트 합계')
ax.set_title('23/24시즌 국가별 공격포인트 비교')
ax.legend()

plt.show()
