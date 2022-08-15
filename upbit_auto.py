import time
import datetime
import pyupbit
import os

access = os.environ.get("UPBIT_ACCESS_KEY_office")          # 본인 값으로 변경
secret = os.environ.get("UPBIT_SECRET_KEY_office")  
upbit = pyupbit.Upbit(access, secret)

BTC = "KRW-BTC"
ETH = "KRW-ETH"

while True:
    amount_BTC = upbit.get_amount(BTC)
    # print("amount:", amount_BTC)
    balance_BTC = upbit.get_balance(BTC)
    # print("balance_BTC:", balance_BTC)
    avg_buy_price_BTC = upbit.get_avg_buy_price(BTC)
    # print("avg_buy_price_BTC:", avg_buy_price_BTC)
    current_price_BTC = pyupbit.get_current_price(BTC)
    # print("current_price_BTC:", current_price_BTC)
    balance_5050_BTC = 5050/current_price_BTC
    # print("balance_5050_BTC:", balance_5050_BTC)

    time.sleep(21600)

    try:
        if upbit.get_balance(BTC) < balance_5050_BTC:
            upbit.buy_market_order(BTC, 5050)
            print("비트코인,", upbit.get_amount(BTC), "원 남은 상태에서 5050원어치 매수")
        else:
            earning_ratio_BTC = (current_price_BTC-avg_buy_price_BTC)/avg_buy_price_BTC*100
            # print("비트코인 earning_ratio_BTC:", earning_ratio_BTC)
            
            if earning_ratio_BTC > 3:
                upbit.sell_market_order(BTC, balance_5050_BTC)
                print("비트코인 시장가 5050 매도")

            elif earning_ratio_BTC < 0:
                upbit.buy_market_order(BTC, 5050)
                print("비트코인 시장가 5050 매수")
                
            else:
                print("비트코인 매도 매수 없이 패스")
                pass
    except Exception as e:
        print(e)
    
    amount_ETH = upbit.get_amount(ETH)
    # print("amount:", amount_ETH)
    balance_ETH = upbit.get_balance(ETH)
    # print("balance_ETH:", balance_ETH)
    avg_buy_price_ETH = upbit.get_avg_buy_price(ETH)
    # print("avg_buy_price_ETH:", avg_buy_price_ETH)
    current_price_ETH = pyupbit.get_current_price(ETH)
    # print("current_price_ETH:", current_price_ETH)
    balance_5050_ETH = 5050/current_price_ETH
    # print("balance_5050_ETH:", balance_5050_ETH)


    try:
        if upbit.get_balance(ETH) < balance_5050_ETH:
            upbit.buy_market_order(ETH, 5050)
            print("이더리움 첫구매: 시장가 5050 매수")
        else:
            earning_ratio_ETH = (current_price_ETH-avg_buy_price_ETH)/avg_buy_price_ETH*100
            # print("이더리움 earning_ratio_ETH:", earning_ratio_ETH)
            
            if earning_ratio_ETH > 3:
                upbit.sell_market_order(ETH, balance_5050_ETH)
                print("이더리움 시장가 5050 매도")
            
            elif earning_ratio_ETH < 0:
                upbit.buy_market_order(ETH, 5050)
                print("이더리움 시장가 5050 매수")
                
            else:
                print("이더리움 매도 매수 없이 패스")
                pass
    except Exception as e:
        print(e)
    
    print(datetime.datetime.now())
    print("-"*100)
    