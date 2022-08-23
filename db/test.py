# -*- coding: utf-8 -*-
from chinese_calendar import is_workday
from datetime import datetime
from datetime import timedelta

# 当前日期N天前的证券交易日
def get_trade_day(trade_day,n):
    """
    :param trade_day: 指定日期
    :param n:距离当前多少天(负数往后推，正数往前推,为0为距离当前最近的交易日)
    :return:
    """

    d = datetime.strptime(trade_day, '%Y%m%d')
    dt = datetime.date(d)


    if n < 0:
        t = -n
    else:
        t = n
    for i in range(100):
        if n < 0:
            delta_day = timedelta(days=-i)
        else:
            delta_day = timedelta(days=i)
        trade_day = dt - delta_day
        if is_workday(trade_day) and trade_day.weekday() < 5:  # 工作日并且不是周末
            if t == 0:
                break
            t = t - 1


    return trade_day.strftime('%Y%m%d')


def get_trade_day_near(year,month,today,n):
    """
    :param trade_day: 指定日期
    :param n:距离当前多少天(负数往后推，正数往前推,为0为距离当前最近的交易日)
    :return:
    """
    trade_day = year + month + today
    d = datetime.strptime(trade_day, '%Y%m%d')
    dt = datetime.date(d)


    if is_workday(dt):
        transTodayDate = get_trade_day(trade_day, n)
    else:
        transTodayDate = get_trade_day(trade_day, n-1)

    # 季报时间
    # 第一季度
    if 5<= int(month) < 8:
        dateQuarter = get_trade_day(year + '0331', 0)
    # 第二季度
    elif 8<= int(month) < 10:
        dateQuarter = get_trade_day(year+'0630', 0)
    # 第三季度
    elif 11<= int(month) or int(month)< 1:
        dateQuarter = get_trade_day(year+'0930', 0)
    # 上一年第四季度
    else:
        dateQuarter = get_trade_day(str(int(year)-1) + '1231', 0)

    # 半年报时间
    if 7 <= int(month):
        dateYear = get_trade_day(year+'0630', 0)
    else:
        dateYear = get_trade_day(str(int(year) - 1) + '1231', 0)


    return transTodayDate,dateQuarter,dateYear



if __name__ == '__main__':
    # year = datetime.now().strftime('%Y')
    # month = datetime.now().strftime('%m')
    # today = datetime.now().strftime('%d')
    year = '2022'
    month = '08'
    today = '01'

    print(get_trade_day_near(year, month, today, 1))


