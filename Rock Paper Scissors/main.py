import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' fpr paper 's' for scissors\n")
    user = user.lower()

    computer =random.choice(['r','p','s'])

    if user == computer:
        return (0, user, computer)
    
    #r>s, s>p, p>r
    if is_win(user,computer):
        return (1, user, computer)
    
    return (-1, user, computer)
    
def  is_win(player, opponent):
     #return true is the player beats the opponent
     #winning conditions: r>s, s>p, p>r

     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
         return True
     return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3,3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        #tie
        if result ==0:
            print('It is a tie. You and the computer both chosen {}. \n'.format(user))

        #player win   
        elif result ==1:
            player_wins += 1
            print('You chose {} and the computer chose {}.You won!\n'.format(user, computer)) 
        else:
              computer_wins += 1
              print ('You chose {} and the computer chose {}.You lost :(\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games! What a champ :D'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))



if __name__ == '__main__':
    play_best_of(3) #2
    #play_best_of(9) #5