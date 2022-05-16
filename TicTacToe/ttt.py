running = True

ttt_table = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
which_user_turn = 'First'
turn_continue = True
filled_pos = 0


def gameon():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('Would you like to replay? Y / N: ')
        if choice not in ['Y','N']:
           print('Sorry this is not a valid input')
        else:
            return choice

def player_input():
    acceptable_range = range(1,10)
    within_range = False
    user_input = 'WRONG'
    
    print('[{0} Player]'.format(which_user_turn))
    
    while user_input.isdigit() == False or within_range == False:
        user_input = input("Enter your desired position in whole number (1-9): ")
        
        if user_input.isdigit() == False:
            print('Sorry that is not a digit!')
        if user_input.isdigit() == True:
            if int(user_input) in acceptable_range:
                print('Input accepted.\n')
                within_range == True
                return int(user_input)
            else:
                print('Sorry, you are out of acceptable range!')
                within_range == False    
    

def display_TTT():
    clear_output()
    print(" {0} | {1} | {2} ".format(ttt_table[1], ttt_table[2], ttt_table[3]))
    print("---|---|---")
    print(" {0} | {1} | {2} ".format(ttt_table[4], ttt_table[5], ttt_table[6]))
    print("---|---|---")
    print(" {0} | {1} | {2} \n".format(ttt_table[7], ttt_table[8], ttt_table[9]))
    #return 0


def replace_mark(user,pos):
    if user == 'First':
        ttt_table[pos] = 'X'
    if user == 'Second':
        ttt_table[pos] = 'O'
    
def check_pos_used(pos):
    if ttt_table[pos] == 'O' or ttt_table[pos] == 'X':
        return True
    else:
        return False

def compare_neighbours(pos1, pos2, pos3):
    if ttt_table[pos1] == ttt_table[pos2] and ttt_table[pos2] == ttt_table[pos3]:
        return True
    else:
        return False

def check_neighbours(pos):
    # check if all neighbours not integers
    # 1. horizontal check
    if pos in [1,4,7]: hor_check = compare_neighbours(pos, pos+1, pos+2)
    elif pos in [2,5,8]: hor_check = compare_neighbours(pos-1, pos, pos+1)
    elif pos in [3,6,9]: hor_check = compare_neighbours(pos-2, pos-1, pos)
    
    # 2. vertical check
    if pos in [1,2,3]: vert_check = compare_neighbours(pos, pos+3, pos+6)
    elif pos in [4,5,6]: vert_check = compare_neighbours(pos-3, pos, pos+3)
    elif pos in [7,8,9]: vert_check = compare_neighbours(pos-6, pos-3, pos)
    
    # 3. diagonal check
    if pos == 1: diag_check = compare_neighbours(pos, pos+4, pos+8)
    elif pos == 5: diag_check = compare_neighbours(pos-4, pos, pos+4)
    elif pos == 9: diag_check = compare_neighbours(pos-8, pos-4, pos)
    elif pos == 3: diag_check = compare_neighbours(pos, pos+2, pos+4)
    elif pos == 7: diag_check = compare_neighbours(pos-4, pos-2, pos)
    else: diag_check = False
    
    return hor_check or vert_check or diag_check

def draw_condition():
    # check draw condition
    if filled_pos == 9: return True
    else: return False

def clear_output():
    print('\n'*50)

while running == True:
    # Call Display TTT table function
    for turn_count in range(1,10):
        display_TTT()
        # Request for player input
        player_pos = player_input()
        if check_pos_used(player_pos):
            print('Error: {0} User please try again with another number'.format(which_user_turn))
        else:
            replace_mark(which_user_turn,player_pos)
            display_TTT()
            filled_pos += 1
            if check_neighbours(player_pos):
                # Win
                print('{0} Player won!'.format(which_user_turn))
                break
            if draw_condition():
                input("It's a Draw! Press any button to continue.")
                break
            else: 
                if which_user_turn == 'First':
                    which_user_turn = 'Second'
                else:
                    which_user_turn = 'First'
            
                
    # win or draw condition calls gameon()
    if gameon() == 'N':
        running = False
    else:
        ttt_table = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
        which_user_turn = 'First'
        filled_pos = 0
    