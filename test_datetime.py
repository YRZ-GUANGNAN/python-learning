# import datetime
# now = datetime.datetime.now()
# print(now)

from datetime import datetime

s = datetime.now()

dt = datetime.strftime(s,"%Y-%m-%d %H:%M:%S")
print(dt)