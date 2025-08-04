# Python uses the input() function to get user input:

username = input('Enter your name: ')

print(username)

# we would need to wrap an int() around the input() to convert the text string into a number:

age = int(input('What is your age? '))

print(age)

# try the Quadratic formula!

a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

x1 = (-b - ((b**2) - 4*a*c)**0.5)/2*a
x2 = (-b + ((b**2) - 4*a*c)**0.5)/2*a


print(x1)
print(x2)
