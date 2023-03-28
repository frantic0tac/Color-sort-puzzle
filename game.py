import random
import sys

b1 = []
b2 = []
b3 = []
b4 = []
b5 = []

colors = ["red", "yel", "blu", "gre"]
tubes = {"1": b1, '2': b2, '3': b3, '4': b4, "5": b5}


def fill_bottles():
    red_c = 0
    yel_c = 0
    blu_c = 0
    gre_c = 0
    for bot in ([b1, b2, b3, b4]):
        for layer in range(0, 4):
            while True:
                choice = random.choice(colors)
                if choice == "red" and red_c == 4:
                    continue
                if choice == "yel" and yel_c == 4:
                    continue
                if choice == "blu" and blu_c == 4:
                    continue
                if choice == "gre" and gre_c == 4:
                    continue

                if choice == "red":
                    red_c += 1
                elif choice == "yel":
                    yel_c += 1
                elif choice == "blu":
                    blu_c += 1
                elif choice == "gre":
                    gre_c += 1
                bot.append(choice)
                break


def show_bottles():
    b10 = ['', '', '', '', ]
    b20 = ['', '', '', '', ]
    b30 = ['', '', '', '', ]
    b40 = ['', '', '', '', ]
    b50 = ['', '', '', '', ]

    l1 = len(b1)
    if l1 == 0:
        for layer in range(0, 4):
            b10[layer] = "   "
    elif l1 in range(1, 4):
        for layer in range(0, l1):
            b10[layer] = b1[layer]
        for layer in range(l1, 4):
            b10[layer] = "   "
    elif l1 == 4:
        for layer in range(0, 4):
            b10[layer] = b1[layer]

    l2 = len(b2)
    if l2 == 0:
        for layer in range(0, 4):
            b20[layer] = "   "
    elif l2 in range(1, 4):
        for layer in range(0, l2):
            b20[layer] = b2[layer]
        for layer in range(l2, 4):
            b20[layer] = "   "
    elif l2 == 4:
        for layer in range(0, 4):
            b20[layer] = b2[layer]

    l3 = len(b3)
    if l3 == 0:
        for layer in range(0, 4):
            b30[layer] = "   "
    elif l3 in range(1, 4):
        for layer in range(0, l3):
            b30[layer] = b3[layer]
        for layer in range(l3, 4):
            b30[layer] = "   "
    elif l3 == 4:
        for layer in range(0, 4):
            b30[layer] = b3[layer]

    l4 = len(b4)
    if l4 == 0:
        for layer in range(0, 4):
            b40[layer] = "   "
    elif l4 in range(1, 4):
        for layer in range(0, l4):
            b40[layer] = b4[layer]
        for layer in range(l4, 4):
            b40[layer] = "   "
    elif l4 == 4:
        for layer in range(0, 4):
            b40[layer] = b4[layer]

    l5 = len(b5)
    if l5 == 0:
        for layer in range(0, 4):
            b50[layer] = "   "
    elif l5 in range(1, 4):
        for layer in range(0, l5):
            b50[layer] = b5[layer]
        for layer in range(l5, 4):
            b50[layer] = "   "
    elif l5 == 4:
        for layer in range(0, 4):
            b50[layer] = b5[layer]

    print(f"\n|   | |   | |   | |   | |   |")
    print(f"|{b10[3]}| |{b20[3]}| |{b30[3]}| |{b40[3]}| |{b50[3]}|")
    print(f"|{b10[2]}| |{b20[2]}| |{b30[2]}| |{b40[2]}| |{b50[2]}|")
    print(f"|{b10[1]}| |{b20[1]}| |{b30[1]}| |{b40[1]}| |{b50[1]}|")
    print(f"|{b10[0]}| |{b20[0]}| |{b30[0]}| |{b40[0]}| |{b50[0]}|")
    print(f"\_1_/ \_2_/ \_3_/ \_4_/ \_5_/")
    print("__________________________________________________________")


