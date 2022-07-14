import datetime

from datetime import time
n = int(input())
time1 = datetime.time(2,30)
h = time1 
m = 20



print( h," часов и ",m," минут")
# Ниже правильный вариант действий а не моя сложная хрень
n = int(input())
m = n % 60
k = n -(1440*(n//1440))
h = k // 60
print( h," часов ",m," минут")
