#Say "Hello, World!" With Python
print("Hello, World!")



#Python If-Else
n=int(input())
if n%2!=0:
    print("Weird")
elif n>=2 and n<=5:
    print("Not Weird")
elif n>=6 and n<=20:
    print("Weird")
elif n>20 and n<=100:
    print("Not Weird")



#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)



#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)



#Loops
if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i*i)
        i+=1



#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')



#Write a function
def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    
    return leap



#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

print(list)



#Nested Lists
if __name__ == '__main__':
    students=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
scores = sorted(set(student[1] for student in students))
secondlowestgrade = scores[1]

secondloweststudents = [student[0] for student in students if student[1] == secondlowestgrade]

secondloweststudents.sort()

for name in secondloweststudents:
    print(name)



#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

if query_name in student_marks:
    marks = student_marks[query_name]
    average_mark = sum(marks) / len(marks)
    print(f'{average_mark:.2f}')
else:
    print("The student is not in the list")



#Lists
if __name__ == '__main__':
    N = int(input())
lista = []

for _ in range(N):
    command, *args = input().split()

    if command == 'insert':
        i, e = map(int, args)
        lista.insert(i, e)
    elif command == 'print':
        print(lista)
    elif command == 'remove':
        e = int(args[0])
        lista.remove(e)
    elif command == 'append':
        e = int(args[0])
        lista.append(e)
    elif command == 'sort':
        lista.sort()
    elif command == 'pop':
        lista.pop()
    elif command == 'reverse':
        lista.reverse()


#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
  
integer_tuple = tuple(integer_list)

hash_value = hash(integer_tuple)
print(hash_value)



#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = sorted(set(arr), reverse=True)

runner_up_score = scores[1]
print(runner_up_score)



#sWAP cASE
def swap_case(s):
    S=s.swapcase()
    return S



#String Split and Join
def split_and_join(line):
    split_line=line.split()
    joined_line = "-".join(split_line)
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")



#Mutations
def mutate_string(string, position, character):
    string_list=list(string)
    string_list[position] = character
    return ''.join(string_list)



#Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count



#String Validators
if __name__ == '__main__':
    s = input()

print(any(c.isalnum() for c in s))

print(any(c.isalpha() for c in s))

print(any(c.isdigit() for c in s))

print(any(c.islower() for c in s))

print(any(c.isupper() for c in s))



#Text Wrap
def wrap(string, max_width):
    wrapped = textwrap.fill(string, max_width)
    return wrapped



