# 경고

import sys

now_h, now_m, now_s = map(int, sys.stdin.readline().split(":"))
throw_h, throw_m, throw_s = map(int, sys.stdin.readline().split(":"))
wait_h, wait_m, wait_s = 0, 0, 0

# wait_s
if throw_s < now_s:
    wait_s = throw_s + 60 - now_s
    throw_m -= 1
else:
    wait_s = throw_s - now_s

# wait_m
if throw_m < now_m:
    wait_m = throw_m + 60 - now_m
    throw_h -= 1
else:
    wait_m = throw_m - now_m

# wait_h
if throw_h < now_h:
    wait_h = throw_h + 24 - now_h
else:
    wait_h = throw_h - now_h

if wait_h == 0 and wait_m == 0 and wait_s == 0:
    wait_h = 24

print("%02d:%02d:%02d" % (wait_h, wait_m, wait_s))
