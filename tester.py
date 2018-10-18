import sys
import random
import time
current_time = lambda: int(round(time.time() * 1000))
from mymap import mymap

largeList = []
for i in range(1000000):
  largeList.append(random.randint(1,1000000))

largeMap = {}
for i in range(1000000):
  largeMap[random.randint(1,1000000)] = "something"

# your class will be tested similarly:
# mymapobject = mymap()
# for i in range(1000000):
#   mymapobject.put(str(random.randint(1,1000000)), "something");

startTime = current_time()

""" Uncomment this for-loop to see how long it takes to determine if a number is in a large list one-million times (it'll take a looooowng long time)
for i in range(1000000):
  if -1 in largeList:
    print("Element is in there!")
"""

""" Uncomment this for-loop to see how long it takes to determine if a number is in a large MAP (dictionary)  one-million times (should be fast like Toro going after that feather toy thingy)
for i in range(1000000):
  if -1 in largeMap:
    print("Element is in there!")
"""

""" Your class will be tested like this (of course the correct functionality will be tested too):
for i in range(1000000):
  if mymapobject.contains(-1):
    print("Element is in there!")
"""

endTime = current_time()


print(startTime)
print(endTime)

print("done")
print("Testing loop took " + str(endTime - startTime) + " milliseconds.")

