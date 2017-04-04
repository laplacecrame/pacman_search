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

import util

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    #info
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # print "*"*68

    # from game import Directions
    # e = Directions.EAST
    # s = Directions.SOUTH
    # w = Directions.WEST
    # n = Directions.NORTH

    frontier = util.Stack()
    explored = set()

    if problem.isGoalState(problem.getStartState()): return []
    explored.add(problem.getStartState())
    for child in problem.getSuccessors(problem.getStartState()):
        newchild = child + ([child[1]],)
        frontier.push(newchild)
    while not frontier.isEmpty():
        node = frontier.pop()
        explored.add(node[0])
        # print node
        if problem.isGoalState(node[0]):
            # print node, "is the goal"
            # print path
            return node[3]
        for child in problem.getSuccessors(node[0]):
            trace = list(node[3])
            trace.append(child[1])
            newchild = child + (trace,)
            if child[0] not in explored:
                # print "*"*64
                # print trace
                frontier.push(newchild)
    #retuen FAILURE

    # frontier = util.Stack()
    # explored = set()
    # path = []
    # trace =  []
    #
    # if problem.isGoalState(problem.getStartState()): return []
    # explored.add(problem.getStartState())
    # trace.append(0)
    # for child in problem.getSuccessors(problem.getStartState()):
    #     frontier.push(child)
    #     trace[-1] += 1
    # while not frontier.isEmpty():
    #     node = frontier.pop()
    #     explored.add(node[0])
    #     path.append(node[1])
    #     trace[-1] -= 1
    #     if problem.isGoalState(node[0]):
    #         # print node, "is the goal"
    #         # print path
    #         return path
    #     trace.append(0)
    #     for child in problem.getSuccessors(node[0]):
    #         if child[0] not in explored:
    #             frontier.push(child)
    #             trace[-1] += 1
    #     traceback = 0
    #     while trace[-1] == 0:
    #         trace = trace[:-1]
    #         traceback += 1
    #         # path = path[:-1]
    #     # if traceback > 0:
    #     #     print trace
    #     #     print path
    #     temp = []
    #     while traceback > 0:
    #         temp.append(Directions.REVERSE[path[-traceback]])
    #         traceback -= 1
    #     path.extend(temp[::-1])
    #     # if traceback > 0:
    #     #     temp = path[-traceback:]
    #     #     print temp.reverse()
    #     #     print Directions.REVERSE[temp[0]]
    #     #     path.append([Directions.REVERSE[item] for item in temp.reverse()])

    #retuen FAILURE

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    frontier = util.Queue()
    explored = set()

    if problem.isGoalState(problem.getStartState()): return []
    explored.add(problem.getStartState())
    for child in problem.getSuccessors(problem.getStartState()):
        newchild = child + ([child[1]],)
        frontier.push(newchild)
        explored.add(child[0])
    while not frontier.isEmpty():
        # frontier.printself()
        node = frontier.pop()
        # explored.add(node[0])
        # print node
        if problem.isGoalState(node[0]):
            # print node, "is the goal"
            # print path
            return reduce(lambda x,y: x+y, node[3]) if type(node[3][0]) is list else node[3]
        for child in problem.getSuccessors(node[0]):
            trace = list(node[3])
            trace.append(child[1])
            newchild = child + (trace,)
            if child[0] not in explored:
                # print "*"*64
                # print trace
                frontier.push(newchild)
                explored.add(child[0])

    #retuen FAILURE

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    frontier = util.PriorityQueue()
    explored = set()
    path = {}
    cost = {}

    if problem.isGoalState(problem.getStartState()): return []
    explored.add(problem.getStartState())
    for child in problem.getSuccessors(problem.getStartState()):
        # newchild = child + ([child[1]], child[2])
        # frontier.push(newchild, newchild[4])
        path[child[0]] = [child[1]]
        cost[child[0]] = child[2]
        frontier.push(child[0], cost[child[0]])

        # explored.add(child[0])
    while not frontier.isEmpty():
        # frontier.printself()
        node = frontier.pop()
        explored.add(node)
        # print node
        if problem.isGoalState(node):
            # print node, "is the goal"
            # print path
            return path[node]
        for child in problem.getSuccessors(node):
            # trace = list(node[3])
            # trace.append(child[1])
            # newchild = child + (trace, node[4] + child[2])
            if child[0] not in explored:
                # print "*"*64
                # print trace
                # frontier.push(newchild, newchild[4])
                tempcost = cost[node] + child[2]
                if not cost.has_key(child[0]) or cost[child[0]] > tempcost:
                    cost[child[0]] = tempcost
                    path[child[0]] = path[node] + [child[1]]
                frontier.update(child[0], cost[child[0]])
                # explored.add(child[0])

    # retuen FAILURE

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    frontier = util.PriorityQueue()
    explored = set()
    path = {}
    cost = {}

    if problem.isGoalState(problem.getStartState()): return []
    explored.add(problem.getStartState())
    for child in problem.getSuccessors(problem.getStartState()):
        # newchild = child + ([child[1]], child[2])
        # frontier.push(newchild, newchild[4])
        path[child[0]] = [child[1]]
        cost[child[0]] = child[2]
        frontier.push(child[0], cost[child[0]] + heuristic(child[0], problem))

        # explored.add(child[0])
    while not frontier.isEmpty():
        # frontier.printself()
        node = frontier.pop()
        explored.add(node)
        # print node
        if problem.isGoalState(node):
            # print node, "is the goal"
            # print path
            return reduce(lambda x,y: x+y, path[node]) if type(path[node][0]) is list else path[node]
        for child in problem.getSuccessors(node):
            # trace = list(node[3])
            # trace.append(child[1])
            # newchild = child + (trace, node[4] + child[2])
            if child[0] not in explored:
                # print "*"*64
                # print trace
                # frontier.push(newchild, newchild[4])
                tempcost = cost[node] + child[2]
                if not cost.has_key(child[0]) or cost[child[0]] > tempcost:
                    cost[child[0]] = tempcost
                    path[child[0]] = path[node] + [child[1]]
                frontier.update(child[0], cost[child[0]] + heuristic(child[0], problem))
                # explored.add(child[0])

    # retuen FAILURE


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
