#다리 놓기

import math

T = int(input())
bridge = []

for _ in range(T):
    n, m = map(int, input().split())
    #bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    bridge.append(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))

for i in range(T):
    print(bridge[i])

