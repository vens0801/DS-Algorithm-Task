def factorial_using_recursion(n):
    if n == 1 or n == 0 :
        return 1
    return n * factorial_using_recursion(n-1)

n = int(input())
result = factorial_using_recursion(n)
print(result)
