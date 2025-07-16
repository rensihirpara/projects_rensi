"72) Write a Python program to read an entire text file. "
#solution

def file_read(Assignment_01):
    txt = open(Assignment_01)
    print(txt.read())

file_read('01_assig_71_to_90.txt')

"73)Write a Python program to append text to a file and display the text."
#solution

def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')

"74) Write a Python program to read first n lines of a file"
#solution
def file_read_from_head(Assignment_01, nlines):
        from itertools import islice
        with open(Assignment_01) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('poem.txt',2)


"75) Write a Python program to read last n lines of a file."
#solution
with open('Assignment_01.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print (last_line)

"76)Write a Python program to read a file line by line and store it into a list"
#solution

def file_read(Assignment_01):
        with open(Assignment_01) as f:    
                content_list = f.readlines()
                print(content_list)

file_read('poem.txt')

"77)Write a Python program to read a file line by line store it into a variable."
#solution

def file_read(Assignment_01):
        with open (Assignment_01, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('poem.txt')

"78)Write a python program to find the longest words."
#solution

def longest_word(Assignment_01):
    with open(Assignment_01, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('poem.txt'))

"79)Write a Python program to count the number of lines in a text file"
#solution

def file_lengthy(Assignment_01):
        with open(Assignment_01) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("poem.txt"))

"80)Write a Python program to count the frequency of words in a file."

#solution
from collections import Counter
def word_count(Assignment_01):
        with open(Assignment_01) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("poem.txt"))

"81)Write a Python program to write a list to a file." 
#solution

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())

"82)Write a Python program to copy the contents of a file to another file."
#solution

from shutil import copyfile
copyfile('practicing.py', 'abc.py')


'''90)Write python program that user to enter only odd numbers, else
will raise an exception. '''
#solution

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")











