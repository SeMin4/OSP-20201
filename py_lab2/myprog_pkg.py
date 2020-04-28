#!/usr/bin/python

import my_pkg
import sys

if __name__ == '__main__':
    while True :
        select_menu = int(input("Select menu: 1) conversion 2) union/intersection 3)exit ? "))
        if (select_menu == 3):
            print("exit the program...")
            sys.exit()
        elif(select_menu == 1):
            binary_str = input("input binary number : ")
            binary_str = "0b" + binary_str
            print("=> OCT>",my_pkg.binaryToOct(binary_str))
            print("=> DEC>",my_pkg.binaryToDec(binary_str))
            print("=> HEX>",my_pkg.binaryToHex(binary_str))
        elif (select_menu == 2):
            first_list = input("1st list: ")
            second_list = input("2nd list: ")
            first_list = first_list.replace('[','')
            first_list = first_list.replace(']','')
            first_list = first_list.replace(' ','')
            first_list = list(map(int, first_list.split(',')))
            second_list = second_list.replace('[','')
            second_list = second_list.replace(']','')
            second_list = second_list.replace(' ','')
            second_list = list(map(int, second_list.split(',')))
            print("=> union", my_pkg.unionSet(first_list, second_list))
            print("=> intersection", my_pkg.intersectionSet(first_list,second_list))




