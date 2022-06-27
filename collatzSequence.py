# Write a program that lets the user type in an integer and that keeps calling collatz()
# on that number until the function returns the value 1

n = input("Give me a number: ")

def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
   

while n != 1:
    n = collatz(int(n))


