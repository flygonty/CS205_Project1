### CS205 Project1 ###
import copy
# reference of deepcopy
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

class Node :
    def __init__( self, puzzle ) :
        self.puzzle = puzzle # puzzle problem
        self.h_cost = 0 # h(n)
        self.f_n = 0 # f(n)
        self.up = None # can move up
        self.down = None # can move down
        self.left = None # can move left
        self.right = None # can move right

    def setH( self, h_cost ) :
        # set h(n)
        self.h_cost = h_cost
    
    def setF( self, f_n ) :
        # set f(n)
        self.f_n = f_n

    def setDepth( self, depth ) :
        # set g(n) which is depth
        self.depth = depth

    def getH( self ) :
        # get value of h(n)
        return self.h_cost
    
    def getF( self ) :
        # get value of f(n)
        return self.f_n

    def getDepth( self ) :
        # get value of g(n)
        return self.depth

    def getState( self ) :
        # get puzzle's current state
        return self.puzzle


def createPuzzle( puzzle, solution ) :
    # generate the puzzle and solution state
    print( '[*] Before started there are several things I would like to inform' )
    print( '[*] Typically, you will need to type arbitrary number to generate the puzzle' )
    print( '[*] However, you should be aware that you must type a valid puzzle' )
    print( '[*] For example you type these numbers 1, 2, 3, 4, 5, 6, 7, 8, 0' )
    print( '[*] !!! IMPORTANT !!!' )
    print( '[*] In this project, "0" means empty space in the puzzle' )
    print( '[*] Now you can create your own puzzle :) Have fun!' )
    print( '[*] What kind of puzzle you wanna create?' )


    print( '[*] First Row' )
    queue = [] # use to store number
    queue_sol = []
    for i in range( 3 ) :
        # read the number in the puzzle and create it
        num = int( input( '[*] Please enter the number: ' ) )
        queue.append( num )
        queue_sol.append( i + 1 )
    puzzle.append( queue )
    solution.append( queue_sol )

    print( '[*] Second Row' )
    queue = [] # use to store number
    queue_sol = []
    for i in range( 3 ) :
        # read the number in the puzzle and create it
        num = int( input( '[*] Please enter the number: ' ) )
        queue.append( num )
        queue_sol.append( i + 4 )
    puzzle.append( queue )
    solution.append( queue_sol )

    print( '[*] Third Row' )
    queue = [] # use to store number
    queue_sol = []
    for i in range( 3 ) :
        # read the number in the puzzle and create it
        num = int( input( '[*] Please enter the number: ' ) )
        queue.append( num )
        queue_sol.append( i + 7 )
    puzzle.append( queue )

    # replace number '9' to '0'
    queue_sol[-1] = 0
    solution.append( queue_sol )

    print( '[*] Puzzle has be set up!' )
    print( '[*] Enjoy your search :)' )


def findZero( puzzle ) :
    # find '0' in the puzzle
    for i in range( len( puzzle ) ) :
        for j in range( len( puzzle[i] ) ) :
            if ( puzzle[i][j] == 0 ) :
                return i, j

def hasVisited( puzzle, visited ) :
    # check the state whether has been visited
    if ( len( visited ) == 0 ) :
        return False

    for i in range( len( puzzle ) ) :
        for j in range( len( puzzle[i] ) ) :
            if ( puzzle[i][j] is not visited[i][j] ) :
                return False
    return True

def exploreAll( node, visited ) :
    # expand the node
    zero_row, zero_column = findZero( node.puzzle )
    state = node.getState()

    # move up
    if ( zero_row > 0 ) :
        temp = copy.deepcopy( state )
        tmp = temp[zero_row-1][zero_column]
        temp[zero_row-1][zero_column] = temp[zero_row][zero_column]
        temp[zero_row][zero_column] = tmp
        if ( hasVisited( temp, visited ) is False ) :
            node.up = Node( temp )

    # move down
    if ( zero_row < len( state ) - 1 ) :
        temp = copy.deepcopy( state )
        tmp = temp[zero_row+1][zero_column]
        temp[zero_row+1][zero_column] = temp[zero_row][zero_column]
        temp[zero_row][zero_column] = tmp
        if ( hasVisited( temp, visited ) is False ) :
            node.down = Node( temp )

    # move left
    if ( zero_column > 0 ) :
        temp = copy.deepcopy( state )
        tmp = temp[zero_row][zero_column-1]
        temp[zero_row][zero_column-1] = temp[zero_row][zero_column]
        temp[zero_row][zero_column] = tmp
        if ( hasVisited( temp, visited ) is False ) :
            node.left = Node( temp )

    # move right
    if ( zero_column < len( state ) - 1 ) :
        temp = copy.deepcopy( state )
        tmp = temp[zero_row][zero_column+1]
        temp[zero_row][zero_column+1] = temp[zero_row][zero_column]
        temp[zero_row][zero_column] = tmp
        if ( hasVisited( temp, visited ) is False ) :
            node.right = Node( temp )

    return node

def showPuzzle( puzzle ) :
    # show the current state of puzzle
    print( 'Here is your puzzle' )
    for i in range( len( puzzle ) ) :
        print( '[ ', end='' )
        for j in range( len( puzzle[i] ) - 1 ) :
            print( str( puzzle[i][j] ) + ", ", end='' )
        print( str( puzzle[i][j+1] ), end='' )
        print( ' ]' )

    print( '\n' )


