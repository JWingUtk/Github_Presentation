# Example for Dr. Sobes Presentation on Github for pull requests

import time as t
import numpy as np

Tock = t.time()

Array = np.random.rand(10000000)

Sum = 0
for i in range(len(Array)):
    Sum = Sum + Array[i]

Tick = t.time()
Time = Tick-Tock

print ("This process took "+str(Time)+" seconds")

Sum2 = Array.sum()

Tick2 = t.time()
Time2=Tick2-Tick
print("But this one only takes "+str(Time2)+" seconds")
print("That's "+str(Time/Time2)+" times faster!!")
