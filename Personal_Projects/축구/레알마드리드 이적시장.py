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

#tot_spending_1415 = RM_transfer_1415
#avg_spending_1415 = RM_transfer_1415['이적료(유로)'].mean()
"""
def mean_calculator(season):
    
    for i in range(len(season['이적료(유로)'])):
        tot_spending = 0
        tot_spending = tot_spending + season['이적료(유로)'].iloc[i]
        
        if (season['이적료(유로)'][i] > 0):
            tot_spending = tot_spending - season['이적료(유로)'].iloc[i]
            
            
    return tot_spending
"""

def yearly_transfer_arrangement(season):
    
    tot_spending = 0
    count = 0
    
    for i in range(len(season['이적료(유로)'])):
        tot_spending = tot_spending + season['이적료(유로)'].iloc[i]
        count += 1
        
        if (season['이적료(유로)'].iloc[i] > 0):
            tot_spending = tot_spending - season['이적료(유로)'].iloc[i]
            count -= 1

    tot_spending = tot_spending * -1
    avg_spending = tot_spending / count

    print("{} 시즌 총 이적료 : {:,} 유로".format(season_nums[0], tot_spending))
    print(avg_spending)
    print(len(season['이적료(유로)']))
    
yearly_transfer_arrangement(RM_transfer_1415)
    
"""
tot_spending = 0
count = 0
for i in range(len(RM_transfer_1415['이적료(유로)'])):
    tot_spending = tot_spending + RM_transfer_1415['이적료(유로)'].iloc[i]
    count += 1
    
    if (RM_transfer_1415['이적료(유로)'].iloc[i] > 0):
        tot_spending = tot_spending - RM_transfer_1415['이적료(유로)'].iloc[i]
        count -= 1

tot_spending = tot_spending * -1
avg_spending = tot_spending / count

print("총 이적료", tot_spending)
print(avg_spending)
print(len(RM_transfer_1415['이적료(유로)']))
#print(mean_calculator(RM_transfer_1415))
"""
