'''
Darin Brown and Skyler Penna
CS415 Project 2
Dr. Gurman Gill, Sonoma State Univrsity
This program represents very long (up to 1000 digits) integers as
lists and multiplies and exponentiates them

'''


def convertIntToList(integer):
    intList = [int(i) for i in str(integer)]
    return list

def preProcessLists(listOfInts1, listOfInts2):
    #make the larger of the two lists even then make the
    #smaller list of equal size
    if len(listOfInts1) > len(listOfInts2):
        if len(listOfInts1) % 2 != 0:
            listOfInts1.insert(0)
        tmp = len(listOfInts1) - len(listOfInts2)
        for i in range(1, tmp):
            listOfInts2.insert(0)
    else:
        if len(listOfInts2) % 2 != 0:
            listOfInts2. insert(0)
        tmp = len(listOfInts2) - len(listOfInts1)
        for i in range(1, tmp):
            listOfInts1.insert(0)


    #karatsuba(listOfInts1, listOfInts2)


def karatsuba(listOfInts1, listOfInts2):
    if len(listOfInts1) == 1 or len(listOfInts2) == 1:
        return listOfInts1*listOfInts2
    else:
        num = max(len(listOfInts1), len(listOfInts2))



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
                print(karatsuba(list1, list2))



main()