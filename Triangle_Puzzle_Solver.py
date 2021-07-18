from copy import deepcopy
from Puzzle_Helpers import Puzzle

solutions = []

def solve(puzzle):
    '''A recursive function to find all solutions to the puzzle.'''
    global solutions
    possible_moves = find_all_moves(puzzle)
    if not possible_moves:
        # Then there are no moves left and we either found a solution or not
        puzzle.Finish_Puzzle()
        # Handle only puzzles with a score of 1 (the best possible score)
        # Append this solution to the list of solutions
        solutions.append(puzzle)
        if puzzle.score == 1:
            # Return the puzzle, thus stopping the recursion.
            return puzzle
    else:
        # Recursively make every possible move at this given board state
        for position in possible_moves:
            x, y, moves = position
            for move in moves:
                # Make a deep copy of the puzzle the maintain the original.
                copy = deepcopy(puzzle)
                copy.Make_Move(x, y, move)
                # Once the move is made and as long as there is a valid state, recursively solve the new puzzle
                if copy and copy.curr_state:
                    if solve(copy):
                        return puzzle
        return None

def find_all_moves(puzzle):
    '''Find all of the moves that can be made in a given puzzle state.'''
    to_return = []
    for i in range(len(puzzle.curr_state)):
        for j in range(len(puzzle.curr_state[i])):
            positional_moves = find_positional_moves(j, i, puzzle)
            if positional_moves:
                to_return.append((j, i, positional_moves))

    return to_return

def find_positional_moves(x, y, puzzle):
    '''Find all possible moves that can be made to the peg at the given coordinates.'''
    if x > y:
        print("invalid location")
        return None

    if puzzle.curr_state[y][x] != 1:
        return None
    
    # down=d, up=u, left=l, right=r, up diagonal=du, down diagonal=dd
    possible_moves = []

    # Check for down move
    if y < len(puzzle.curr_state) - 2:
        if puzzle.curr_state[y+1][x] == 1 and puzzle.curr_state[y+2][x] != 1:
            possible_moves.append("d")
    
    # Check for up move
    if y > 1:
        if len(puzzle.curr_state[y-1]) > x and len(puzzle.curr_state[y-2]) > x:
            if puzzle.curr_state[y-1][x] == 1 and puzzle.curr_state[y-2][x] != 1:
                possible_moves.append("u")
    
    # Check for left move
    if x > 1:
        if puzzle.curr_state[y][x-1] == 1 and puzzle.curr_state[y][x-2] != 1:
            possible_moves.append("l")

    # Check for right move
    if x < len(puzzle.curr_state[y]) - 2:
        if puzzle.curr_state[y][x+1] == 1 and puzzle.curr_state[y][x+2] != 1:
            possible_moves.append("r")

    # Check for up diagonal move
    if x > 1 and y > 1:
        if puzzle.curr_state[y-1][x-1] == 1 and puzzle.curr_state[y-2][x-2] != 1:
            possible_moves.append("ud")

    # Check for down diagonal move
    if y < len(puzzle.curr_state) - 2 and x < len(puzzle.curr_state[y+2]):
        if puzzle.curr_state[y+1][x+1] == 1 and puzzle.curr_state[y+2][x+2] != 1:
            possible_moves.append("dd")
    
    return possible_moves

if __name__ == "__main__":
    intial_puzzle_state = [
        [1],
        [1, 1],
        [1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    # Create the puzzle object
    puzzle = Puzzle(intial_puzzle_state)
    # Solve the puzzle
    solve(puzzle)
    print(f"Found {len(solutions)} possible solutions before finding one with a score of 1.")
    # Since the code stops looking when it finds a solution with a score of 1,
    # This will print out that solution with the score of 1.
    solutions[len(solutions)-1].Print_Solution()