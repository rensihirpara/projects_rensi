'''61)Write a Python function to calculate the factorial of a number (a
nonnegative integer) '''
#solution

def factorial(n):
    if n==0:
      return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number to compute the factorial:"))
print(factorial(n))

"62)Write a Python function to check whether a number is in a given range"
#solution

def test_range(n):
    if n in range(3,10):
        print("%s is in the range"% str(n))
    else:
        print("the number is outside the given range.")

test_range(5)

"63) Write a Python function to check whether a number is perfect or not."
#solution

def perfect_number(n):
    sum = 0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum==n
print(perfect_number(6))

'''64) Write a Python function that checks whether a passed string is
palindrome or not'''
#solution

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
