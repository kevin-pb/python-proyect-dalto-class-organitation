def is_prime(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def prime_numbers_until(num):
    prime_numbers = []
    for i in range(3,num):
        result = is_prime(i)
        if result == True: prime_numbers.append(i)
    return prime_numbers

result = prime_numbers_until(13)
print(result)