def initilizedPuzzle( puzzle, solution ) :
    # initilize a puzzle
    puzzle = [[1,2,3],[4,5,6],[0,7,8]]
    solution = [[1,2,3],[4,5,6],[7,8,0]]
    return puzzle, solution


def isGoal( puzzle, solution ) :
    # test puzzle is solution
    for i in range( len( puzzle ) ) :
        for j in range( len( puzzle[i] ) ) :
            if ( puzzle[i][j] is not solution[i][j] ) :
                return False

    return True

def misplacedNum( puzzle, solution ) :
    # calculate misplace tile
    misplaced_num = 0
    for i in range( len( puzzle ) ) :
        for j in range( len( puzzle[i] ) ) :
            if ( puzzle[i][j] is not solution[i][j] ) :
                misplaced_num += 1

    return misplaced_num

def distanceManhattan( puzzle, puzzle_i, puzzle_j, solution ) :
    # calculate the distance to solution 
    distance = 0
    sol_i = 0
    sol_j = 0

    for i in range( len( solution ) ) :
        for j in range( len( solution[i] ) ) :
            if ( solution[i][j] is puzzle[puzzle_i][puzzle_j] ) :
                sol_i = i
                sol_j = j
                distance += abs( i - puzzle_i ) + abs( j - puzzle_j )
    return distance

def manhattanNum( puzzle, solution ) :
    # calculate manhattan heursitc num
    manhattan_num = 0
    for i in range( len( solution ) ) :
        for j in range( len( solution[i] ) ) :
            if ( ( puzzle[i][j] is not solution[i][j] ) and ( puzzle[i][j] is not 0 ) ) :
                # get distance
                manhattan_num += distanceManhattan( puzzle, i, j, solution )
    return manhattan_num

def sortQ( q ) :
    # bubble sort
    # https://www.geeksforgeeks.org/bubble-sort/
    for i in range( len( q ) ) :
        for j in range( len( q ) - i - 1 ) :
            if ( q[j].getF() > q[j+1].getF() ) :
                q[j], q[j+1] = q[j+1], q[j]

def general_search( problem, q_function, solution ) :
    #     nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE)) 
    #     loop do
    #       if EMPTY(nodes) then return "failure"
    #       node = REMOVE-FRONT(nodes)
    #       if problem.GOAL-TEST(node.STATE) succeeds then return node
    #       nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
    #     end
    q = [] # queue for nodes
    visited = [] # record the state that visited before
    num_expanded_node = 0 # record the number of node expands

    # initialize the queue
    parent = Node( problem )
    parent.setDepth( 0 )

    if ( q_function == 2 ) :
        parent.setH( misplacedNum( parent.getState(), solution ) )
    elif ( q_function == 3 ) :
        parent.setH( manhattanNum( parent.getState(), solution ) )

    parent.setF( parent.getDepth() + parent.getH() )
    q.append( parent )

    while ( True ) :
        if ( len( q ) == 0 ) :
            print( 'failure' )
            return "failure"

        node = q.pop( 0 )

        if ( isGoal( node.getState(), solution ) is True ) :
            print( 'Expaned nodex: {}'.format( num_expanded_node ) )
            print( 'Depth: {}'.format( node.getDepth() ) )
            return "success"

        expand_node = exploreAll( node, visited )
        num_expanded_node += 1
        expand_node.setDepth( node.getDepth() + 1 )

        elements = expand_node.up, expand_node.down, expand_node.left, expand_node.right

        for ele in elements :
            if ele is not None :
                ele.setDepth( expand_node.getDepth() )
                if ( q_function == 1 ) :
                    # uniform cost search
                    ele.setDepth( ele.getDepth() )
                    ele.setH( 0 )
                elif ( q_function == 2 ) :
                    # misplaced tile heuristic
                    ele.setDepth( ele.getDepth() )
                    ele.setH( misplacedNum( ele.getState(), solution ) )
                elif ( q_function == 3 ) :
                    # misplaced tile heuristic
                    ele.setDepth( ele.getDepth() )
                    ele.setH( manhattanNum( ele.getState(), solution ) )

                ele.setF( ele.getDepth() + ele.getH() )
                q.append( ele )
                # sort queue
                sortQ( q )
                visited.append( ele.getState() )


def main() :
    # interface to interact the 8-puzzle problem
    puzzle = []
    solution = []

    print( '[+] Welcome to use puzzle!' )
    print( '[+] Now you may enter your initial state for the puzzle :)\n' )
    sel = int( input( '[*] Please choose the puzzle 1. Hardcoded Puzzle 2. Custom Puzzle : ' ) )
    if ( sel == 1 ) :
        puzzle, solution = initilizedPuzzle( puzzle, solution )
        showPuzzle( puzzle )
    elif ( sel == 2 ) :
        createPuzzle( puzzle, solution )
        showPuzzle( puzzle )
    else :
        print( 'Unintended Selction of Puzzle' )
    
    node = Node( puzzle )
    sel = int( input( '[*] Please choose the search 1. UCS 2. A* with misplaced 3. A* with manhattan:  ' ) )
    general_search( puzzle, sel, solution )


if __name__ == "__main__" :
    main()