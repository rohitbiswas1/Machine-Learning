#Prime Number checker
number=int(input("Enter any number : "))

is_prime=True

if number > 1:
    for i in range(2,number):
        if(number % 2 )==0:
            is_prime=False
            break
print(is_prime)