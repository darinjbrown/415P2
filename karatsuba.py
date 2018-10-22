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
    if len(listOfInts1) > len(listOfInts2):
        if (len(listOfInts1) % 2) != 0 and len(listOfInts1) > 1:
            listOfInts1.insert(0, 0)
        tmp = len(listOfInts1) - len(listOfInts2)
        while tmp > 0:
            listOfInts2.insert(0, 0)
            tmp = tmp - 1

    elif len(listOfInts1) < len(listOfInts2) and len(listOfInts2) > 1:
        if (len(listOfInts2) % 2) != 0:
            listOfInts2.insert(0, 0)
        tmp = len(listOfInts2) - len(listOfInts1)
        while tmp > 0:
            listOfInts1.insert(0, 0)
            tmp = tmp - 1
    else:
        if (len(listOfInts1) % 2) != 0 and len(listOfInts1) > 1:
            listOfInts1.insert(0, 0)
            listOfInts2.insert(0, 0)

    return listOfInts1, listOfInts2


#splits a list of even size in half and returns the two lists
def splitList(listofInts):
    half = len(listofInts)//2
    return listofInts[:half], listofInts[half:]




def addLists(list1, list2):
    tmp = []
    carry = 0
    list1, list2 = preProcessLists(list1, list2)
    i = (len(list1)-1)

    while i > -1:
        if (int(list1[i]) + int(list2[i]) + carry) > 9:
            sumElem = int(list1[i]) + int(list2[i]) + carry
            sumElem = sumElem % 10
            tmp.insert(0, sumElem)
            carry = 1
        else:
            n = int(list1[i]) + int(list2[i]) + carry
            tmp.insert(0, n)
            carry = 0
        i = i-1
    '''
    if ((int(list1[i]) + int(list2[i]) + carry) > 9):
        sumElem = int(list1[i]) + int(list2[i]) + carry
        sumElem = sumElem % 10
        tmp.insert(0, sumElem)
        carry = 1
    else:
        n = int(list1[i]) + int(list2[i]) + carry
        tmp.insert(0, n)
        carry = 0
    '''
    if carry > 0:
        tmp.insert(0, carry)

    return tmp



def subLists(list1, list2):
    tmp = []
    carry = 0
    list1, list2 = preProcessLists(list1, list2)
    i = (len(list1))

    while i > -1:
        if (int(list1[i]) - int(list2[i])) < 0:
            tmp.insert(0, ((10+int(list1[i])) - int(list2[i]) - carry))
            carry = 1
        else:
            tmp.insert(0, (int(list1[i]) - int(list2[i]) - carry))
            carry = 0
        i = i-1

    return tmp



def karatsuba(listOfInts1, listOfInts2):

    if len(listOfInts1) == 1 and len(listOfInts2) == 1:
        tmp = []
        tint1 = "".join(map(str, listOfInts1))
        tint2 = "".join(map(str, listOfInts2))
        tint1 = int(tint1)*int(tint2)
        tint1 = str(tint1)
        for i in tint1:
            tmp.append(int(i))
        return tmp

    else:
        listOfInts1, listOfInts2 = preProcessLists(listOfInts1, listOfInts2)
        nm = len(listOfInts1)/2

        l1First, l1Second = splitList(listOfInts1)
        l2First, l2Second = splitList(listOfInts2)

        c2 = karatsuba(l1First, l2First)
        c0 = karatsuba(l1Second, l2Second)

        fHalf = addLists(l1First, l2First)
        sHalf = addLists(l1Second, l2Second)

        z3 = karatsuba(fHalf, sHalf)

        z2 = addLists(c2, c0)

        c1 = subLists(z3, z2)

        shift = nm + nm

        i = 0
        while i < shift:
            c2.append(0)
            i = i+1
        j = 0
        while j < nm:
            c1.append(0)
            j = j+1

        c3 = addLists(c2, c1)

        result = addLists(c3, c0)

        return result



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
            result = karatsuba(list1, list2)
            print(result)



main()