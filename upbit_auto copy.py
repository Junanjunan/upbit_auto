import time
import datetime
import pyupbit
import os

access = os.environ.get("UPBIT_ACCESS_KEY_office")
secret = os.environ.get("UPBIT_SECRET_KEY_office")  
upbit = pyupbit.Upbit(access, secret)

BTC = "KRW-BTC"
ETH = "KRW-ETH"

while True:
    amount_BTC = upbit.get_amount(BTC)
    print("amount:", amount_BTC)
    balance_BTC = upbit.get_balance(BTC)
    print("balance_BTC:", balance_BTC)
    avg_buy_price_BTC = upbit.get_avg_buy_price(BTC)
    print("avg_buy_price_BTC:", avg_buy_price_BTC)
    current_price_BTC = pyupbit.get_current_price(BTC)
    print("current_price_BTC:", current_price_BTC)
    balance_7000_BTC = 7000/current_price_BTC
    print("balance_7000_BTC:", balance_7000_BTC)

    try:
        if avg_buy_price_BTC == 0:
            upbit.buy_market_order(BTC, 7000)
            print("비트코인 첫구매: 시장가 7000 매수")
        else:
            earning_ratio_BTC = (current_price_BTC-avg_buy_price_BTC)/avg_buy_price_BTC*100
            print("비트코인 earning_ratio_BTC:", earning_ratio_BTC)
            
            if earning_ratio_BTC > 3:
                if upbit.get_balance(BTC) < balance_7000_BTC:
                    upbit.buy_market_order(BTC, 7000)
                    print("비트코인,", upbit.get_amount(BTC), "원 남은 상태에서 7000원어치 매수")
                else:
                    upbit.sell_market_order(BTC, balance_7000_BTC)
                    print("비트코인 시장가 7000 매도")

            elif earning_ratio_BTC < 0:
                upbit.buy_market_order(BTC, 7000)
                print("비트코인 시장가 7000 매수")
                
            else:
                print("비트코인 매도 매수 없이 패스")
                pass
    except Exception as e:
        print(e)
    
    amount_ETH = upbit.get_amount(ETH)
    print("amount:", amount_ETH)
    balance_ETH = upbit.get_balance(ETH)
    print("balance_ETH:", balance_ETH)
    avg_buy_price_ETH = upbit.get_avg_buy_price(ETH)
    print("avg_buy_price_ETH:", avg_buy_price_ETH)
    current_price_ETH = pyupbit.get_current_price(ETH)
    print("current_price_ETH:", current_price_ETH)
    balance_7000_ETH = 7000/current_price_ETH
    print("balance_7000_ETH:", balance_7000_ETH)


    try:
        if avg_buy_price_ETH == 0:
            upbit.buy_market_order(ETH, 7000)
            print("이더리움 첫구매: 시장가 7000 매수")
        else:
            earning_ratio_ETH = (current_price_ETH-avg_buy_price_ETH)/avg_buy_price_ETH*100
            print("이더리움 earning_ratio_ETH:", earning_ratio_ETH)
            
            if earning_ratio_ETH > 3:
                if upbit.get_balance(ETH) < balance_7000_ETH:
                    upbit.buy_market_order(ETH, 7000)
                    print("이더리움,", upbit.get_amount(ETH), "원 남은 상태에서 7000원어치 매수")
                else:
                    upbit.sell_market_order(ETH, balance_7000_ETH)
                    print("이더리움 시장가 7000 매도")
            
            elif earning_ratio_ETH < 0:
                upbit.buy_market_order(ETH, 7000)
                print("이더리움 시장가 7000 매수")
                
            else:
                print("이더리움 매도 매수 없이 패스")
                pass
    except Exception as e:
        print(e)
    
    print(datetime.datetime.now())
    print("-"*100)
    time.sleep(3600)