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


def multiplyDigit(int1, int2):
    answer = 0
    # do something
    return answer



def multiplyList(listOfInts1, listOfInts2):
    answer = []
    #do something
    return answer





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
                multiply


main()