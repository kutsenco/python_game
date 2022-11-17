"""
Welcome to my game
"""

def restart_mission_1() :

    """
    This function gives the player a choice - to start the game again or the first mission again
    """

    print("You can start the game over (y)...")

    print("You can end the game (n)...")

    enter_1 = input(">>> ")

    if enter_1 == 'y' or enter_1 == 'yes' :
        main()

    elif enter_1 == 'n' or enter_1 == 'no' :
        print("You have made your choice...")
        print("See you another time...")
        exit()

def restart_mission_2() :

    """
    This function gives the player a choice - to start the game again or the second mission again
    """

    print("You can start the game over (y)...")

    print("You can end the game (n)...")

    enter_2 = input(">>> ")

    if enter_2 == 'y' or enter_2 == 'yes' :
        main()

    elif enter_2 == 'n' or enter_2 == 'no' :
        print("You have made your choice...")
        print("See you another time...")
        exit()
    else :
        print("Your data type is not valid...")
        print("That's why you lost...")
        exit()

def restart_mission_3() :

    """
    This function gives the player a choice - to start the game again or the third mission again
    """

    print("You can start the game over (y)...")

    print("You can end the game (n)...")

    enter_3 = input(">>> ")

    if enter_3 == 'y' or enter_3 == 'yes' :
        main()

    elif enter_3 == 'n' or enter_3 == 'no' :
        print("You have made your choice...")
        print("See you another time...")
        exit()
    else :
        print("Your data type is not valid...")
        print("That's why you lost...")
        exit()

