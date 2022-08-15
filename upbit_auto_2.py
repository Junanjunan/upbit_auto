import time
import pyupbit
import os

access = os.environ.get("UPBIT_ACCESS_KEY_office")
secret = os.environ.get("UPBIT_SECRET_KEY_office") 
upbit = pyupbit.Upbit(access, secret)

BTC = "KRW-BTC"
ETH = "KRW-ETH"

while True:
    avg_buy_price_BTC = upbit.get_avg_buy_price(BTC)
    current_price_BTC = pyupbit.get_current_price(BTC)
    balance_5050_BTC = 5050/current_price_BTC
    earning_ratio_BTC = (current_price_BTC-avg_buy_price_BTC)/avg_buy_price_BTC*100

    print(earning_ratio_BTC)
    print(balance_5050_BTC)
    print(current_price_BTC*balance_5050_BTC)

    try:
        if earning_ratio_BTC > 5:
            upbit.sell_market_order(BTC, balance_5050_BTC)
            print("시장가 5050 매도")
        
        elif earning_ratio_BTC < -1:
            upbit.buy_market_order(BTC, balance_5050_BTC)
            print("시장가 5050 매수")
            
        else:
            print("매도 매수 없이 패스")
            pass
    except Exception as e:
        print(e)
    
    time.sleep(3600)