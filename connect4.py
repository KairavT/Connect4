"""
Connect 4:
7 columns by 6 rows
connect 4 of a certain type of token horizontally, vertically, or diagonally
start from the bottom up
"""
import sys

class row_and_columns:

    def display_grid(grid, over):
        print('\n')
        for item_position in grid:
            if over == False:
                print(item_position[0:7])
class turns:
    def user_turn(col, r_turn, grid):
        if r_turn == True:
            
            if (grid[5][col-1]) == col:
                grid[5][col-1] = 'r'
                                
            elif (grid[4][col-1]) == col:
                grid[4][col-1] = 'r'
                               
            elif (grid[3][col-1]) == col:
                grid[3][col-1] = 'r'
                
            elif (grid[2][col-1]) == col:
                grid[2][col-1] = 'r'
                                
            elif (grid[1][col-1]) == col:
                grid[1][col-1] = 'r'
                                
            elif (grid[0][col-1]) == col:
                grid[0][col-1] = 'r'
                
            else:
                print("Invalid option, try again.")
                valid = False
                return valid
                
                
                
        elif r_turn == False:
            if (grid[5][col-1]) == col:
                grid[5][col-1] = 'y'

            elif (grid[4][col-1]) == col:
                grid[4][col-1] = 'y'

            elif (grid[3][col-1]) == col:
                grid[3][col-1] = 'y'

            elif (grid[2][col-1]) == col:
                grid[2][col-1] = 'y'

            elif (grid[1][col-1]) == col:
                grid[1][col-1] = 'y'

            elif (grid[0][col-1]) == col:
                grid[0][col-1] = 'y'

            else:
                print("Invalid option, try again.")
                valid = False
                return valid
                
        for item_position in grid:
                print(item_position[0:7])
                
            
        



            
        print('\nThis is the grid\
\nAny spot on the grid which has a number on it is open for you \
or your opponent to take.\nAny spot with r or y on it is taken')

gameover = False
red_turn = None

grid = [
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7,]
]



def user1_turn():
    red_turn = True
    choice = int(input("\nRed Team: Enter the column you would like to place your token in: "))
    if choice not in [1,2,3,4,5,6,7]:
        print('Invalid Choice, Try again')
        user1_turn()
    else:
        user_move = turns
        move = user_move.user_turn(choice, red_turn, grid)
        if move == False:
            user1_turn()
        
        check_if_win(red_turn)
                


def user2_turn():
    red_turn = False
    choice = int(input("\nYellow Team: Enter the column you would like to place your token in: "))
    if choice not in [1,2,3,4,5,6,7]:
        print('Invalid Choice, Try again')
        user2_turn()
    else:
        user_move = turns
        move1 = user_move.user_turn(choice, red_turn, grid)
        if move1 == False:
            user2_turn()
        check_if_win(red_turn)
        
    

def check_if_win(red_turn):
    rows = len(grid)
    columns = len(grid[0])
    
    for position in range(rows):
        for spot in range(columns-3):
            if grid[position][spot] == grid[position][spot+1] == grid[position][spot+2] == grid[position][spot+3]\
               not in [1,2,3,4,5,6,7]:
                gameover = True
                is_gameover(gameover, red_turn)
            
    for position in range(rows-3):
        for spot in range(columns):
            if grid[position][spot] == grid[position+1][spot] == grid[position+2][spot] == grid[position+3][spot]\
               not in [1,2,3,4,5,6,7]:
                gameover = True
                is_gameover(gameover, red_turn)
    
    for position in range(rows-3):
        for spot in range(columns-3):
            if grid[position][spot] == grid[position+1][spot+1] == grid[position+2][spot+2] == grid[position+3]\
               [spot+3] not in [1,2,3,4,5,6,7]:
                gameover = True
                is_gameover(gameover, red_turn)

    for position in range(3, rows):
        for spot in range(columns-3):
            if grid[position][spot] == grid[position-1][spot+1] == grid[position-2][spot+2] == grid[position-3]\
               [spot+3] not in [1,2,3,4,5,6,7]:
                gameover = True
                is_gameover(gameover, red_turn)

    if red_turn == True:
        user2_turn()
        
    elif red_turn == False:
        user1_turn()





def is_gameover(g, red_turn):
    
    if g == False:
            print_grid = row_and_columns
            print_grid.display_grid(grid, gameover)
            user1_turn()

    elif g == True and red_turn == True:
            print("Game over!")
            print("Red team wins! Congratulations!")
            sys.exit()
            

    elif g == True and red_turn == False:
            print("Game over!")
            print("Yellow team wins! Congratulations!")
            sys.exit()
            



print('Player(s) 1 are the red team, any spot on the "grid" with the letter r is a spot that player(s) 1 controls.\
    \nAny spot with the letter y is the yellow team, player(s) 2')

is_gameover(gameover, None)

