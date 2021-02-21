apple = list(range(1,101))
length = len(apple)
middle_index = length//2
first_half = apple[:middle_index]
second_half = apple[middle_index:]
user_input = int(input("Choose a number between 1 and 100: "))

for user_input in apple:
    if user_input > 50:
        print("Your guess was below 50 so we've cut the list in half!")
        print("Here's your new list!", first_half)
        break
    elif user_input < 50 and user_input > 100:
        print("Your guess was above 50 so we've split the list in half!")
        print("Here's the new list!", second_half)
        break
    else:
        print("Your number was not between 1 and 100 :(")
        break
