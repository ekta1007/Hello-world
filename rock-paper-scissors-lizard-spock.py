# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
dict_player ={ 0 : 'rock', 1: 'Spock' , 2 : 'paper' ,3:'lizard'
    , 4:'scissors'}

# this gives the keys as -: dict_player.keys() = [0,1,2,3,4]

def number_to_name(number):
    return dict_player.get(number)
 
    
def name_to_number(name):
    dict_player_reverse=dict([(v,k) for k,v in dict_player.items()])
    return dict_player_reverse.get(name)


def rpsls(name): 

    # convert name to player_number using name_to_number
    player_number=name_to_number(name)
    print "Player chooses %s" % name
    
    # compute random guess for comp_number using random.randrange()
    # goes till 5 since 5 is not included
    comp_number=random.randrange(0,5)
    print "Computer chooses %s" % number_to_name(comp_number)
   
    if (comp_number == 0 and player_number==4) or (comp_number == 4 and player_number==0):
        winner = min(comp_number,player_number)
    elif (comp_number == 1 and player_number==4) or (comp_number == 4 and player_number==1):
        winner = min(comp_number,player_number)
    elif (comp_number == 0 and player_number==3) or (comp_number == 3 and player_number==0):
        winner = min(comp_number,player_number)
    elif comp_number==player_number :
        winner="Tie"
        print "It's a Tie!"
    else :
        winner = max(comp_number,player_number)
    if winner ==comp_number :
        print "Computer wins!"
    elif winner ==player_number  :
        print "Player wins!"
    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

