
# Online Python - IDE, Editor, Compiler, Interpreter
from array import *
def f_sort(a):
    array_name = a
    array_name.sort()

    print(array_name)
    print('task')

    i = 1
    print(array_name[0])
    while i<len(array_name):
 ##   print('шаг'i)
        if array_name[i-1]<array_name[i]:
            print(array_name[i])
        i += 1
        
f_sort([4,4,7,6,1,2,3,4,5])