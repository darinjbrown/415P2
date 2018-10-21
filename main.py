'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''

def convertIntToString(integer):
    intString = str(integer)
    return intString


def multiplyDigit(int1, int2):
    answer = 0
    # do something
    return answer

def difLists(string1:str, string2:str):
    #input two strings of digits and subtracts smaller from larger
    #returns difference
    string1 = str(string1)
    string2 = str(string2)
    string3 = ""
    #set string2 to smaller, string3 for return value
    if len(string1) < len(string2):
        string3 = string1
        string1 = string2
        string2 = string3
        string3 = ""

    len1 = len(string1)
    len2 = len(string2)

    #reverse both strings
    string1 = string1[::-1]
    string2 = string2[::-1]
    carry = 0

    for i in range(len2):
        sub = (int(string1[i])-int(string2[i])- carry)

        #work out borrowing in terms of carry
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0

        string3 = string3 + str(sub)

    #remaining from larger number
    for i in range(len2, len1):
        sub = int(string1[i]) - carry
        if sub < 0:
            sub += 10
            carry = 1
        else:
            carry = 0
        string3 = string3 + str(sub)

    #reverse result
    string3 = string3[::-1]

    return string3




def sumLists(string1:str, string2:str):
    string2 = str(string2)
    string1 = str(string1)
    string3 = ""
    if len(string1) > len(string2):
        string3 = string1
        string1 = string2
        string2 = string3
    string3 = ""
    len1 = len(string1)
    len2 = len(string2)
    dif = len2 - len1

    carry = 0

    #move from left end of both
    for i in range(len1-1,-1,-1):
        sum = int(string1[i]) + int(string2[i+dif]) + carry
        string3 = string3 + str(sum%10)
        carry = sum // 10

    #remaining digits of string2
    for i in range (len2 - len1 - 1, -1, -1):
        sum = int(int(string2[i]) + carry)
        string3 = string3 + str(carry)
        carry = sum // 10

    #remaining carry
    if (carry):
        string3 = string3 + str(carry)

    #reverse string
    string3 = string3[::-1]

    return string3






def kMultiply(string1:str, string2:str):

    #base case
    if len(string1) == 1 and len(string2) == 1:
        return int(string1) * int(string2)

    #make length of each number the same
    if len(string1) < len(string2):
        string1 = extraZeros(string1, len(string2)-len(string1), 'left')
    elif len(string2) < len(string1):
        string2 = extraZeros(string2, len(string1)-len(string2), 'left')

    n = len(string1)
    m = n//2

    #check for odd length of digit, if so do this
    if (n%2) != 0:
        m = m + 1
    BPad = n - m
    APad = BPad + BPad
    w = string1[:m]
    x = string1[m:]
    y = string2[:m]
    z = string2[m:]

    #calculate recursively
    wy = kMultiply(w,y)
    xz = kMultiply(x,z)
    tempK = kMultiply(sumLists(w, x), sumLists(y, z))
    A = extraZeros(wy, APad, 'right')
    B = extraZeros(difLists(difLists(tempK,wy),xz), BPad, 'right')

    return sumLists(A, sumLists(B, xz))

def extraZeros(numString:str, numOfZeros, side):

    # append 0's to beginning or end of a string of digits
    # input paramaters:  string to append, number of zero's to add, left or right side
    # returns modified numString
    numString = str(numString)
    for i in range (numOfZeros):
        if side == 'left':
            numString = str(0) + numString
        else:
            numString = numString + str(0)
    return numString




def main():

    userChoice = 1

    while userChoice != 3:
        print("1 = Multiply\n"
              "2 = Exponentiate\n"
              "3 = quit\n")

        userChoice = input("Enter your choice: ")
        userChoice = int(userChoice)
        while userChoice < 1 or userChoice > 3:
            print("Please enter a number between 1 and 3!")
            userChoice = input("Enter your choice: ")

        if userChoice == 3:
            exit()

        if userChoice == 1:
            string1 = str(input("Enter the first of two positive integers: "))
            string2 = str(input("Enter the second of two positive integers: "))
            print(string1, " * ", string2, " is:")
            print(kMultiply(string1,string2))
            print()

        if userChoice == 2:
            print("exponentiating")

main()