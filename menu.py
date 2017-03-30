def menu():
    print('       RANDOM SUDOKU GAME V2.© 2017 \n Developers: Ádám Földvári and Dávid Tanács \nChoose difficulty:')
    lvl_choice = int(input(' 1.Hard \n 2.Medium \n 3.Easy \n 4.Begginer \nEnter the difficulty number here:'))
    if lvl_choice == 1:
        difficulty = 9
    elif lvl_choice == 2:
        difficulty = 6
    elif lvl_choice == 3:
        difficulty = 4
    elif lvl_choice == 4:
        difficulty = 3
    return difficulty
