import time
import pyupbit

access = "xP8bxkf6tZ4HTKPVdye4Md2efkhNvJ9mBY7cDuWC"          # 본인 값으로 변경
secret = "Jq4gMOug15qH1rPCxte67OOzWYPCzn4duuMxZI5W"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# print(upbit.get_balance("KRW-XRP"))
# print(upbit.get_balance("KRW"))

# print(upbit.get_balance("KRW-BTC"))
# print(upbit.get_avg_buy_price("KRW-BTC"))
# print(upbit.get_amount("KRW-BTC"))
# print(upbit.get_chance("KRW-BTC"))
# print(upbit.get_chance("KRW-DKA"))
# print(upbit.get_chance("KRW-XRP"))
# print(upbit.get_balance("KRW-DKA"))
# print(upbit.get_balance("KRW-ETH"))

# print(pyupbit.get_orderbook("KRW-BTC"))


# all_currency = upbit.get_balances()

# print(all_currency[0])


# quantity = upbit.get_balance("KRW-BTC")
# price = upbit.get_avg_buy_price("KRW-BTC")

# pq = quantity * price

# print(upbit.get_individual_order("KRW-BTC"))



# upbit.sell_limit_order("KRW-ETH", 5000000, 0.001)


print(upbit.get_chance("KRW-ETH"))


# while True:
#     try:
#         upbit.buy_limit_order("KRW-BTC", 1000, 20)
#         print("buy success")
#         time.sleep(2)
#     except:
#         print("Error")
#         time.sleep(2)
