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


# convert number to a name using if/elif/else

def number_to_name(number):    
    if (number == 0) :
        name = 'rock'

    elif (number == 1) :
        name = 'Spock'
        
    elif (number == 2) :
        name = 'paper'
       
    elif (number == 3) :
        name = 'lizard'
       
    elif (number == 4) :
        name = 'scissors'
    return name

    

 # convert name to number using if/elif/else    
def name_to_number(name):
    if (name == 'rock') :
        number = 0
    elif (name == 'Spock'):
        number = 1 
    elif (name == 'paper'):
        number = 2 
    elif (name == 'lizard'):
        number = 3 
    elif (name == 'scissors'):
        number = 4 
    return number

import random

def rpsls(guess): 
    
# convert name to player_number using name_to_number
    
    player_number = name_to_number(guess)
  

# compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5) 
   
    print "\nPlayer chooses", guess

    print "Computer chooses", number_to_name(comp_number)
    # compute difference of player_number and comp_number modulo five
    
    if (comp_number + 1) % 5 == player_number : 
        print "Player Wins!"
        
    elif (comp_number +2) % 5  == player_number :
        print "Player Wins!"
        
    elif (comp_number == player_number) :
        print "Its a tie!"   
        
    else  :
        print "Computer Wins!"
        

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
