'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''

def firstListGreaterValue(list1, list2):
    #input 2 lists
    #after running function return greater then lesser

    #determine number of leading 0's in each list
    leadingList1 = 0
    leadingList2 = 0
    for i in len(list1):
        if list1[i] == '0':
            leadingList1 += 1
        else:
            break
    for i in len(list2):
        if list2[i] == '0':
            leadingList2 += 1
        else:
            break

    # return the longer list
    if (len(list1) - leadingList1) > (len(list2) - leadingList2):
        return list1, list2
    if (len(list2) - leadingList2) > (len(list1) - leadingList1):
        return list2, list1

    # lengths are equal, so check each digit to find the greater
    for i in (len(list1)):
        if int(list1[i]) > int(list2[i]):
            return list1, list2

    # list2 is greater, so swap
    return list2, list1



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

    if any(neg < 0 for neg in tmp):
        i = 0
        while i < len(tmp)-1:
            if tmp[i] < 0:
                tmp[i] = int(tmp[i])*-1
            i = i+1

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

        c1 = subLists(karat3, c2)

        c1 = subLists(c1, c0)

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