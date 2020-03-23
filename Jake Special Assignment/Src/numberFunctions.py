'''
Created on Mar 21, 2020
Module for doing the functions
@author: jakeluebbe
'''

def Solve(start, finish):
    result = 0
    for i in range(start, finish,1):
        if checkNumber(i):
            result +=1            
    return result
    print(result)

            
def checkNumber(num):
    result = 1
    strNum = str(num)
    prevChar = 0
    for c in strNum:
        if str(prevChar) > str(c):
            result = 0
        else:
            break
        prevChar = c
    return result
        