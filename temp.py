import datetime

current = datetime.datetime.now()
recover = current + datetime.timedelta(hours=8)
die = current + datetime.timedelta(hours=20)
print("current : ", current.strftime("%m-%d %H-%M"))
print("recover : ", recover.strftime("%m-%d %H-%M"))
print("die : ", die.strftime("%m-%d %H-%M"))