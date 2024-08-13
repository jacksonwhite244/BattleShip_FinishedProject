from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
#import sys
#def input( prompt=None ):
#   if prompt != None:
#       print( prompt, end="" )
#   aaa_str = sys.stdin.readline()
#   aaa_str = aaa_str.rstrip( "\n" )
#   print( aaa_str )
#   return aaa_str

class Player(object):
    """
        add your Class header here.
    """
    def __init__(self, name, board, ship_list):
        """
            add your method header here.
        """
        self.name = name
        self.board = board
        self.ship_list = ship_list
        self.guessed = []
    def validate_guess(self, guess):
        """
            add your method header here.
        """
        # tuple
        guess = (int(guess[0]),int(guess[1]))
        length = len(self.board.board)
        if guess in self.guessed:
            raise RuntimeError("This guess has already been made!")
        elif guess[0] > length or guess[1] > length:
            raise RuntimeError("Guess is not a valid location!")
        else:
            self.guessed.append(guess)

    def get_player_guess(self):
        """
            add your method header here.
        """
        guess = input("Enter your guess: ")
        print(guess)
        worked = False
        while not worked:
            try:
                list_guess = guess.split(', ')
                tup_guess = tuple(list_guess)
                self.validate_guess(tup_guess)
                if len(tup_guess) == 2:
                    worked = True
            except Exception as e:
                print(e)
                guess = input("Enter your guess: ")
        return (int(list_guess[0]),int(list_guess[1]))


    def set_all_ships(self):

        for i in self.ship_list:
            worked = False
            while not worked:
                try:

                    cord = input("Enter the coordinates of the ship of size {}: ".format(str(i)))
                    #print(end='')
                    print(cord)
                    cord = (cord[0],cord[2])

                    orientation = input("Enter the orientation of the ship of size {}: ".format(str(i)))
                    #print(end='')
                    print(orientation)
                    ship = Ship(i,cord,orientation)
                    self.board.validate_ship_coordinates(ship)
                    self.board.place_ship(ship)
                    worked =True
                except Exception as e:
                    print("{}".format(e))




class BattleshipGame(object):
    """
        add your Class header here.
    """

    def __init__(self, player1, player2):
        """
            add your method header here.
        """

        self.player1 = player1
        self.player2 = player2


    def check_game_over(self):
        """
            add your function header here.
        """
        player1win = 0
        player1_board = self.player1.board.board

        for row in player1_board:
            for space in row:
                if space == 'S':
                    player1win +=1

        player2win = 0
        player2_board = self.player2.board.board
        for row in player2_board:
            for space in row:
                if space == 'S':
                    player2win += 1
        if player1win == 0:
            return self.player2.name
        elif player2win == 0:
            return self.player1.name
        else:
            return ''


    def display(self):
        """
            add your function header here.
        """

        print("{}'s board:".format(self.player1.name))
        print(self.player1.board)
        #print()
        print("{}'s board:".format(self.player2.name))
        print(self.player2.board)
        #print()

    def play(self):
        """
            add your function header here.
        """
        self.player1.set_all_ships()
        self.player2.set_all_ships()
        cont = 'c'
        while cont.lower() != 'q':
            self.display()
            try:
                print("{}'s turn.".format(self.player1.name))
                guess = self.player1.get_player_guess()
                self.player2.board.apply_guess(guess)
                if self.check_game_over():
                    winner = self.check_game_over()
                    print("{} wins!".format(winner))
                    #print('hey')
                    quit()
                else:
                    print("{}'s turn.".format(self.player2.name))
                    guess2 = self.player2.get_player_guess()
                    self.player1.board.apply_guess(guess2)

                if self.check_game_over():
                    winner = self.check_game_over()
                    print("{} wins!".format(winner))
                    #print('ho')
                    quit()
                else:

                    cont = input("Continue playing?: ")
                    print(cont)
                    if cont.lower() == 'q':
                        quit()
            except Exception as e:
                print(e)


