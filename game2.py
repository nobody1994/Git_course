# Check if three numbers adds up to 15
def check_winner(picked_numbers):
    for i in range(len(picked_numbers)):
        for j in range(i + 1, len(picked_numbers)):
            for k in range(j + 1, len(picked_numbers)):
                if picked_numbers[i] + picked_numbers[j] + picked_numbers[k] == 15:
                    return True
    return False


#welcome message and game definition
print("Number scrabble is played with the list of numbers between 1 and 9.")
print("Each player takes turns picking a number from the list.")
print("Once a number has been picked, it cannot be picked again.")
print("If a player has picked three numbers that add up to 15, that player wins the game.")
print("However, if all the numbers are used and no player gets exactly 15, the game is a draw.\n")

#declare a list of availabe numbers
MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#make two list to store the picked numbers from two players
player_one_nums = []
player_two_nums = []

#make a while loop until MyList is empty
while MyList:
    # get a number from player one
    number_one = input("Player one, please enter a valid number : ")
    while True:
        if not all (char in "123456789" for char in str(number_one)):
            number_one = input("Player one, please enter a number : ")
        else:
            number_one = int(number_one)
            break
    #check if the number still in MyList
    if number_one in MyList:
        #delete the picked number avioding the repeated numbers
        MyList.remove(number_one)
        #add the picked numbers from player oe to a list
        player_one_nums.append(number_one)
        #check if 3 numbers or more are picked from player one and if there sum is 15
        if len(player_one_nums) >= 3 and check_winner(player_one_nums):
            print("player one wins\n")
            break

        #check if MyList is empty
        if not MyList:
            print("the game is a draw")
        else:
            #get a number from player two
            number_two = input("Player two, please enter a valid number : ")
            while True:
                if not all(char in "123456789" for char in str(number_two)):
                    number_two = input("Player two, please enter a number : ")
                else:
                    number_two = int(number_two)
                    break
            if number_two in MyList:
                MyList.remove(number_two)
                player_two_nums.append(number_two)
                if len(player_two_nums) >= 3 and check_winner(player_two_nums):
                    print("player two wins\n")
                    break
                if not MyList:
                    print("the game is a draw")

            else:
                print("invalid number , please try again ")
                number_two = int(input("Player two, Please enter a number : "))

    else:
        print("Invalid number , please try again ")

print("player one numbers is : ", player_one_nums)
print("player two numbers is : ", player_two_nums)