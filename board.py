class Ship(object):
    """
        add your Class header here.
    """
    def __init__(self, length, position, orientation):
        """
            add your method header here.
        """
        self.length = length
        self.orientation = orientation
        #pos = position.split(',')
        pos = position
        x = int(pos[0])
        y = int(pos[1])
        self.positions = []
        if self.orientation == 'h':
            for i in range(self.length):
                self.positions.append((x,y+i))
        elif self.orientation == 'v':
            for i in range(self.length):
                self.positions.append((x+i,y))
        self.hit_count = 0
        self.is_sunk = False

    def get_positions(self):
        """
            add your method header here.
        """
        return self.positions

    def get_orientation(self):
        """
            add your method header here.
        """
        return self.orientation

    def apply_hit(self):
        """
            add your method header here.
        """
        self.hit_count += 1
        if self.hit_count == self.length:
            self.is_sunk = True


class Board(object):
    """
        add your Class header here.
    """
    def __init__(self, size):
        """
            add your method header here.
        """
        self.size = size
        self.board = []
        for i in range(self.size):
            inside = list(' '*self.size)
            self.board.append(inside)

        self.ships = []

    def place_ship(self, ship):
        """
            add your method header here.
        """
        if ship not in self.ships:
            self.ships.append(ship)

        coordinates = ship.positions
        for cord in coordinates:
            row = cord[0]
            column = cord[1]
            self.board[row][column]='S'

    def apply_guess(self, guess):
        """
            add your method header here.
        """
        row = guess[0]
        column = guess[1]
        if self.board[row][column] == 'S':
            for ship in self.ships:
                for position in ship.positions:
                    if position[0] == row and position[1] == column:
                        ship.apply_hit()
            self.board[row][column] = 'H'
            #update hit count
            print('Hit!')
        else:
            self.board[row][column] = 'M'
            print('Miss!')


    def validate_ship_coordinates(self, ship):
        """
            add your method header here.
        """
        coordinates = ship.positions
        for cord in coordinates:
            row = cord[0]
            column = cord[1]
            if row > self.size or column > self.size:
                raise RuntimeError("Ship coordinates are out of bounds!")
            elif self.board[row][column] != ' ':
                raise RuntimeError("Ship coordinates are already taken!")

    def __str__(self):
        """
            add your method header here.
        """
        out = ''
        index = len(self.board)
        index_list = []
        for i in range(index):
            index_list.append(i)

        for y in range(index):
            for i in range(index):
                out += '[{}]'.format(self.board[y][i])
            out+= '\n'
        return out

#x = [['h','s','h'],['s','h','h'],['h','s','s']]
#index = [0,1,2]
#out = ''
#for y in range(len(x)):
#    for i in range(len(index)):
#        out += '[{}]'.format(x[y][i])
#    out += '\n'
#print(out)