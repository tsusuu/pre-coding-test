#
# TODO: 간단버전도 만들 예정

import sys

hour, min, sec = sys.stdin.readline().strip().split()
hour, min, sec = int(hour), int(min), int(sec)

getTime = sys.stdin.readline().strip()
getTime = int(getTime)

getHour = 0
getMin = 0
getSec = 0

if getTime > 3600:
    getHour = int(getTime / 3600)
    getTime = getTime - getHour * 3600
    getMin = int(getTime / 60)
    getSec = getTime - getMin * 60

elif getTime < 3600:
    getMin = int(getTime / 60)
    getSec = getTime - getMin * 60

elif getTime < 60:
    getSec = getTime


sec += getSec
if sec >= 60:
    min += 1
    sec -= 60


min += getMin
if min >= 60:
    hour += 1
    min -= 60

hour += getHour
if hour >= 24:
    hour = hour % 24

print(hour, min, sec)
