"""
현대카드 홈페이지 >> 카드 이용내역(매출전표조회) 엑셀 파일 다운로드 후 csv로 변환
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib.ticker import FuncFormatter
import os

# 폰트 설정
font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 경로
file_paths = ['C:/Users/yth21/Desktop/TH/data/hyundaicard_202308.csv',
              'C:/Users/yth21/Desktop/TH/data/hyundaicard_202309.csv',
              'C:/Users/yth21/Desktop/TH/data/hyundaicard_202310.csv']

for file_path in file_paths:
    
    #파일 이름 추출
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    #파일 이름에서 날짜 부분 추출('_' 를 기준으로 분류하고 두번째 부분 선택)
    date_part = file_name.split('_')[1]
    #월 부분만 추출
    month = date_part[-2:]
    
    df = pd.read_csv(file_path, header=[2])

    # 불필요한 정보 제거
    df = df.iloc[:-3, :-1]

    # 금액 합산 시 오류를 피하기 위해 string 형식의 승인금액을 int로 변환
    df['승인금액'] = df['승인금액'].str.replace(',', '').astype(int)

    # 날짜별 결제금액 및 가맹점명 합산
    df_pay = df.groupby('승인일').agg({'승인금액': 'sum', '가맹점명': lambda x: ', '.join(x)}).reset_index()

    # '승인일'을 datetime 형식으로 변경
    df_pay['승인일'] = pd.to_datetime(df_pay['승인일'], format='%Y년 %m월 %d일', errors='coerce')

    # '승인일'에서 연도, 월을 빼고 일만 남김
    df_pay['승인일'] = df_pay['승인일'].dt.strftime('%d')

    # 최대 및 최소 결제일 찾기
    highest_day = df_pay.loc[df_pay['승인금액'].idxmax()]
    lowest_day = df_pay.loc[df_pay['승인금액'].idxmin()]

    # 시각화
    plt.figure(figsize=(15, 7))
    plt.bar(df_pay['승인일'], df_pay['승인금액'], color='skyblue')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}"))
    plt.xlabel('날짜', fontsize=15, fontweight='bold')
    plt.ylabel('원(₩)', fontsize=15, fontweight='bold')
    plt.title(f'{date_part} 지출', fontsize=30, pad=10, fontweight='bold')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.grid(axis='y')
    plt.savefig(f"C:/Users/yth21/Desktop/TH/data/{date_part}.png", dpi=300)
    plt.show()

    # 최대 및 최소 결제일 정보 출력
    print("-----------------------")
    print(f"{month}월 최대 결제일")
    print("승인일 : {}일\n승인금액 : 총 {:,}원\n가맹점명: {}".format(highest_day['승인일'], highest_day['승인금액'], highest_day['가맹점명']))
    print(f"\n{month}월 최소 결제일")
    print("승인일 : {}일\n승인금액 : 총 {:,}원\n가맹점명: {}".format(lowest_day['승인일'], lowest_day['승인금액'], lowest_day['가맹점명']))
    print("-----------------------")
