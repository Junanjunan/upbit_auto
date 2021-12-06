import pyupbit

access = "xsh6wVoCZRYgho6pZSysS2vIBJKJB95OsUM6FPK8"          # 본인 값으로 변경
secret = "XEgphpenMNKFbOC0kK86cCxlPMDTCrnH29noO3mS"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# print(upbit.get_balance("KRW-XRP"))
# print(upbit.get_balance("KRW"))
# print(upbit.get_balance("KRW-BTC"))
# print(upbit.get_balance("KRW-DKA"))
# print(upbit.get_balance("KRW-ETH"))

# print(pyupbit.get_orderbook("KRW-BTC"))


all_currency = upbit.get_balances()


print(all_currency[3])
