from copy import deepcopy

class Puzzle:
    '''The object to store the puzzle data, including all moves that were made.'''

    def __init__(self, initial_state):
        self.puzzle_states = []
        self.moves = []
        self.solution = []
        self.curr_state = initial_state
        self.score = -1

    def Finish_Puzzle(self):
        '''To be called when the puzzle is finished. This will score the puzzle, set the solution variable, and return the solution.'''
        remaining_pegs = sum(map(sum, self.curr_state))
        self.score = remaining_pegs
        self.solution = self.curr_state
        return self.solution

    def Make_Move(self, x, y, move):
        '''
        Make the specified move to the peg at the given coordinates.
        Valid moves include 'd' for down, 'u' for up, 'l' for left, 'r' for right, 'ud' for diagonal upwards, and 'dd' for diagonal downwards.
        '''
        if x > y:
            # The x value should never be greater than the y value, so return None if that is the case
            print("invalid location")
            return None

        if self.curr_state[y][x] != 1:
            # If a position is passed that has no peg in it. This should not happen.
            print("no peg here to move")
            return None

        # Save the current state of the puzzle in it's object (as a deepcopy so as not to break the main state)
        self.puzzle_states.append(deepcopy(self.curr_state))

        # Remove the peg at the specified coordinates
        self.curr_state[y][x] = 0

        # Make the necessary move, removing the jumped peg and adding the destination location.
        if move == 'd':
            self.curr_state[y+1][x] = 0
            self.curr_state[y+2][x] = 1
        elif move == 'u':
            self.curr_state[y-1][x] = 0
            self.curr_state[y-2][x] = 1
        elif move == 'l':
            self.curr_state[y][x-1] = 0
            self.curr_state[y][x-2] = 1
        elif move == 'r':
            self.curr_state[y][x+1] = 0
            self.curr_state[y][x+2] = 1
        elif move == 'ud':
            self.curr_state[y-1][x-1] = 0
            self.curr_state[y-2][x-2] = 1
        elif move == 'dd':
            self.curr_state[y+1][x+1] = 0
            self.curr_state[y+2][x+2] = 1
        else:
            self.curr_state[y][x] = 1
            print("Invalid move value")
            return None

        # Append the move that was made to the list of moves for this puzzle
        self.moves.append(move)

        # Return the new state of the puzzle
        return self.curr_state

    def Print(self):
        '''Print the current state of the puzzle in a nice format.'''
        self.Print(self.curr_state)

    def Print(self, state):
        '''Print the specified state of the puzzle in a nice format'''
        for row in state:
            print(row)

    def Print_Solution(self):
        '''
        Print the solution to the puzzle.
        
        Note: This function has a lot of output, so it is recommended not to use this often.
        '''

        # Print out the score dialog, telling the user if a solution was found.
        if self.score <= 4 and self.score > 0:
            print(f"You solved it! Your score was {self.score}")
        elif self.score == -1:
            print("Error: No score was computed!")
        else:
            print(f"Failed! Your score was {self.score}")
        
        # Print the solution that was found.
        print("The solved board is:")
        self.Print(self.solution)
        print()

        # Print out all the moves and board states to get to the solution.
        print("Steps to get there")
        self.Print(self.puzzle_states[0])
        print()
        for i in range(1, len(self.puzzle_states)):
            if i-1 < len(self.moves)-1:
                print(self.moves[i-1])
            self.Print(self.puzzle_states[i])
            print()
        print(self.moves[len(self.moves)-1])
        self.Print(self.solution)
        print()