def player_move():
    while True:
        while True:
            print("Please choose test tube to pour from or press 'Q' to exit.")
            from_bot = input("< ")
            if from_bot.isdigit() == False or int(from_bot) not in range(1, 6):
                print("Please choose number from 1 to 5.", end="")
                continue
            elif from_bot.lower() == "q":
                sys.exit()

            from_bot = tubes[from_bot]
            break

        while True:
            print("Please choose test tube to pour into or press 'Q' to exit.")
            to_bot = input("< ")

            if int(to_bot) not in range(1, 6):
                print("Please choose number from 1 to 5.", end="")
                continue
            elif to_bot == from_bot:
                print("You can't choose the same test tube twice.", end="")
                continue
            elif to_bot.lower() == "q":
                sys.exit()
            to_bot = tubes[to_bot]
            break
        if len(to_bot) == 0 or (to_bot[-1] == from_bot[-1] and len(to_bot) <= 3):
            trans = from_bot.pop(-1)
            to_bot.append(trans)
            break
        else:
            print("You cant make such action.")
            continue


def check_score():
    b10 = ['', '', '', '', ]
    b20 = ['', '', '', '', ]
    b30 = ['', '', '', '', ]
    b40 = ['', '', '', '', ]
    b50 = ['', '', '', '', ]

    l1 = len(b1)
    if l1 == 0:
        for layer in range(0, 4):
            b10[layer] = "   "
    elif l1 in range(1, 4):
        for layer in range(0, l1):
            b10[layer] = b1[layer]
        for layer in range(l1, 4):
            b10[layer] = "   "
    elif l1 == 4:
        for layer in range(0, 4):
            b10[layer] = b1[layer]

    l2 = len(b2)
    if l2 == 0:
        for layer in range(0, 4):
            b20[layer] = "   "
    elif l2 in range(1, 4):
        for layer in range(0, l2):
            b20[layer] = b2[layer]
        for layer in range(l2, 4):
            b20[layer] = "   "
    elif l2 == 4:
        for layer in range(0, 4):
            b20[layer] = b2[layer]

    l3 = len(b3)
    if l3 == 0:
        for layer in range(0, 4):
            b30[layer] = "   "
    elif l3 in range(1, 4):
        for layer in range(0, l3):
            b30[layer] = b3[layer]
        for layer in range(l3, 4):
            b30[layer] = "   "
    elif l3 == 4:
        for layer in range(0, 4):
            b30[layer] = b3[layer]

    l4 = len(b4)
    if l4 == 0:
        for layer in range(0, 4):
            b40[layer] = "   "
    elif l4 in range(1, 4):
        for layer in range(0, l4):
            b40[layer] = b4[layer]
        for layer in range(l4, 4):
            b40[layer] = "   "
    elif l4 == 4:
        for layer in range(0, 4):
            b40[layer] = b4[layer]

    l5 = len(b5)
    if l5 == 0:
        for layer in range(0, 4):
            b50[layer] = "   "
    elif l5 in range(1, 4):
        for layer in range(0, l5):
            b50[layer] = b5[layer]
        for layer in range(l5, 4):
            b50[layer] = "   "
    elif l5 == 4:
        for layer in range(0, 4):
            b50[layer] = b5[layer]

    full = 0
    for bot in (b10, b20, b30, b40, b50):
        all = bot[0] + bot[1] + bot[2] + bot[3]
        if all in ("redredredred", "yelyelyelyel", "blublublublu", "gregregregre"):
            full += 1

    if full == 4:
        return "win"

    count = 0

    for f in [b1]:
        for s in [b2, b3, b4, b5]:
            if f[-1] == s[-1]:
                count += 1
    for f in [b2]:
        for s in [b3, b4, b5]:
            if f[-1] == s[-1]:
                count += 1
    for f in [b3]:
        for s in [b4, b5]:
            if f[-1] == s[-1]:
                count += 1
    for f in [b4]:
        for s in [b5]:
            if f[-1] == s[-1]:
                count += 1

    print(count)
    if count == 1:
        for f in (b1, b2, b3, b4):
            for s in (b2, b3, b4, b5):
                if f[-1] == s[-1] and f != s:
                    if len(f) > len(s):
                        if s[len(s) - 1] == f[len(s) - 1] and len(s) - 1 > 0:
                            return "tie"
                    elif len(s) > len(f):
                        if s[len(f) - 1] == f[len(f) - 1] and len(f) - 1 > 0:
                            return "tie"
                    elif len(s) == len(f) and len(s) == 4:
                        return "tie"

    count = 0

    return "continue"


# Game starts here
fill_bottles()
show_bottles()

while True:  # Game main loop
    player_move()
    show_bottles()
    result = check_score()
    if result == "win":
        print("You won! Congrats!")
        break
    elif result == "tie":
        print("No more moves! it's tie!")
        break