#Designer Door Mat
def generatedoor(N, M):
    for i in range(N//2):
        pattern = (('.|.'*(2*i+1)).center(M, '-'))
        print(pattern)

    welcome = 'WELCOME'.center(M, '-')
    print(welcome)

    for i in range(N//2-1, -1, -1):
        pattern = (('.|.'*(2*i+1)).center(M, '-'))
        print(pattern)

if __name__ == "__main__":
    N, M = map(int, input().split())
    generatedoor(N, M)



#String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")



#Introduction to Sets
def average(array):
    heights = set(array)
    tot_height = sum(heights)
    num= len(heights)
    avg= tot_height / num
    return round(avg, 3)



#Check Subset
def is_subset(A, B):
    return A.issubset(B)

n = int(input())

for _ in range(n):
    len_A = int(input())
    set_A = set(map(int, input().split()))
    len_B = int(input())
    set_B = set(map(int, input().split()))
    result = is_subset(set_A, set_B)
    print(result)



#Set Mutations
N_A = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, len_B = input().split()
    len_B = int(len_B)
    B = set(map(int, input().split()))
    
    if operation == 'update':
        A.update(B)
    elif operation == 'intersection_update':
        A.intersection_update(B)
    elif operation == 'difference_update':
        A.difference_update(B)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
        
somma=sum(A)
print(somma)



#Set .symmetric_difference() Operation
num_english = int(input())
e_subscribers = set(map(int, input().split()))
num_french = int(input())
f_subscribers = set(map(int, input().split()))

not_both = (e_subscribers.symmetric_difference(f_subscribers))

tot_students = len(not_both)
print(tot_students)



#Set .difference() Operation
num_e_students = int(input())
e_subscribers = set(map(int, input().split()))
num_f_students = int(input())
f_subscribers = set(map(int, input().split()))

e_subscribers2 = set(e_subscribers)
f_subscribers2 = set(f_subscribers)

both = e_subscribers2.intersection(f_subscribers2)

final_e_subscribers = e_subscribers2 - both

only_english_subscribers = len(final_e_subscribers)

print(only_english_subscribers)



#Set .intersection() Operation
num_e_students = int(input())
e_subscribers = set(map(int, input().split()))
num_f_students = int(input())
f_subscribers = set(map(int, input().split()))

e_subscribers2 = set(e_subscribers)
f_subscribers2 = set(f_subscribers)

both = e_subscribers2.intersection(f_subscribers2)

tot_both = len(both)

print(tot_both)



#Set .union() Operation
num_e_students = int(input())
e_subscribers = set(map(int, input().split()))
num_f_students = int(input())
f_subscribers = set(map(int, input().split()))

e_subscribers2 = set(e_subscribers)
f_subscribers2 = set(f_subscribers)

subscribed = e_subscribers2.union(f_subscribers2)

total = len(subscribed)

print(total)



#Set .add()
N = int(input())
country_stamps = set()

for _ in range(N):
    country = input()
    country_stamps.add(country)

print(len(country_stamps))



#collections.Counter()
X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())

sizes = {size: shoe_sizes.count(size) for size in set(shoe_sizes)}

tot_earned = 0

for _ in range(N):
    size, price = map(int, input().split())
    if size in sizes and sizes[size] > 0:
        tot_earned += price
        sizes[size] -= 1

print(tot_earned)



#Collections.deque()
from collections import deque
d = deque()
N = int(input())

for _ in range(N):
    operation, *args = input().split()
    getattr(d, operation)(*map(int, args))

print(*d)



#DefaultDict Tutorial
n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

dictionary = {}

for i, word in enumerate(A):
    if word in dictionary:
        dictionary[word].append(i+1)
    else:
        dictionary[word] = [i+1]

for word in B:
    if word in dictionary:
        print(*dictionary[word])
    else:
        print(-1)



#Exceptions
T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        result = a // b
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)



#Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    fib_num = [0, 1]
    while len(fib_num) < n:
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num[:n]



#Zipped!
N, X = map(int, input().split())
sum_marks = [0] * N
for _ in range(X):
    marks = list(map(float, input().split()))
    for i in range(N):
        sum_marks[i] += marks[i]

for tot_marks in sum_marks:
    average = tot_marks / X
    av=round(average, 1)
    print(av)



#ginortS
S = input()
def sorting(x):
    if x.islower():
        return (0, x)
    elif x.isupper():
        return (1, x)
    elif x.isdigit():
        if int(x) % 2 == 1:
            return (2, x)
        else:
            return (3, x)

sorted_string = ''.join(sorted(S, key=sorting))

print(sorted_string)



#Re.split()
regex_pattern = r'[,.]'



#Group(), Groups() & Groupdict()
def repeating_character(s):
    for i in range(len(s)-1):
        if s[i].isalnum() and s[i] == s[i+1]:
            return s[i]
    return -1

S = input()
result = repeating_character(S)
print(result)



#Validating Roman Numerals
regex_pattern = r"^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"



#Validating phone numbers
import re
def valid_number(number):
    return bool(re.match(r'^[789]\d{9}$', number))

N = int(input())
given_num = [input() for _ in range(N)]

for number in given_num:
    if valid_number(number):
        print("YES")
    else:
        print("NO")



#XML 1 - Find the Score
def get_attr_number(node):
    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score



#XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)



#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        numbers = []
        for number in l:
            number = number[-10:]
            number = '+91 ' + number[:5] + ' ' + number[5:]
            numbers.append(number)
        f(numbers)
    return fun











