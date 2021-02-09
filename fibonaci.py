# Memoization

def fibonnaci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fibonnaci(n - 1, memo) + fibonnaci(n-2, memo)
        return memo[n]

print(fibonnaci(int(input("Enter a number to get the Fibonnachi number: "))))