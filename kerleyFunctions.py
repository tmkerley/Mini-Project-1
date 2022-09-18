import datetime as dt

def adjustForWeekends(endDate, delta):
    for i in range(10):
        tempDelta = dt.timedelta(days=i)
        temp = endDate - tempDelta
        if temp.weekday() > 4:
            delta = delta + dt.timedelta(days=1)
    return endDate - delta
