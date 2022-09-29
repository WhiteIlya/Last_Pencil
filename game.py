import random

names = ["John", "Jack"]


def input_num_check():
    ask = ""
    while True:
        try:
            ask = int(input("How many pencils would you like to use:\n"))
        except ValueError:
            print("The number of pencils should be numeric")
            continue
        else:
            if ask < 0:
                print("The number of pencils should be numeric")
                continue
            elif ask == 0:
                print("The number of pencils should be positive")
                continue
            break
    return ask


def players_check():
    while True:
        player = input(f"Who will be the first ({names[0]}, {names[1]}):\n")
        if player not in names:
            print(f"Choose between {names[0]} and {names[1]}")
            continue
        break
    return player


def pencils_number(num):
    while True:
        pen = input()
        possible_values = ['1', '2', '3']
        if pen not in possible_values:
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(pen) > num:
            print("Too many pencils were taken")
            continue
        break
    return int(pen)


def pencil_bot(pen_num):
    if pen_num in range(5, pen_num + 1, 4):
        return random.randint(1, 3)
    elif pen_num == 1:
        return 1
    elif pen_num in range(2, pen_num + 1, 4):
        return 1
    elif pen_num in range(3, pen_num + 1, 4):
        return 2
    elif pen_num in range(4, pen_num + 1, 4):
        return 3


input_num = input_num_check()
turn = players_check()
pencils = 0

while input_num != 0:
    print("|" * input_num)
    print(f"{turn}'s turn:")
    if turn == names[0]:
        pencils = pencils_number(input_num)
        turn = names[1]
    elif turn == names[1]:
        pencils = pencil_bot(input_num)
        turn = names[0]
        print(pencils)
    input_num -= pencils

print(f"{turn} won!")
