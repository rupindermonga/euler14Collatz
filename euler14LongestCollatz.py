
# n = n/2, n is even
# n = 3n+1, n is odd

def LongestCollatz(n):
    cnt = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n +1
        cnt += 1
    return cnt

def lengthLongestCollatz(n):
    max_length = 0
    for i in range(n):
        if LongestCollatz(i) > max_length:
            max_length = LongestCollatz(i)
            new_number = i
    return new_number

final = lengthLongestCollatz(1000000)
print(final)