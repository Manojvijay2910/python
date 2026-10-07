from datetime import date
import time

startTime = time.perf_counter()
dates = []

d1 = date(2018, 8, 12)
d2 = date(2017, 8, 12)
d3 = date(2016, 8, 12)

dates.append(d1)
dates.append(d2)
dates.append(d3)

dates.sort()

time.sleep(3)
for d in dates:
    print(d)

endTime = time.perf_counter()

print("Execution time: {}".format(endTime - startTime))