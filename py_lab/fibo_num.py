#!/usr/bin/python

import sys

if __name__ == '__main__':
    num = int(input("fibonacci number?"))
    arr = []
    arr.append(0)
    arr.append(1)

    for i in range (2, num + 1):
        arr.insert(i, arr[i - 1] + arr[i -2])


    for i in range(1, num + 1) :
        if i < num :
            print(arr[i], end =',')
        else :
            print(arr[i])
   
    print("F%d = %d" % (num , arr[num]))
