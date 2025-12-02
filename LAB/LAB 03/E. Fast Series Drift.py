def binaryExponentiation(a, b, m):
    answer = 1
    a %= m
    while b > 0:
        if b%2 == 1:
            answer = (answer*a) % m
        a = a*a % m
        b = b >> 1
    return answer


def fastSeriesDrift(a, n, m):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    mid_power = n // 2
    
    # Even power
    if n%2 == 0:
        answer = fastSeriesDrift(a, mid_power, m)
        return answer * (1 + binaryExponentiation(a, mid_power, m)) % m
    
    # Odd case
    else:
        return (fastSeriesDrift(a, n-1, m) + binaryExponentiation(a, n, m)) % m


T = int(input())
for _ in range(T):
    arr = input().split(" ")
    a = int(arr[0])
    n = int(arr[1])
    m = int(arr[2])
    print(fastSeriesDrift(a, n, m))
