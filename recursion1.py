from gettext import find


def findsum(n):
    sum = 0 #base case
    for i in range(1, n+1):
        sum +=i 
    return sum
for n in range(1, 5):
    print(findsum(n))
print(findsum(5))

#stop at 0
#add 5+4+3+2+1

def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)
print(find_sum(5))

#------------------------------------


def fib(n): #fib number at nth position
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)
    #6         (6-1)(5) +    (6-2)(4) = 9
    #4         (4-1)(3) +    (4-2)(2) = 5
print(fib(6))
#0,1,2,3,4,5,6,7,8,9 #i
#0,1,1,2,3,5,8,13,21 #n

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(1,11):
    print(n, ":", fibonacci(n))
# print(fibonacci(11))
    
#memoization: stores values for future function calls so they don't have to repeat the work