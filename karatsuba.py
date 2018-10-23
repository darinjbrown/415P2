'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''
def minusLists(list1:list, list2:list):
    #make sure subtracting smaller from larger
    list1, list2 = firstListGreaterValue(list1,list2)

    #create empty list to store result
    list3 = []

    #length of each string
    l1 = len(list1)
    l2 = len(list2)

    #reverse both strings
    list1 = list1[::-1]
    list2 = list2[::-1]

    #variable for carrying when borrowing
    carry = 0
    #school mathematics compute difference of current digits
    for i in range(l2):
        sub = (int(list1[i]) - (int(list2[i])-carry))

        #if sub < 0 need to perform borrow/carry
        if sub < 0:
            sub = sub + 10
            carry = 1
        else:
            carry = 0
        subL = convertIntToList(sub)
        list3.extend(subL)

    #reverse string
    list3 = list3[::-1]

    return list3



def exponentiate(num, exp):
    num = list(num)
    strtList = num
    while exp > 1:
        strtList = removeLeadingZeroes(strtList)
        num = removeLeadingZeroes(num)
        numcpy = num
        if exp % 2 == 0:
            num = karatsuba(num, numcpy)
            exp = exp / 2
        else:
            num = karatsuba(num, numcpy)
            num = karatsuba(num, strtList)
            exp = (exp - 1) / 2
    return num

def firstListGreaterValue(list1, list2):
    #input 2 lists
    #after running function return greater then lesser
    #determine number of leading 0's in each list

    if len(list1) > len(list2):
        return list1, list2
    elif len(list1) < len(list2):
        return list2, list1
    else:
        if list1[0] > list2[0]:
            return list1, list2
        else:
            return list2, list1


def listToString(list):
    #convert to string for printing purposes (print answer as 4532 instead of [4,5,3,2])
    result = str("")
    if len(list) == 1:
        return str(list[0])
    for element in list:
        result = str(result) + str(element)
    return result



def convertIntToList(integer):
    list = [int(i) for i in str(integer)]
    return list

def preProcessLists(listOfInts1, listOfInts2):
    #make the larger of the two lists even then make the
    #smaller list of equal size if
    l1 = listOfInts1[:]
    l2 = listOfInts2[:]
    if len(l1) > len(l2):
        if (len(l1) % 2) != 0:
            l1.insert(0, 0)
        tmp = len(l1) - len(l2)
        while tmp > 0:
            l2.insert(0, 0)
            tmp = tmp - 1

    elif len(l1) < len(l2):
        if (len(l2) % 2) != 0:
            l2.insert(0, 0)
        tmp = len(l2) - len(l1)
        while tmp > 0:
            l1.insert(0, 0)
            tmp = tmp - 1

    else:
        if (len(l1) % 2) != 0:
            l1.insert(0, 0)
            l2.insert(0, 0)

    return l1, l2


def removeLeadingZeroes(list1:list):
    i = int(0)
    for i in (list1):
        if list1[0] != 0:
            return list1
        else:
            del(list1[0])
        #while list1[0] == '0':
        #del(list1,[i])

    return list1




def cutLeadingZeroes(list):
    zChecker = 0
    i = 0
    tmp = list[:]
    while i < len(tmp)-2 and zChecker == 0:
        if int(tmp[i]) == 0:
            tmp.pop(0)
        else:
            zChecker = 1
        i = i+1

    return tmp


#splits a list of even size in half and returns the two lists
def splitList(listofInts):
    half = len(listofInts)//2
    return listofInts[:half], listofInts[half:]




def addLists(list1, list2):
    tmp = []
    carry = 0

    if (len(list1) > 1) or (len(list2) > 1):
        list1, list2 = preProcessLists(list1, list2)

    i = (len(list1)-1)

    while i > -1:
        if (int(list1[i]) + int(list2[i]) + carry) > 9:
            n = int(list1[i]) + int(list2[i]) + carry
            n = n % 10
            tmp.insert(0, n)
            carry = 1
        else:
            n = int(list1[i]) + int(list2[i]) + carry
            tmp.insert(0, n)
            carry = 0
        i = i-1

    if carry > 0:
        tmp.insert(0, carry)

    #if len(tmp) > 1:
    #    tmp = cutLeadingZeroes(tmp)
    return tmp



def subLists(list1, list2):
    tmp = []
    carry = 0

    if (len(list1) > 1) or (len(list2) > 1):
        list1, list2 = preProcessLists(list1, list2)

    i = (len(list1)-1)

    while i > -1:
        if (int(list1[i]) - int(list2[i])) < 0:
            tmp.insert(0, ((10+int(list1[i])) - carry - int(list2[i])))
            carry = 1
        else:
            tmp.insert(0, (int(list1[i]) - carry - int(list2[i])))
            carry = 0
        i = i-1

    #if len(tmp) > 1:
    #    tmp = cutLeadingZeroes(tmp)

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

        karat3 = karatsuba(addLists(l1First, l1Second), addLists(l2First, l2Second))

        new1, new2 = karat3, c2
        c1 = minusLists(new1, new2)

        new3, new4 = c1, c0
        c1 = minusLists(new3, new4)

        shift = (nm + nm)

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
        if len(result) > 1:
            result = removeLeadingZeroes(result)
        return result


def main():
    userChoice = 1

    while userChoice != 3:
        print("1 = Multiply\n"
              "2 = Exponentiate\n"
              "3 = quit\n")

        userChoice = int(input("Enter your choice: "))

        while int(userChoice) < 1 or int(userChoice) > 3:
            print("Please enter a number between 1 and 3!")
            userChoice = input("Enter your choice: ")

        if userChoice == 3:
            return

        if userChoice == 1:
            print("Two numbers will be multiplied using karatsuba")
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            list1 = convertIntToList(num1)
            list2 = convertIntToList(num2)
            result = karatsuba(list1, list2)
            result = cutLeadingZeroes(result)

            print(listToString(result))

        if userChoice == 2:

            base = (input("Enter number to exponentiate: "))
            exponent = int((input("Enter the exponent as an integer: ")))
            num = convertIntToList(base)
            result = exponentiate(num, exponent)

            print (listToString(removeLeadingZeroes(result)))


main()