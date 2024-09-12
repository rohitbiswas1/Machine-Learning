#Factorial Calculator
Number =int(input("Enter any number : "))
factorial=1

while Number >0:
    factorial= factorial*Number
    Number =  Number-1

print("Factorial: ", factorial)
