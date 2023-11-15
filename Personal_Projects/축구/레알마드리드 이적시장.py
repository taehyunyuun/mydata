import pandas as pd
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
path_1415 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1415.csv'
path_1516 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1516.csv'
path_1617 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1617.csv'
path_1718 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1718.csv'
path_1819 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1819.csv'
path_1920 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_1920.csv'
path_2021 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2021.csv'
path_2122 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2122.csv'
path_2223 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2223.csv'
path_2324 = 'C:/Users/yth21/Desktop/TH/data/Football/RM_transfer_2324.csv'

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
print(season_nums)

RM_transfer_1415 = pd.read_csv(path_1415, header=2)
RM_transfer_1516 = pd.read_csv(path_1516, header=2)
RM_transfer_1617 = pd.read_csv(path_1617, header=2)
RM_transfer_1718 = pd.read_csv(path_1718, header=2)
RM_transfer_1819 = pd.read_csv(path_1819, header=2)
RM_transfer_1920 = pd.read_csv(path_1920, header=2)
RM_transfer_2021 = pd.read_csv(path_2021, header=2)
RM_transfer_2122 = pd.read_csv(path_2122, header=2)
RM_transfer_2223 = pd.read_csv(path_2223, header=2)
RM_transfer_2324 = pd.read_csv(path_2324, header=2)

season_lists = [RM_transfer_1415,
                RM_transfer_1516,
                RM_transfer_1617,
                RM_transfer_1718,
                RM_transfer_1819,
                RM_transfer_1920,
                RM_transfer_2021,
                RM_transfer_2122,
                RM_transfer_2223,
                RM_transfer_2324]

for df in season_lists:
    tot_spending = 0
    tot_income = 0
    spending_count = 0
    income_count = 0
    season_count = 0
    
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

    print("-----------------------")
    print("{} 시즌 총 이적료 지출 : {:,} 유로".format(season_nums[season_count], tot_spending))
    print("인당 평균 이적료 지출 : {:,} 유로\n".format(avg_spending))
    
    print("총 영입 인원 : {} 명".format(spending_count))
    print("FA 영입 인원 : {} 명".format(FA_arrival_nums))
    print("임대 영입 인원 : {} 명".format(Loan_arrival_nums))
    print("유스 콜업 인원 : {} 명".format(Callup_nums))
    print("-----------------------")
    print("{} 시즌 총 이적료 수입 : {:,} 유로".format(season_nums[season_count], tot_income))
    print("인당 평균 이적료 수입 : {:,} 유로\n".format(avg_income))
    print("총 방출 인원 : {} 명".format(tot_departure_nums))
    print("FA 방출 인원 : {} 명".format(FA_departure_nums))
    print("임대 이적 인원 : {} 명".format(Loan_departure_nums))
    print("-----------------------")
    season_count += 1
"""
def yearly_transfer_arrangement(season):
    
    tot_spending = 0
    tot_income = 0
    spending_count = 0
    income_count = 0
    season_count = 2
    
    tot_spending = season[season['이적 형태'] == 'Arrival']['이적료(유로)'].sum()
    tot_spending = tot_spending * -1
    spending_count = len(season[season['이적 형태'] == 'Arrival']['이적료(유로)'])
    avg_spending = round(tot_spending / spending_count)
    
    tot_income = season[season['이적 형태'] == 'Departure']['이적료(유로)'].sum()
    income_count = len(season[season['이적 형태'] == 'Departure']['이적료(유로)'])
    avg_income = round(tot_income / income_count)

    FA_arrival_nums = season[(season['이적 형태'] == 'Arrival') & (season['기타'] == 'FA')].shape[0]
    Loan_arrival_nums = season[(season['이적 형태'] == 'Arrival') & (season['기타'] == 'Loan')].shape[0]
    Callup_nums = season[(season['이적 형태'] == 'Arrival') & (season['기타'] == 'Call up')].shape[0]
    
    tot_departure_nums = len(season['이적료(유로)']) - spending_count
    FA_departure_nums = season[(season['이적 형태'] == 'Departure') & (season['기타'] == 'FA')].shape[0]
    Loan_departure_nums = season[(season['이적 형태'] == 'Departure') & (season['기타'] == 'Loan')].shape[0]

    print("-----------------------")
    print("{} 시즌 총 이적료 지출 : {:,} 유로".format(season_nums[season_count], tot_spending))
    print("인당 평균 이적료 지출 : {:,} 유로\n".format(avg_spending))
    
    print("총 영입 인원 : {} 명".format(spending_count))
    print("FA 영입 인원 : {} 명".format(FA_arrival_nums))
    print("임대 영입 인원 : {} 명".format(Loan_arrival_nums))
    print("유스 콜업 인원 : {} 명".format(Callup_nums))
    print("-----------------------")
    print("{} 시즌 총 이적료 수입 : {:,} 유로".format(season_nums[season_count], tot_income))
    print("인당 평균 이적료 수입 : {:,} 유로\n".format(avg_income))
    print("총 방출 인원 : {} 명".format(tot_departure_nums))
    print("FA 방출 인원 : {} 명".format(FA_departure_nums))
    print("임대 이적 인원 : {} 명".format(Loan_departure_nums))
    print("-----------------------")
    

yearly_transfer_arrangement(season_lists[2])
"""
"""    
for i in range(len(season_lists)):
    yearly_transfer_arrangement(season_lists[i])
"""
