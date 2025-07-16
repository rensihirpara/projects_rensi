'''36) Write a Python function that takes a list and returns a new list with
unique elements of the first list.'''
#solution

def unique_items(nums):
    unique = []
    for a in nums:
        if a not in unique:
            unique.append(a)
    return unique
print(unique_items([1,2,2,3,3,4,5,5]))
        
"37)Write a Python program to convert a list of characters into a string."
#solution

x = ['a','p','p','l','e']
str1="".join(x)
print(str1)

"38)Write a Python program to select an item randomly from a list."
#solution 1

my_list = ['1','2','3','a','b','c']
import random
print(random.choice(my_list))

#solution 2

def random_items(list1):
    from random import choice
    return choice(list1)
print(random_items([1,2,33,44,55]))

"39)Write a Python program to find the second smallest number in a list."
#solution

mylist=[22,44,55,666,777,40]
mylist.sort()
print(mylist)
print("second_smallest:",mylist[+1])

"40) Write a Python program to get unique values from a list "
#solution

list1=[1,1,2,33,33,44,55,55,55,66]
unique_list=[]
for q in list1 :
    if q not in unique_list:
        unique_list.append(q)
print(unique_list)

"41) Write a Python program to check whether a list contains a sub list "
#solution

def contains_sublist(main_list,sublist):
    len_main = len(main_list)
    len_sub = len(sublist)

    for i in range(len_main-len_sub+1):
        if main_list[i:i+len_sub]==sublist:
            return True
    return False
    
main_list = [1,2,3,4,5,6,]
sublist = [3,4,5]

if contains_sublist(main_list,sublist):
    print("The list contains the sublist.")
else:
    print("The list does not contains the sublist.")

"42) Write a Python program to split a list into different variables."
#solution

test = [("unit_1"),("unit_2"),("unit_3"),("abc(123)"),("oral_test")]

opt1,opt2,opt3,opt4,opt5 = test

print(opt1)
print(opt2)
print(opt3)
print(opt4)
print(opt5)

"44)Write a Python program to create a tuple with different data types. "
#solution

mytuple = ("apple", 2233,120.1022,[11,23,33],True,)
print("tuple with different data base:",mytuple)
print("integer:",mytuple[1])
print("string:",mytuple[0])
print("float:",mytuple[2])
print("list:",mytuple[3])
print("boolean:",mytuple[4])

"45)Write a Python program to unzip a list of tuples into individual lists. "

#solution
#tuple
l = [(1,2),(3,4),(5,6),(7,8)]
result = list(zip(*l))
print(result)

"46)Write a Python program to convert a list of tuples into a dictionary."
#solution

list2 = [(1,'apple'),(2,'banana'),(3,'cherry')]
dictionary = dict(list2)
print("dictionary:",dictionary)

'''48) Write a Python script to sort (ascending and descending) a
dictionary by value.'''
#solution

my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
    
sorted_dict_asc = dict(sorted(my_dict.items(),key = lambda item : item[1]))
sorted_dict_des = dict(sorted(my_dict.items(),key = lambda item : item[1],reverse = True))
print("assending order:",sorted_dict_asc)
print("descending order:",sorted_dict_des)

'''9)Write a Python script to concatenate following dictionaries to create
a new one'''

#SOLUTION

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

new_dict = {**dict1,**dict2,**dict3}
print("concatenate dictionary :",new_dict)

'''50) Write a Python script to check if a given key already exists in a
dictionary.'''

#solution

my_dict1 = {'apple': 5, 'banana': 2, 'cherry': 8}

def check_key_exits(dictionary,key):
    if key in dictionary:
        return True
    else:
        return False
    
key_to_check = 'apple'
exits = check_key_exits(my_dict1, key_to_check)
print(f"does the key '{key_to_check}'exit in the dictionary?:",exits)
     
 










