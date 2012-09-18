import time
import math

print time.ctime()
print "Calcul de 20000! ... 20100! Sans threads"
for i in range(20000, 20101):
	math.factorial(i)
print time.ctime()
