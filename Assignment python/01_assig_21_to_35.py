''' 21). Write a Python program to add 'in' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then
add 'ly' instead if the string length of the given string is less than 3,
leave it unchanged.'''

#solution

s="abc"
if len(s)>2:
    if s.endswith('in'):
        s +="ly"
    else:
        s +="in"
    print(s)

s="string"
if len(s)>3:
    if s.endswith("ing"):
        s +="ly"
    else:
        s +="ly"
    print(s)
    
s="st"
if len(s)>3:
    if s.endswith("ing"):
        s +="ly"
    else:
        s +="ing"
    print(s)                

'''22) Write a Python function to reverses a string if its length is a multiple
of 4.'''

#solution

def reverse_if_multiple_of_four(a):
    if len(a)%4==0:
       return a[::-1]
    else:
       return a
print(reverse_if_multiple_of_four("ABCD"))
print(reverse_if_multiple_of_four("abc"))
print(reverse_if_multiple_of_four("abcde_fg"))

'''23) Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''

#solution

def first_and_last_two_chars(s):
    if len(s)<2:
        return""
    else:
        return s[:2]+ s[-2:]

print(first_and_last_two_chars("hello_world"))
print(first_and_last_two_chars("Tops_Techonolies"))
print(first_and_last_two_chars("h"))
print(first_and_last_two_chars(""))


"24) Write a Python function to insert a string in the middle of a string"

#solution

def insert_string_in_middle(str,word):
    return str[:2]+ word + str[-2:]

print(insert_string_in_middle("[()]","Python"))
print(insert_string_in_middle("__","pyhton"))

'''29) Write a Python function to get the largest number, smallest num
and sum of all from a list.'''

#solution

def analyze_list(numbers):
    if not numbers:
        return  none,none,none

    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)

    return largest,smallest,total_sum

my_list=[1,2,44,55,99]
largest,smallest,total_sum = analyze_list(my_list)
print(f"Largest:{largest}")
print(f"Smallest:{smallest}")
print(f"sum:{total_sum}")


'''31) Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list
of strings.'''


def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


"32)Write a Python program to remove duplicates from a list. "

a=[1,2,2,2,3,3,4,5,6,6]
dupi_items = set()
uniq_items =[]
for x in a:
    if x not in dupi_items:
        uniq_items.append(x)
        dupi_items.add(x)

print(dupi_items)


"33) Write a Python program to check a list is empty or not."

my_list = []
if not my_list:

 print("the list is empty")

else:
     print("the list is empty")

'''34) Write a Python function that takes two lists and returns true if they
have at least one common member.'''

#solution

list1 = [1,2,3]
list2 = [3,4,5]

def have_comman_member(list1,list2):
    for items in list1:
        if items in list2:
            return True
    return False

print(have_comman_member(list1,list2))
list1 = [1,2,3,4]
list2 = [3,4,5,6]

def have_comman_mem(list1,list2):
    for items in list1:
        if items in list2:
            return True
        return False

print(have_comman_mem(list1,list2))

'''35) Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. 
'''

#solution

def generate_squares():
    
    squares = [x**2 for x in range(1, 31)]
    
    # Get the first 5 elements
    first_five = squares[:5]
    
    # Get the last 5 elements
    last_five = squares[-5:]
    
    print("First 5 elements:", first_five)
    print("Last 5 elements:", last_five)

generate_squares()


















































