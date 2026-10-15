def safe_sqrt(n):
    if not isinstance(n, (int, float)):
        return "Invalid input"
    if n < 0 :
        return "Cannot take square root of a negative number"
    return n ** 0.5

print(safe_sqrt(10))
print(safe_sqrt(-9))