# 초콜릿 자르기

a, b = map(int, input().split())
print(min(a, b) * (max(a, b) - 1) + min(a, b) - 1)
