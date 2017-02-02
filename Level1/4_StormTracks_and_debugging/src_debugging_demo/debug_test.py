# -*- coding: utf-8 -*-


def user_input():
    flag = True
    while flag :
        ip = raw_input('some number...')
        if ip.isalpha():
            print 'try again'
        else:
            i_ip = float(ip)
            flag = False
    return i_ip


def main():
    mylist = (1, 2, 3)
    for item in mylist:
        print item
        print item + user_input()
        
        
if __name__ == "__main__":
    main()
