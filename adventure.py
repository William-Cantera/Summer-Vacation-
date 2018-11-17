"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

"""
__author__ = "William Cantera"
__version__ = 2

#------------------------------------------------------------------------------------------------------------------------------------------
#AREA FOR STORING MESSAGES DISPLAYED IN GAME, ALSO SOME VARIABLES

delaware_msg = """
You are in Delaware, let's make this the best summer vacation ever.  
Where do you go first? Great Britain, Egypt, or Ancient Greece?
               """

great_britain_msg = """
You get to Great Britain and the first thing you hear is a police officer shouting
at you: "Oi, you got a loicense for that opion?!" You get thrown in jail for wrongthink
and die there three years later
                    """

egypt_msg1 = """
You land in Egypt, home to Pharoahs and conquerers for thousands of years. There are a couple big sites
that are must see. But to get there you should first go to Giza.
             """

egypt_msg2 = """
You don't want to go to Egypt *alone*, best save this for last, surely you need someone to enjoy the sights with!
             """

giza_msg = """
You finally arrive in Giza and are very excited to see some famous sites. Where to go first? The Sphinx or the great
pyramid, built by the all powerful deity Khufu himself?
           """

giza_msg2 = """
Yes, you and your ally have conquered the sphinx and taken the prize that's rightfully yours. Now to finish up your
journey, to the Great Pyramid it is!
            """  

sphinx_win_msg1 = """
You get to the sphinx and take in the enormous stone creature before you. What's this though, it appears to be looking
right at you. It says "Answer my riddle mortal for a chance to recieve great riches, but get it wrong andd suffer the
consequences." You gulp as the sphinx prepares his speech. But before it can continue, Chryseis leaps into action casting
a spell on the beast, it is now asleep and you and Chryseis go into the entrance of the sphinx and into a room labeled
prize room it has three doors: Door One, Door Two, Door Three.
                  """

sphinx_win_msg2 = """
You get to the sphinx and take in the enormous stone creature before you. What's this though, it appears to be looking
right at you. It says "Answer my riddle mortal for a chance to recieve great riches, but get it wrong andd suffer the
consequences." You gulp as the sphinx prepares his speech. Continuing it says:"Who was the mother of the great Khufu
who built the largest pyramid, A. Amenhotep IV, B. Nefertiti, C. Cleopatra, D. Hetepheres I."
                  """
  
sphinx_win_msg3 = """
Correct! you walk past the defeated beast and go into the entrance of the sphinx and into a room labeled
prize room it has three doors: Door One, Door Two, Door Three.
                  """ 

sphinx_lose_msg = """
That answer is incorrect, the sphinx eats you, you are dead.
                  """

door1_msg = """
So you decided to go with Door One, drumroll... The door flies open and inside you find GOLD!
            """

door2_msg = """
Ahh yes, Door Two, excellent choice, you feel the immense power as the door opens and... you find BREAD! Kind of
underwhelming, but who knows that stuffs been in there maybe it's magick.
            """  

door3_msg = """
Hmm, Door Three, it seems promising, here goes nothing. The door abruptly swings open and inside you find MUMMY JUICE!
Wait that's disgusting. Oh well maybe the liquified body of a dead Pharaoh will be useful later.
            """ 

error_msg = """
That's not a valid location
            """ 

quit_msg = """
You have the audacity to quit this game, you will regret that decision.
           """

win_msg = """
Congradulations, you've won.
          """
 
scarab = "Scarab"
gems = "Gems"
mummy_juice = "Mummy Juice"
gold = "Gold"
clothes = "Clothes"
bread = "Bread"

#----------------------------------------------------------------------------------------------------------------------------------------------------

class World:
    '''
    This class represents the world, the main engine of the game, other general attributes unique to
    the world are added here
    
    Attributes:
        game_status (str): the state of the game, either "win", "lose", or "playing"
        Player (Player): the player class
        Companion (Companion): the companion class 
        riddle (bool): whether or not the riddle has been anwsered correctly
        has_companion (bool): whether or not the player has an active companion
        hektor (bool): whether or not Hektor was chosen to win the fight
        death_counter (int): how many times the player has died
        score (str): a message displayed at the end of the game based on the amount of valuable items the player has
        valuable (list): says whether or not an item found in the game is valuable, affects score
        start (bool): a boolean indicating if the user has typed start at the start of the game or not
    '''
    def __init__(self):   
        self.game_status = "playing"
        self.player = Player()
        self.companion = Companion()
        self.riddle = True
        self.sphinx_sleep = False
        self.has_companion = False
        self.hektor = False
        self.death_counter = 0
        self.score = ""
        self.valuable = [gold, mummy_juice, gems, scarab]
        self.start = False
        pass
    
    def is_done(self):
        '''
        Consumes: nothing and Produces a boolean
        
        Args: none
        Returns: boolean, true if game should end, false otherwise
        '''
        if self.game_status == "playing":
            return False
        else:
            return True
        pass
    
    def is_good(self):
        '''
        Consumes: nothing and Produces a boolean
        
        Args: none
        Returns: boolean True is world is valid, false if otherwise
        '''
        if self.player.location == "Great Britain" or self.riddle == False:
            return False
        else:
            return True
        pass
    
        
    def render(self):
        '''
        Consumes: nothing and Produces a string
        
        Args: None
        Returns: a message based on the game state
        '''
        msg = ""
        msg += self.location_msg()+"\n"
        msg += self.current_location_choices()+"\n"
        return msg

    def location_msg(self):
        '''
        Consumes: nothing and Produces nothing
        
        Args: None
        Returns: a message based on the current location
        '''
        if self.player.location == "Delaware" and self.start == True:
            return delaware_msg
        elif self.player.location == "Not Egypt":
            return egypt_msg2
        elif self.player.location == "Egypt":
            return egypt_msg1
        else:
            return ""
    
    def current_location_choices(self):
        '''
        Consumes: nothing and produces nothing
        
        Args: None
        Returns: (str): the displayed message
        '''
        if self.start == True:
            msg = "Either:\n"
            locs = self.valid_locations()
            for loc in locs:
                msg += loc+"\n"
            return msg
        else:
            return ""
    
    def valid_locations(self):
        '''
        Consumes: nothing and Produces nothing
        
        Args: None
        Returns: the valid list of locations for the given location
        '''
        if self.player.location == "Delaware":
            return ["Egypt", "Great Britain", "Ancient Greece",]
        elif self.player.location == "Not Egypt":
            return ["Delaware"]
        elif self.player.location == "Egypt":
            return ["Delaware", "Giza"]
        else:
            return False 
        
    def is_input_good(self, user_input):
        '''
        Consumes: a string and Produces a boolean
        
        Args: user_input (str): the users input
        Returns: a boolean, True if the input is a valid string for the given area
        '''
        if user_input == "quit":
            return True
        elif user_input == "Start":
            return True 
        elif user_input == "Great Britain":
            return True
        elif user_input == "Egypt":
            return True
        else:
            return False
    
        
    def start_delaware(self, string):
        '''
        Consumes: a string and Produces nothing
        
        Args: string (str): the users input
        Returns: updated game state
        '''
        if string == "Delaware":
            self.player.location = "Delaware"
        elif string == "Great Britain":
            self.player.location = "Great Britain"
            self.game_status = "lose"
        elif string == "dummy":
            self.player.location = "dummy"
            self.game_status = "win"    
        
    def in_egypt_sphinx(self, string):
        '''
        Consumes: a string and Produces nothing
        
        Args: string (str): the users input
        Returns: updated game state
        '''
        if string == "Egypt" and self.has_companion == True:
            self.player.location = "Egypt"
        elif string == "Egypt" and self.has_companion == False:
            self.player.location = "Not Egypt"
        elif string == "Giza" and self.sphinx_sleep == False:
            self.player.location = "Giza"
        elif string == "Sphinx":
            self.player.location = "Sphinx"
            if self.companion.name == "Chryseis":
                self.player.location = "Prize Room"
                self.sphinx_sleep = True
        elif string == "D":
            self.sphinx_sleep = True
            self.player.location = "Prize Room"
        elif string == "A" or string == "B" or string == "C":
            self.riddle = False
        elif string == "Door One":
            self.player.inventory.append(gold)
        elif string == "Door Two":
            self.player.inventory.append(bread)
        elif string == "Door Three":
            self.player.inventory.append(mummy_juice)  
        elif string == "Giza":
            self.player.location = "Giza"            
            
        
    
    def process(self, user_input):
        '''
        Consumes: a string and Produces nothing
        
        Args: user_input (str): string rperesenting the users input
        Returns: updated game state
        '''
        if user_input == "quit":
            self.game_status = "quit"
        elif user_input == "Start":
            self.start = True 
        elif user_input == "Great Britain" or user_input == "dummy" or user_input == "Delaware":
            self.start_delaware(user_input)
        elif user_input == "Egypt":
            self.in_egypt_sphinx(user_input)
       # else:
           # return "Your input is not understood" 
        pass
    
    def tick(self):
        ''' 
        Consumes: nothing and Produces nothing
        
        Args: None
        Returns: an updated world state, tick should update things in the background
        '''
        pass
    
    def render_start(self):
        '''
        Consumes: nothing and Produces a string
        
        Args: None
        Returns: A message introducing the player to the game
        '''
        return "Summer Vacation! by: William Cantera, type Start, or quit to quit"
        
    def render_ending(self):
        '''
        Consumes: nothing and Produces a string
        
        Args: None
        Returns: a message depending on whether or not the game has been won, lost or quit
        '''
        if self.game_status == "quit":
            return quit_msg
        elif self.player.location == "dummy":
            return win_msg
        elif self.player.location == "Great Britain":
            return great_britain_msg
        else:
            return None
        pass
    
    def __repr__(self):
        '''
        Consumes: nothing and Produces nothing
        
        Args: None
        Returns: a readable value for certain world attributes
        '''
        return str(vars(self)) 
    
         
#--------------------------------------------------------------------------------------------------


class Player:
    '''
    This class represents a player the person playing the game, important attributes such as location are here,
    other attributes relating to the players status, inventory etc. are all here
    
    Attributes:
        location (str): the current location of the player in the world, starts at Delaware
        inventory (list): a list of items the player may or may not recieve in the game
        energy (bool): whether or not the player is energized
        fate (bool): whether or not fate is on the players side
        chryseis (bool): whether or not the player chose Chryseis as a companion
        achilles (bool): whether or not the player chose Achilles as a companion
        helen (bool): whether or not the player chose Helen as a companion
        banned (bool): whether or not the player is banned from entering the palace
        armor (bool): whether or not the player has armor
        lost (bool): whether or not the player is lost, (in the labyrinth)
    '''
    def __init__(self):
        self.location = "Delaware"
        self.inventory = ["Clothes"]
        self.energy = False
        self.fate = False
        self.chryseis = False
        self.achilles = False
        self.helen = False
        self.banned = False
        self.armor = False
        self.lost = False
        
  
        
class Companion:
    '''
    This class represents the companion the player chooses, which can be either Chryseis, Achilles, or Helen
    the companion class has similar attributes to the player like location, but is different in that they do
    some of the fighting and therefor have attributes denotinig to combat
    
    Attributes:
        location (str): the location of the companion, should be the same as the player once they are in the game
        name (str): the name of the companion, varies upon player choice
        health (int): the health of the companion, if it hits 0, companion dies
        sword (bool): whether or not the companion has some weapon
        alive (bool): wether or not the companion is alive
        inventory (list): list of items the companion has, each companion starts with a unique item set
    '''
    def __init__(self):
        self.location = None 
        self.name = ""
        self.health = 5
        self.sword = False
        self.alive = True
        self.inventory = [clothes]
        
#-------------------------------------------------------------------------------------------------------------------
# WORLD INIT TESTS
test_world2 = World()

test_world = World()
test_world.death_counter = 2
assert test_world.death_counter == 2
assert test_world.game_status == "playing"
assert test_world.riddle == True

#WORLD OTHER FUNCTION TESTS
#is_done tests
assert test_world.is_done() == False
test_world.game_status = "win"
assert test_world.is_done() == True

#start_delaware tests
test_world.start_delaware("Delaware")
assert test_world.player.location == "Delaware"
test_world.start_delaware("Great Britain")
assert test_world.player.location == "Great Britain"
assert test_world.game_status == "lose"

#in_egypt_sphinx tests
test_world.player.location = "Delaware"
test_world.in_egypt_sphinx("Egypt")
assert test_world.player.location == "Not Egypt"
test_world.has_companion = True
test_world.in_egypt_sphinx("Egypt")
assert test_world.player.location == "Egypt"
test_world.in_egypt_sphinx("Giza")
assert test_world.player.location == "Giza"
test_world.in_egypt_sphinx("Sphinx")
assert test_world.player.location == "Sphinx"
test_world.in_egypt_sphinx("A")
assert test_world.riddle == False
test_world.companion.name = "Chryseis"
test_world.player.location = "Prize Room"
assert test_world.player.location == "Prize Room"
test_world.in_egypt_sphinx("Door One")
assert test_world.player.inventory == ["Clothes", "Gold"]
test_world.in_egypt_sphinx("Sphinx")
assert test_world.player.location == "Prize Room"
test_world.in_egypt_sphinx("Door Two")
assert test_world.player.inventory == ["Clothes", "Gold", "Bread"]
test_world.player.location = "Prize Room"


#PLAYER TESTS
test_player = Player()
test_player.lost = True
assert test_player.lost == True
assert test_player.energy == False
assert test_player.location == "Delaware"

#COMPANION TESTS
test_companion = Companion()
test_companion.name = "Heman"
assert test_companion.name == "Heman"
assert test_companion.location == None
assert test_companion.alive == True

#is_good tests
assert test_world.is_good() == False
assert test_world2.is_good() == True

#is_input_good tests
assert test_world.is_input_good("quit") == True
assert test_world.is_input_good("Start") == True
assert test_world.is_input_good("Great Britain") == True

#process tests
test_world.process("Egypt")
assert test_world.player.location == "Egypt"
test_world.process("Great Britain")
assert test_world.game_status == "lose"
test_world.process("quit") 
assert test_world.game_status == "quit"

#render_start tests
assert test_world.render_start() == "Summer Vacation! by: William Cantera, type Start, or quit to quit"

#render_ending tests
test_world.game_status = "quit"
assert test_world.render_ending() == quit_msg
test_world.game_status = "lose"
test_world.player.location = "Great Britain"
assert test_world.render_ending() == great_britain_msg
test_world.player.location = "dummy"
assert test_world.render_ending() == win_msg

#render tests
test_world.start = True
test_world.player.location = "Delaware"
assert test_world.render() ==  """\nYou are in Delaware, let's make this the best summer vacation ever.  \nWhere do you go first? Great Britain, Egypt, or Ancient Greece?\n               \nEither:\nEgypt\nGreat Britain\nAncient Greece\n\n"""   
test_world.player.location = "Egypt" 
assert test_world.render() == """\nYou land in Egypt, home to Pharoahs and conquerers for thousands of years. There are a couple big sites\nthat are must see. But to get there you should first go to Giza.\n             \nEither:\nDelaware\nGiza\n\n"""                     
               
#location_msg tests
test_world.player.location = "Delaware"
assert test_world.location_msg() == delaware_msg
test_world.player.location = "Egypt"
assert test_world.location_msg() == egypt_msg1

#current_location_choices tests
assert test_world.current_location_choices() == 'Either:\nDelaware\nGiza\n'
test_world.start = False
assert test_world.current_location_choices() == ""

#valid_locations tests
assert test_world.valid_locations() == ['Delaware', 'Giza']
test_world.player.location = "Delaware"
assert test_world.valid_locations() == ["Egypt", "Great Britain", "Ancient Greece",]




# Command Paths to give to the unit tester

WIN_PATH = ["dummy"]
LOSE_PATH = ["Great Britain"] 

def main():
    '''
    This is the Main game function. When executed, it begins a run of the game.
    Read over it to understand the engine that you are using and the order
    that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())

# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # world = World()
    # world.is_done()
    # print(world.render())
    # ...
