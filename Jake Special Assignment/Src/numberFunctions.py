'''
Created on Mar 21, 2020
Module for doing the functions
@author: jakeluebbe
'''

def Solve(start, finish):
    result = 0
    for i in range(start, finish,1): #In the range specified in the parameter, increment y 1
        if (checkNumber(i) == 1): #Need this to mean if result in checkNumber  = 1
            result +=1 #Add 1 to result
    print(result)

            
def checkNumber(num):
    result = 1 #default result to the best
    intNum = num #set up intNum for the comparison
    prevChar = 0 #set this to 0 so nothing fails at the very start
    #print("Type for prevChar is " + str(type(prevChar)))
    for i in str(intNum): #for loop to run through the number
        #print("Type for i is " + str(type(i)))
        if int(prevChar) > int(i):
            result = 0 #if the number before is greater than the number being checked in the for loop, result = 0
            break#So if result does become 0, then it doesn't keep checking the rest of the numbers
        else:
            prevChar = i #prevChar = i to check the next number in the loop
    return result
        