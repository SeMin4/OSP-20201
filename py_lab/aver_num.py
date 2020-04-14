#!/usr/bin/python

import sys

if __name__ == '__main__':
    num = int(input("How many numbers do you want to average?"))
    sum = 0
    for i in range(num):
        tmp = int(input("Number %d : " % (i + 1)))
        sum += tmp

    average = sum / num
    print("Average : ", average)
