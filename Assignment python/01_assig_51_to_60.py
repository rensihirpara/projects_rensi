'''53) Write a Python script to print a dictionary where the keys are
numbers between 1 and 1'''
#solution

my_dict = {i: i ** 2 for i in range(1, 16)}
print(my_dict)


"54) Write a Python program to check multiple keys exists in a dictionary"
#solution

dict1 = {'abc':1,'def':2,'ghi':3,'jkl':4}
def check_keys_exit(dictionary,keys):
    return all(key in dictionary for key in keys)
keys_to_check = {'def','abc'}

if check_keys_exit(dict1,keys_to_check):
    print("all keys exit.")
else:
    print("all keys are missing")

"55) Write a Python script to merge two Python dictionaries"
#solution

dict2 = {'apple':1,'banana':2,'cherry':3}
dict3 = {'rohan':4,'mohan':5,'sohan':6}

def merge_dicts(dict2,dict3):
    merged_dict = {**dict2,**dict3}
    return merged_dict
merged_dict = merge_dicts(dict2,dict3)
print("merged dictionary:",merged_dict)

'''56) Write a Python program to map two lists into a dictionary
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).'''
#solution

keys = ['a','b','d','c']
value = [400,400,400,300]
main_dict = dict(zip(keys,value))
print(main_dict)

"57)Write a Python program to find the highest 3 values in a dictionary "
#solution

my_dict1 = {'a': 50, 'b': 400, 'c': 100, 'd': 300, 'e': 200}

def top_n_values(dictionary,n):
    return sorted(dictionary.values(), reverse = True)[:n]
top_3_values = top_n_values(my_dict1,3)
print("top 3 values:",top_3_values)

'''58)Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
• Counter ({'item1': 1150, 'item2': 300})'''
#solution

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

from collections import Counter

def combine_values(dicts4):
    combined = Counter()
    for d in dicts4:
        combined[d['item']]+=d['amount']
    return combined
combined_result = combine_values(data)
print("Counter:",combined_result)

'''59)Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.'''
#solution

from collections import Counter

def string_to_dict(s):
    return Counter(s)

# Example usage:
input_string = "hello world"
letter_count = string_to_dict(input_string)

print("Letter count dictionary:", letter_count)

'''60)Sample string:
 'w3resource' Expected output:
• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''
#solution

from collections import Counter

def string_to_dict(s):
    return Counter(s)

# Sample string:
input_string = "w3resource"
letter_count = string_to_dict(input_string)

print("Letter count dictionary:", letter_count)


























