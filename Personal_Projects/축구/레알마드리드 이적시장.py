import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib.ticker import FuncFormatter
import os
import re

# 폰트 설정
font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 경로
file_paths = ['C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1415.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1516.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1617.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1718.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1819.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1920.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2021.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2122.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2223.csv',
              'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2324.csv']

# 시즌 숫자를 문자열 형태로 리스트에 저장
season_nums = [re.findall(r'\d+', path)[-1] for path in file_paths]
season_lists = [pd.read_csv(file_path, header=2) for file_path in file_paths]

season_count = 0

# 시즌별로 지출과 수입을 저장할 리스트 생성
spending_totals = []
M_spending_totals = []

income_totals = []
M_income_totals = []

for df in season_lists:
    
    tot_spending = 0
    tot_income = 0
    
    spending_count = 0
    income_count = 0
    
    tot_spending = df[df['이적 형태'] == 'Arrival']['이적료(유로)'].sum()
    tot_spending = tot_spending * -1
    spending_count = len(df[df['이적 형태'] == 'Arrival']['이적료(유로)'])
    avg_spending = round(tot_spending / spending_count)
    
    tot_income = df[df['이적 형태'] == 'Departure']['이적료(유로)'].sum()
    income_count = len(df[df['이적 형태'] == 'Departure']['이적료(유로)'])
    avg_income = round(tot_income / income_count)

    FA_arrival_nums = df[(df['이적 형태'] == 'Arrival') & (df['기타'] == 'FA')].shape[0]
    Loan_arrival_nums = df[(df['이적 형태'] == 'Arrival') & (df['기타'] == 'Loan')].shape[0]
    Callup_nums = df[(df['이적 형태'] == 'Arrival') & (df['기타'] == 'Call up')].shape[0]
    
    tot_departure_nums = len(df['이적료(유로)']) - spending_count
    FA_departure_nums = df[(df['이적 형태'] == 'Departure') & (df['기타'] == 'FA')].shape[0]
    Loan_departure_nums = df[(df['이적 형태'] == 'Departure') & (df['기타'] == 'Loan')].shape[0]
    
    # 시즌별로 지출과 수입을 저장
    spending_totals.append(tot_spending)
    M_spending_totals.append(tot_spending / 1e6) # 백만 단위
    
    income_totals.append(tot_income)
    M_income_totals.append(tot_income / 1e6) # 백만 단위
    
    print("-----------------------")
    print("{} 시즌 총 이적료 지출 : {:,} 유로 ({}M 유로)\n".format(season_nums[season_count], tot_spending, M_spending_totals[season_count]))
    
    print("총 영입 인원 : {} 명".format(spending_count))
    print("FA 영입 인원 : {} 명".format(FA_arrival_nums))
    print("임대 영입 인원 : {} 명".format(Loan_arrival_nums))
    print("유스 콜업 인원 : {} 명\n".format(Callup_nums))

    print("{} 시즌 총 이적료 수입 : {:,} 유로 ({}M 유로)\n".format(season_nums[season_count], tot_income, M_income_totals[season_count]))

    print("총 방출 인원 : {} 명".format(tot_departure_nums))
    print("FA 방출 인원 : {} 명".format(FA_departure_nums))
    print("임대 이적 인원 : {} 명".format(Loan_departure_nums))
    print("-----------------------")
    season_count += 1

width = 0.35
x = np.arange(len(season_nums))

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, M_spending_totals, width, label='이적료 지출', color='red')
rects2 = ax.bar(x + width/2, M_income_totals, width, label='이적료 수입', color='blue')

ax.set_xlabel('시즌')
ax.set_ylabel('이적료(백만 유로)')
ax.set_title('시즌별 이적료 지출 및 수입')
ax.set_xticks(x)
ax.set_xticklabels(season_nums)
ax.legend()

# y 축 레이블 형식 변경 (백만 단위로 표시)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:,.0f}M'.format(x)))

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
