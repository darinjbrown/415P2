'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''


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


    #karatsuba(listOfInts1, listOfInts2)

#splits a list of even size in half and returns the two lists
def splitList(listofInts):
    half = len(listofInts)//2
    return listofInts[:half], listofInts[half:]




def addLists(l1First, l2First, l1Second, l2Second):
    z0 = []
    z1 = []

    carry1 = 0
    carry2 = 0

    for i in range(len(l2First), 1):
        if l1First[i] + l2First[i] + carry1 > 9:
            z0.insert(0, 0)
            carry1 = 1
        else:
            z0.insert(l1First[i] + l2First[i] + carry1)
            carry1 = 0

        if l1Second[i] + l2Second[i] + carry2 > 9:
            z1.insert(0, 0)
            carry2 = 1
        else:
            z1.insert(l1Second[i] + l2Second[i] + carry2)
            carry2 = 0

    return z0, z1



def subLists(z0, z1):
    tmp = []

    for i in range(len(z0), 1):
        if z0[i] - z1[i] < 0:
            z0[i-1] = z0[i-1] - 1
            tmp.insert(int(str(1) + str(z1[i])) - z1[i])
        else:
            tmp.insert(z0[i] - z1[i])

    return tmp



def karatsuba(listOfInts1, listOfInts2):
    if (len(listOfInts1) == 1 or len(listOfInts2) == 1):
        return listOfInts1[0]*listOfInts2[0]
    else:
        num = len(listOfInts1)/2

        l1First, l1Second = splitList(listOfInts1)
        l2First, l2Second = splitList(listOfInts2)

        c2 = karatsuba(l1First, l2First)
        c0 = karatsuba(l2First, l2Second)

        z0, z1 = addLists(l1First, l2First, l1Second, l2Second)
        z2 = subLists(z0, z1)

        c1 = subLists(karatsuba(z0, z1), z2)

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
            preProcessLists(list1, list2)
            result = karatsuba(list1, list2)
            print(result)



main()