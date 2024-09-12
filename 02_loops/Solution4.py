#Reverse a String
name = input("Enter the name of the string: ") 
reversed_str = ""

for i in name:
    reversed_str = i + reversed_str

print("Reversed string:", reversed_str) 
