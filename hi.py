print("Hello! Myself")



#prime number

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n%i == 0:
        count += 1

if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")   
 





#Palindrome number

num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")