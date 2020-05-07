from datetime import datetime

dayOfWeek = datetime.now().isoweekday()  ###返回数字1-7代表周一到周日
print(dayOfWeek)
import time, datetime

# 时间戳
print(int(float(time.time()) * 1000))
print(int(time.time()))
# 今天的日期
print(datetime.date.today())

print(time.strftime("%W"))
def someMethod():
    # a =  datetime.now().microsecond

    currentSecond = datetime.datetime.now().second
    currentMinute = datetime.datetime.now().minute
    currentHour = datetime.datetime.now().hour

    currentDay = datetime.datetime.now().day
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    print(currentSecond, currentMinute, currentHour, currentDay, currentMonth, currentYear)
#
someMethod()

currentYear = datetime.datetime.now().year # 当前时间年份
week_num = (datetime.date.today()) # 当前时间第几周
print(currentYear,week_num)
# parameter = str(currentYear)+'_'+str(int(week_num+1))
# print(parameter)


