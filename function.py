def sum_list(lst:list):
    total = 0
    for i in lst:
        total += i
    return total

def is_prime(n:int):
    if n < 2:
        return False
    for i in range(2,int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divide(a: int, b: int) -> float :
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def reverse_string(s: str) -> str:
    return s[::-1]

def contains(lst: list, value: int) -> bool:
    if lst:
       return lst.__contains__(value)
    else:
        return False

