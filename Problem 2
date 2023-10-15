#Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(candles):
    max_height = max(candles)
    return candles.count(max_height)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()




#Number Line Jumps
import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        d = (x2 - x1) / (v1 - v2)
        if d.is_integer() and d >= 0:
            return "YES"
        else:
            return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()




#Viral Advertising
import math
import os
import random
import re
import sys
def viralAdvertising(n):
    shared = 5
    tot_likes = 0
    
    for _ in range(n):
        liked = shared // 2
        tot_likes += liked
        shared = liked * 3
    return tot_likes 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()





#Recursive Digit Sum
import math
import os
import random
import re
import sys
def superDigit(n, k):
    def sum_of_elements(num):
        if len(num) == 1:
            return int(num)
        else:
            return sum_of_elements(str(sum(int(i) for i in num)))
    superdigit = sum_of_elements(n)
    superdigitconcatenated = sum_of_elements(str(superdigit * k))
    return superdigitconcatenated

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()





#Insertion Sort - Part 1
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    last = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > last:
        arr[i+1] = arr[i] 
        print(' '.join(map(str, arr)))
        i -= 1
    arr[i+1] = last
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)





#Insertion Sort - Part 2
import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



