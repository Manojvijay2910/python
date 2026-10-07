from datetime import *

d = date(2020, 10, 21)
t = time(12, 30)
dt = datetime.combine(d, t)
print(dt)