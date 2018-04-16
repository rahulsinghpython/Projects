
import time

print(time.gmtime())

time_here = time.localtime()
print(time_here)
print("year:", time_here[0], time_here.tm_year)
print("month:", time_here[1], time_here.tm_mon)
print("day:", time_here[2], time_here.tm_mday)


import time
from time import time as my_timer
# from time import process_time as my_timer
# for using a seperate way instead of clock in computer
import random

input("please enter to start")

wait_time= random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at "+ time.strftime("%X", time.localtime(end_time)))

print("your reaction time was {} seconds.".format(end_time - start_time))
