from datetime import datetime, timedelta

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

date_start = datetime(1901, 1, 1)
date_end = datetime(2000, 12, 31)

total_sundays = 0


def daterange(d1, d2):
    return (d1 + timedelta(days=i) for i in range((d2 - d1).days + 1))


for d in daterange(date_start, date_end):
    # print (d.day)
    if (days[d.weekday()] == 'Sunday'):
        if d.day == 1:
            total_sundays += 1

print(total_sundays)
