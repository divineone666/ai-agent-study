# 作业
name = "传播智客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司： {name},:股票代码： {stock_code},:当前股价： {stock_price}")
print("每日增长系数： %.1f, 经过 %d 的增长后, 股价达到：%.2f " % (stock_price_daily_growth_factor,growth_days,finally_stock_price))

# input
print("请说")
name_1= input()
print("好的,你是:%s" % name_1)

# input2
name_2 = input("请说")
print("好的，你是：%s" % name_2)

name_3 = input()
name_4 = input()
print("%s,你是尊贵的: %s" %(name_3,name_4))