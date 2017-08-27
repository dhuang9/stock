import pandas as pd
from pandas_datareader import data as web
import datetime

start = datetime.datetime(2017, 8, 1)
end = datetime.date.today()

# 获取数据
apple = web.DataReader("AAPL", "yahoo", start, end)

print(type(apple))

print(apple.head())