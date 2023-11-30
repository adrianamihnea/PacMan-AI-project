# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import random
import util

class CustomNode :
    def __init__ (self , name , cost ):
        self.name = name # attribute name
        self.cost = cost # attribute cost
    def getName ( self ):
        return self.name
    def getCost ( self ):
        return self.cost

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def randomSearch ( problem ):
    current = problem.getStartState()
    solution =[]
    while (not (problem . isGoalState (current))):
        succ = problem . getSuccessors(current)
        no_of_successors = len (succ)
        random_succ_index = int(random.random() * no_of_successors)
        next = succ [ random_succ_index ]
        current = next [0]
        solution.append (next [1])
    print("The  solution  is ", solution)
    return solution

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # successors = problem.getSuccessors(problem.getStartState())
    # print("Start's successors:", successors)
    #
    # for successor in successors:
    #     state, action, cost = successor
    #     print("\tstate: ", state)
    #     print("\taction: ", action)
    #     print("\tcost: ", cost)

    # from game import Directions
    # w = Directions.WEST
    # return [w, w]

    # node1 = CustomNode(" first ", 3)  # creates a new object
    # node2 = CustomNode(" second ", 10)
    # print(" Create  a  stack ")
    # my_stack = util.Stack()
    # print(" Push  the new  node   into  the  stack ")
    # my_stack.push(node1)
    # my_stack.push(node2)
    # print("Pop an  element   from  the  stack ")
    # extracted = my_stack.pop()  # call a method of the object
    # print(" Extracted   node  is ", extracted.getName(), " ", extracted.getCost())

    "*** YOUR CODE HERE ***"
    visited = set()     #keep track of the visited nodes in the graph
    my_stack = util.Stack()         #initialise an empty stack
    start = problem.getStartState()
    #every node in the stack: position + solution until that position
    my_stack.push((start, []))

    solution = []       # solution will be something like: "North", "West", ... (for now it's empty cause we didn't go anywhere)
    while not my_stack.isEmpty():
        state, action = my_stack.pop()
        if(problem.isGoalState(state)):      #we arrived at the food
            return action
        if(state not in visited):
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                succ_state, succ_action, succ_cost = successor
                solution = action + [succ_action]
                my_stack.push((succ_state, solution))

    return solution
    "*** COMPLETED ***"

    # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()     #keep track of the visited nodes in the graph
    my_queue = util.Queue()         #initialise an empty queue
    start = problem.getStartState()
    #every node in the queue: position + solution until that position
    my_queue.push((start, []))

    solution = []       # solution will be something like: "North", "West", ... (for now it's empty cause we didn't go anywhere)
    while not my_queue.isEmpty():
        state, action = my_queue.pop()
        if(problem.isGoalState(state)):      #we arrived at the food
            # visited = set()
            return action
        if(state not in visited):
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                succ_state, succ_action, succ_cost = successor
                solution = action + [succ_action]
                my_queue.push((succ_state, solution))

    return solution
    "*** COMPLETED ***"

    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    "*** YOUR CODE HERE ***"
    visited = set()  # keep track of the visited nodes in the graph
    priority_queue = util.PriorityQueue()  # initialise an empty priority queue
    start = problem.getStartState()
    # every node in the priority queue: item(position + solution until that position) & cost
    priority_queue.push((start, []), 0)

    solution = []  # solution will be something like: "North", "West", ... (for now it's empty cause we didn't go anywhere)
    while not priority_queue.isEmpty():
        (state, action) = priority_queue.pop()      #returns only the item without cost
        if (problem.isGoalState(state)):  # we arrived at the food
            return action
        if (state not in visited):
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                succ_state, succ_action, cost = successor
                solution = action + [succ_action]
                priority_queue.push((succ_state, solution), problem.getCostOfActions(solution))

    return solution
    "*** COMPLETED ***"

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set()  # keep track of the visited nodes in the graph
    function_priority_queue = util.PriorityQueueWithFunction(lambda x: problem.getCostOfActions(x[1]) + heuristic(x[0], problem))
    start = problem.getStartState()
    # every node in the queue: position + solution until that position
    function_priority_queue.push((start, []))

    solution = []  # solution will be something like: "North", "West", ... (for now it's empty cause we didn't go anywhere)
    while not function_priority_queue.isEmpty():
        state, action = function_priority_queue.pop()
        if (problem.isGoalState(state)):  # we arrived at the food
            return action
        if (state not in visited):
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                succ_state, succ_action, succ_cost = successor
                solution = action + [succ_action]
                function_priority_queue.push((succ_state, solution))
    return solution
    "*** COMPLETED ***"
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
rs = randomSearch
