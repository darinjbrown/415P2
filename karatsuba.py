'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''


def exponentiate(list1, list2)

def listToString(list):
    #convert to string for printing purposes (print answer as 4532 instead of [4,5,3,2])
    result = str("")
    if len(list) <= 1:
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
    if len(listOfInts1) > len(listOfInts2):
        if (len(listOfInts1) % 2) != 0:
            listOfInts1.insert(0, 0)
        tmp = len(listOfInts1) - len(listOfInts2)
        while tmp > 0:
            listOfInts2.insert(0, 0)
            tmp = tmp - 1

    elif len(listOfInts1) < len(listOfInts2):
        if (len(listOfInts2) % 2) != 0:
            listOfInts2.insert(0, 0)
        tmp = len(listOfInts2) - len(listOfInts1)
        while tmp > 0:
            listOfInts1.insert(0, 0)
            tmp = tmp - 1

    else:
        if (len(listOfInts1) % 2) != 0:
            listOfInts1.insert(0, 0)
            listOfInts2.insert(0, 0)

    return listOfInts1, listOfInts2



def cutLeadingZeroes(list):
    zChecker = 0
    i = 0
    while i < len(list)-2 and zChecker == 0:
        if int(list[i]) == 0:
            list.pop(0)
        else:
            zChecker = 1
        i = i+1

    return list


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

    if len(tmp) > 1:
        tmp = cutLeadingZeroes(tmp)
    return tmp



def subLists(list1, list2):
    tmp = []
    carry = 0

    if (len(list1) > 1) or (len(list2) > 1):
        list1, list2 = preProcessLists(list1, list2)

    i = (len(list1)-1)

    while i > 0:
        if (int(list1[i]) - int(list2[i])) < 0:
            tmp.insert(0, ((10+int(list1[i])) - carry - int(list2[i])))
            carry = 1
        else:
            tmp.insert(0, (int(list1[i]) - carry - int(list2[i])))
            carry = 0
        i = i-1

    tmp.insert(0, int(list1[i]) - carry - int(list2[i]))

    if len(tmp) > 1:
        tmp = cutLeadingZeroes(tmp)

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

        karat3 = karatsuba(fHalf, sHalf)

        new1, new2 = firstListGreaterValue(karat3, c2)
        #new1, new2 = karat3, c2
        c1 = subLists(new1, new2)

        new3, new4 = firstListGreaterValue(c1, c0)
        #new3, new4 = c1, c0
        c1 = subLists(new3, new4)

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
        result = cutLeadingZeroes(result)
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
            print(listToString(result))

        if userChoice == 2:
            base = int(input("Enter number to exponentiate: "))
            exponent = int(input("Enter the exponent as an integer: "))
            baseList = convertIntToList(base)
            result = baseList
            if exponent == 1:
                result = baseList
            elif exponent == 0:
                result = 1
            else:
                result = baseList
                for i in range (1, exponent):
                    result = karatsuba(result, baseList)
            print (listToString(result))






main()