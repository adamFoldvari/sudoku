def menu():
    # ask the for a difficulty level, if a good input is given, return an integer stored in a variable
    print("\033c")
    print('       RANDOM SUDOKU GAME V2.© 2017 \n Developers: Ádám Földvári and Dávid Tanács \nChoose difficulty:')
    lvl_choice = 0
    while lvl_choice == 0:
        try:
            lvl_choice = int(input(' 1.Hard \n 2.Medium \n 3.Easy \n 4.Begginer \nEnter the difficulty number here:'))
            if lvl_choice == 1:
                difficulty = 9
            elif lvl_choice == 2:
                difficulty = 6
            elif lvl_choice == 3:
                difficulty = 4
            elif lvl_choice == 4:
                difficulty = 3
            else:
                print("\033c")
                print('Please choose the number of the difficulty level!')
                lvl_choice = 0
        except ValueError:
            print("\033c")
            print('Please choose the number of the difficulty level!')
            lvl_choice = 0
    return difficulty
