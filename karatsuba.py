'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''
import copy


def convertIntToList(integer):
    list = [int(i) for i in str(integer)]
    return list

def preProcessLists(listOfInts1, listOfInts2):
    #make the larger of the two lists even then make the
    #smaller list of equal size
    if (len(listOfInts1) > len(listOfInts2)):
        if len(listOfInts1) % 2 != 0:
            listOfInts1.insert(0, 0)
        tmp = len(listOfInts1) - len(listOfInts2)
        for i in range(1, tmp):
            listOfInts2.insert(0, 0)
    else:
        if len(listOfInts2) % 2 != 0:
            listOfInts2. insert(0, 0)
        tmp = len(listOfInts2) - len(listOfInts1)
        for i in range(1, tmp):
            listOfInts1.insert(0, 0)

    return listOfInts1, listOfInts2

    #karatsuba(listOfInts1, listOfInts2)

#splits a list of even size in half and returns the two lists
def splitList(listofInts):
    half = len(listofInts)//2
    return listofInts[:half], listofInts[half:]




def addLists(list1, list2):
    tmp = []
    carry = 0

    i = len(list1)-1
    j = len(list2)-1

    while i > -1 and j > -1:
        if ((list1[i] + list2[j] + carry) > 9):
            tmp.insert(0, 0)
            carry = 1
        else:
            n = list1[i] + list2[j] + carry
            tmp.insert(0, n)
            carry = 0
        i = i-1
        j = j-1

    n = list1[i]+carry
    tmp.insert(0, n)

    return tmp



def subLists(list1, list2):
    tmp = []
    carry = 0

    i = len(list1)-1
    j = len(list2)-1

    while i > -1 and j > -1:
        if ((list1[i] - list2[j]) < 0):
            tmp.insert(0, ((10+list1[i])-list2[j]))
            carry = 1
        else:
            tmp.insert(0, (list1[i] - list2[j] - carry))
        i = i-1
        j = j-1

    return tmp



def karatsuba(listOfInts1, listOfInts2):
    if (len(listOfInts1) == 1 and len(listOfInts2) == 1):
        tmp = []
        tint1 = "".join(map(str, listOfInts1))
        tint2 = "".join(map(str, listOfInts2))
        tint1 = int(tint1)*int(tint2)
        tint1 = str(tint1)
        for i in tint1:
            tmp.append(i)
        return tmp
    else:
        num = len(listOfInts1)/2

        l1First, l1Second = splitList(listOfInts1)
        l2First, l2Second = splitList(listOfInts2)

        c2 = karatsuba(l1First, l2First)
        c0 = karatsuba(l1Second, l2Second)

        z0 = addLists(l1First, l2First)
        z1 = addLists(l1Second, l2Second)

        z3 = karatsuba(z0, z1)
        z2 = addLists(c2, c0)

        c1 = subLists(z3, z2)

        shift = 2*num
        for i in range(1, shift):
            c2.append(0)
        for x in range(1, num):
            c1.append(0)

        c3 = addLists(c2, c1)

        c3 = addLists(c3, c0)

        return c3



def main():
    userChoice = 1

    while userChoice != 3:
        print("1 = Multiply\n"
              "2 = Exponentiate\n"
              "3 = quit\n")

        userChoice = input("Enter your choice: ")

        while userChoice < 1 or userChoice > 3:
            print("Please enter a number between 1 and 3!")
            userChoice = input("Enter your choice: ")

        if userChoice == 1:
            print("Two numbers will be multiplied using karatsuba")
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            list1 = convertIntToList(num1)
            list2 = convertIntToList(num2)
            list1, list2 = preProcessLists(list1, list2)
            result = karatsuba(list1, list2)
            print(result)



main()