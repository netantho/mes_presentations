import time
import math
import threading

print time.ctime()
print "Calcul de 20000! ... 20100! Avec threads"
th = []
for i in range(20000, 20101):
	th.append(threading.Thread(None, math.factorial, None, (i,)))
for th_elem in th:
	th_elem.start()
print time.ctime()
