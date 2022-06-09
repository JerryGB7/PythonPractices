num = int(input("Enter a number: "))
divisors = []

for i in range(2, num):
    if num % i == 0:
        divisors.append(i)
print(divisors)