def main() :

    """
    the key mission through which all this happens
    """

    print("""
        During the entire existence of the planet Ene,
        it is surrounded and destroyed by biting monsters
    """)

    print("They destroyed all the living things that were on this planet")
    print("However, one day, as a result of crossbreeding two monsters, a unique appeared... ")
    print("This is the main character who should free E from all monsters... ", end='\n\n')

    print("""
        You also have the right to familiarize yourself with the rules of the game on the author's website, the link to which is placed below...
    """, end='\n\n')

    print("https://fron-end.github.io/game/", end='\n\n')

    print("""
        If you don't have internet, choose You can view the game description when entering (yes/no)... 
    """, end='\n\n')

    description = input(">>> ")

    if description == 'yes' or description == 'y' :
        print("Description of the game: ", end='\n\n')

        print("""
            The game begins with the fact that you have to save the world from biting monsters. There are three stages of the game: 
        """, end='\n\n')

        print("1. Easy (City)")
        print("2. Hard (Mountains)")
        print("3. Very hard (Cosmos)", end='\n\n')

        print("""
            Monsters have completely taken over this world, so you need to act quickly to save all living things...
        """, end='\n\n')

        print("""
            The development of events and the level of difficulty will depend on the choice of location, so pay attention to this...
        """, end='\n\n')

        print("""
            The first mission begins in the 'city' location... This is the easiest progression in this game...
        """, end='\n\n')

        print("""
            You have chosen the second branch of development in this game, it takes place in the mountain location. In this location, the monsters are hiding in the mountains...
        """, end='\n\n')

        print("Mission_3 consists of two stages...", end='\n\n')

        print("""
            the first: in order to survive in space, you need to know a chemical element, without which you cannot destroy the monsters in this location... 
        """, end='\n')

        print("""
            At the second stage of the space location, you will need to know the bitwise representation of some numbers... 
        """, end='\n')

        print("""
            In this way and with the help of a chemical element, it will be possible to destroy them... 
        """, end='\n\n')

        print("""
            In my project, I used the following functions: main(), mission_1(), mission_2(), mission_3() to structure my game and make it more understandable for the successors!!!
        """, end='\n\n')

        print("""
            Also used the time module to make the game more interesting and intriguing!!!
        """, end='\n\n')

        print("I will be grateful to everyone who visits this game... ", end='\n\n')

    elif description == 'no' or description == 'n' :
        print("Then let's go straight to the game... ")
    else :
        print("Try again... ", end='\n\n')
        main()

    yes = "y"
    no_is_no = "n"
    print("Do you want to start the game? (n/y): ")
    choice = input(">>> ")

    if choice == yes :
        print("To date, the world has been taken over by battle monsters", end='\n\n')

        print("In addition to the serial number, each monster has: 1, 4,...", end='\n\n')

        print("""
            there is also a bitwise view of the number data: '0bd1011', '0b10110', ...
        """, end='\n\n')

        print("For example: 1('0b1'), 4('0b100'), 7('0b111'), 9('0b1001'), ...", end='\n\n')

        print("How to address you, hero...", end='\n\n')

        name = input(">>> ")

        print("It is being processed...", end='\n\n')

        print("Congratulations, ", name, ", today is day X.", end='\n\n')

        print("Mathematics, and knowing the basics of programming will save the world!!!")

        print("""
            Choose one location where you will implement your plan to save the whole world from evil monsters (1, 2, 3): 
        """, end='\n\n')

        print("1. city")
        print("2. mountains")
        print("3. space")

        location = input(">>> ")

        print("It is being processed... ", end='\n\n')

        def mission_1() :
            if location == '1' :
                print("---------------------------Mission_1---------------------------", end='\n\n')

                print("The city has the most monsters, they are everywhere", end='\n\n')

                print("Something needs to be done about it ...", end='\n\n')

                print("Let's see what's in the inventory(n/y): ", end='\n\n')

                inventory = input(">>> ")

                if inventory == 'y' :
                    arr = [
                        "1. Pistol (10 cartridges)", "| "
                        "2. Carbon dioxide", "| "
                        "3. 1 liter of gasoline", "| "
                        "4. Lighter"
                    ]

                    print(*arr)

                    print("The monsters are coming!!!", end='\n\n')

                    print("We need to decide how we will destroy the monsters: ", end='\n\n')

                    print("1. Pistol (10 cartridges) | ", end='\n\n')
                    print("2. 1 liter of gasoline + lighter | ", end='\n\n')
                    print("3. Carbon dioxide", end='\n\n')

                    print("Choose death for a biting monster (1, 2, 3): ", end='\n\n')

                    died = input(">>> ")

                    if died == '1' :
                        print("You shot the monster through! You won!!!", end='\n\n')

                        print("I'm looking for a token...", end='\n\n')

                        print("Yes... Fund it!", end='\n\n')

                        print(name, "congratulations on winning!!!", end='\n\n')

                    elif died == '2' :
                        print("Mon burned alive! Great work! and out!!!", end='\n\n')

                        print("I'm looking for a token ...", end='\n\n')

                        print("Yes... Found it!", end='\n\n')

                        print(name, "congratulations on winning!!!", end='\n\n')

                    elif died == '3' :
                        print("""
                            You fired a monster with the help of a chemical reaction!!! You won!!!
                        """, end='\n\n')

                        print("Looking for a token...", end='\n\n')

                        print("Yes... Found it!", end='\n\n')

                        print(name, "congratulations on winning!!!", end='\n\n')

                    else :
                        print("""
                            You need to choose an action that will destroy the monster ...
                        """, end='\n\n')
                        print("You never made up your mind, so the monster killed you...")

                        restart_mission_1()

                elif inventory == 'n' :
                    print("You have no inventory, so you were killed ... ", end='\n\n')

                    restart_mission_1()

                else :
                    print("You didn't have time to choose a way to destroy monsters...")
                    print("That's why these scum destroyed you")

                    restart_mission_1()

            elif location != '1' and location != '2' and location != '3' :
                print("Such a location does not exist... ")
                print("You have been thrown out of time space...")

                restart_mission_1()

        mission_1()

        def mission_2() :
            if location == '2' :
                print("--------------------------Mission_2--------------------------", end='\n\n')

                print("""
                    In the mountains, monsters have created their caves, so at this stage you will need to know the bitwise representation of various numbers ...
                """, end='\n\n')

                print("""
                    Enter the number 3 to find out the bitmap of the three monsters that are in the cave ... 
                """, end='\n\n')

                enter_number_3 = int(input(">>> "))

                if enter_number_3 == 3 :

                    i = 0

                    relevant = 0

                    while i < 3 :
                        k = enter_number_3 + relevant
                        print(i + 1, [*bin(k)])
                        i += 1
                        relevant += 1
                    print()

                    print("""
                        Please select the number of the monster you would like to destroy (1, 2, 3)...
                    """, end='\n\n')

                    over = input(">>> ")

                    if over == '1' :
                        arr = [*bin(k)]
                        result_1 = arr.count('1')

                        print("Enter the number of T values... ", end='\n\n')

                        result_1 = input(">>> ")

                        print("It is being processed: ", end='\n\n')

                        if result_1 == '2' :
                            print("You killed the monster ...", end='\n\n')

                            print("I'm looking for a token ...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')
                        else :
                            print("Your answer is not correct...")
                            print("The monster killed you ...", end='\n\n')

                            restart_mission_2()

                    elif over == '2' :
                        arr_1 = [*bin(k)]
                        result_2 = arr_1.count('1')

                        print("Enter the number of T values... ", end='\n\n')

                        result_2 = input(">>> ")

                        print("It is being processed ...", end='\n\n')

                        if result_2 == '1' :
                            print("You killed the monster...", end='\n\n')

                            print("I'm looking for a token ...", end='\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')
                        else :
                            print("Your answer is not correct...")
                            print("The monster killed you ...", end='\n\n')

                            restart_mission_2()

                    elif over == '3' :
                        arr_2 = [*bin(k)]
                        result_3 = arr_2.count('1')

                        print("Enter the number of T values... ", end='\n\n')

                        result_3 = input(">>> ")

                        print("It is being processed ...", end='\n\n')

                        if result_3 == '2' :
                            print("You killed the monster...", end='\n\n')

                            print("I'm looking for a token ...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')
                        else :
                            print("Your answer is not correct...")
                            print("The monster killed you...", end='\n\n')

                            restart_mission_2()

                    else :
                        print("You're trying to kill a monster that doesn't exist... ")
                        print("The monsters overtook you and tore you to pieces...")
                        print("you lost...")

                        restart_mission_2()

                elif enter_number_3 == (arr(2)) :
                    print("You entered the wrong value, so the monsters ate you...")

                    restart_mission_2()

                else :
                    print("""
                        You lost because the battle monsters were exactly in the 3rd cave ... 
                    """, end='\n\n')

                    restart_mission_2()

            elif location != '1' and location != '2' and location != '3' :
                print("Such a location does not exist... ", end='\n\n')

                restart_mission_2()

        mission_2()

        def mission_3() :
            if location == '3' :
                print("-------------------------Mission_3-------------------------", end='\n\n')

                print("Welcome to space... ", end='\n\n')

                print("""
                    In order to fight monsters in space, you need to know the Un formula
                """, end='\n\n')
                print("""
                    ((V is an uppercase letter, v is a lowercase letter) <-- it has the form (Vvv) -->)
                """, end='\n\n')

                element = input(">>> ")

                if element == 'Unp' or element == 'unp' or element == 'UNP' :
                    print("""
                        Perfectly!!! Now you are ready to fight monsters to the fullest...
                    """, end='\n\n')

                    i = 0

                    number_monster = 'monster'

                    while i < 4 :
                        long_monster = 2 * (i + 3)

                        print(long_monster, number_monster)
                        i += 1

                    print("Choose a monster to destroy(6, 8, 10, 12): ", end='\n\n')

                    result = input(">>> ")

                    if result == '6' :
                        print("""
                            To destroy a monster, you need to write down the bitwise representation of the number (without '0b') under which it is located and which you have chosen... 
                        """, end='\n\n')

                        result_1 = input(">>> ")

                        if result_1 == '110' :

                            print("You killed the monster ...", end='\n\n')

                            print("I'm looking for a token ...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')

                        elif result_1 == '0b110' :
                            print("""
                                You didn't read the game rules carefully (you must enter the bitwise form of the number without '0b'...)
                            """, end='\n\n')

                            print("Because of your inattention, the monsters destroyed you...")

                            restart_mission_3()

                        else :
                            print("Data entry is not correct...", end='\n\n')

                            restart_mission_3()

                    elif result == '8' :
                        print("""
                            To destroy a monster, you need to write down the bitwise representation of the number (without '0b') under which it is located and which you have chosen... 
                        """, end='\n\n')

                        result_1 = input(">>> ")

                        if result_1 == '1000' :

                            print("You killed the monster ...", end='\n\n')

                            print("I'm looking for a token ...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')

                        elif result_1 == '0b110' :
                            print("""
                                You did not carefully read the rules of the game (you must enter the bitwise form of the number without '0b'...)
                            """, end='\n\n')

                            print("Because of your inattention, the monsters destroyed you...")

                            restart_mission_3()

                        else :
                            print("Data entry is not correct...", end='\n\n')

                            restart_mission_3()

                    elif result == '10' :
                        print("""
                            To destroy a monster, you need to write down the bitwise representation of the number (without '0b') under which it is located and which you have chosen... 
                        """, end='\n\n')

                        result_1 = input(">>> ")

                        if result_1 == '1010' :

                            print("You killed the monster...", end='\n\n')

                            print("I'm looking for a token...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')

                        elif result_1 == '0b110' :
                            print("""
                                You did not carefully read the rules of the game (you must enter the bitwise form of the number without '0b'...)
                            """, end='\n\n')

                            print("Because of your inattention, the monsters destroyed you...")

                            restart_mission_3()

                        else :
                            print("Data entry is not correct...", end='\n\n')

                            restart_mission_3()

                    elif result == '12' :
                        print("""
                            To destroy a monster, you need to write down the bitwise representation of the number (without '0b') under which it is located and which you have chosen... 
                        """, end='\n\n')

                        result_1 = input(">>> ")

                        if result_1 == '1100' :

                            print("You killed the monster...", end='\n\n')

                            print("I'm looking for a token ...", end='\n\n')

                            print("Yes... Found it!", end='\n\n')

                            print(name, "congratulations on winning!!!", end='\n\n')

                        elif result_1 == '0b110' :
                            print("""
                                You did not carefully read the rules of the game (you must enter the bitwise form of the number without '0b'...)
                            """, end='\n\n')

                            print("Because of your inattention, the monsters destroyed you...")

                            restart_mission_3()

                        else :
                            print("""
                                Unfortunately, the answer is not correct... You lost... 
                            """, end='\n\n')

                            restart_mission_3()

                    else :
                        print("Un exploded in your hands... ", end='\n\n')

                        restart_mission_3()

                else :
                    print("Unfortunately, this answer is incorrect... You lose...", end='\n\n')

                    restart_mission_3()

            elif location != '1' and location != '2' and location != '3' :
                print("Such a location does not exist... ")

                restart_mission_3()

        mission_3()

    elif choice == no_is_no :
        print("Let's play then another time ...", end='\n\n')
    else :
        print("You need to enter one of the following options: (n) or (y)", end='\n\n')

main()
