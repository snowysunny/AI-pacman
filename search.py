#-*- coding:utf-8 -*-

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
import sys

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


    import util

    stack = util.Stack()                #Store the visited nodes
    visited = set()
    action = []                         #store the action
    realpaths = []                      #store the realpaths
    currentpath = []                    #store the path that is working

    startstate = problem.getStartState()
    if problem.isGoalState(startstate):
        return 'Stop'

    stack.push([startstate, 'Start', 1])        #push by the style of successors
    realpaths.append([startstate])              #append must be list

    while not stack.isEmpty():
        node = stack.pop()
        if problem.isGoalState(node[0]):
            break
        currentpath = realpaths.pop()

        if node[0] not in visited:
            visited.add(node[0])                #add the node into visited
            successors = problem.getSuccessors(node[0])         #get the successor

            for successor in successors:
                if successor[0] not in visited:
                    stack.push(successor)
                    currentpathcopy = currentpath[:]
                    currentpathcopy.append(successor)
                    realpaths.append(currentpathcopy)

    for realpath in realpaths[-1][1:]:
        action.append(realpath[1])

    return action

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***astar "
    queue = util.Queue()
    visited = []
    realpaths = []
    action = []

    startstate = problem.getStartState()
    if problem.isGoalState(startstate):
        return 'Stop'

    queue.push((startstate, 'Stop', 0))
    realpaths.append([startstate])

    while not queue.isEmpty():
        node = queue.pop()
        if problem.isGoalState(node[0]):
            break
        currentpath = realpaths.pop(0)
        if node[0] not in visited:
            visited.append(node[0])
            successors = problem.getSuccessors(node[0])

            for successor in successors:
                if successor[0] not in visited:
                    queue.push(successor)
                    temppath = []
                    temppath = currentpath[:]
                    temppath.append(successor)
                    realpaths.append(temppath)

    for realpath in realpaths[0][1:]:
        action.append(realpath[1])
    return action
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priorityqueue = util.PriorityQueue()
    visited = []
    action = []

    startstate = problem.getStartState()

    if problem.isGoalState(startstate):
        return 'Stop'

    priorityqueue.push([[(startstate, 'Stop', 0), 0]], 0)

    while not priorityqueue.isEmpty():
        nodes = priorityqueue.pop()
        node = nodes[-1]

        if problem.isGoalState(node[0][0]):
            for path in nodes[1:]:
                action.append(path[0][1])
            return action

        if node[0][0] not in visited:
            visited.append(node[0][0])
            successors = problem.getSuccessors(node[0][0])

            for successor in successors:
                if successor[0] not in visited:
                    cost = node[1] + successor[2]
                    currentpath = nodes[:]
                    currentpath.append([successor, cost])
                    priorityqueue.push(currentpath, cost)
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priorityqueue = util.PriorityQueue()
    visited = []
    action = []

    startstate = problem.getStartState()

    if problem.isGoalState(startstate):
        return 'Stop'
    priority = heuristic(startstate, problem)
    priorityqueue.push([[(startstate, 'Stop', 0), 0]], priority)

    while not priorityqueue.isEmpty():
        nodes = priorityqueue.pop()

        node = nodes[-1]
        if problem.isGoalState(node[0][0]):
            for path in nodes[1:]:
                action.append(path[0][1])
            return action

        if node[0][0] not in visited:
            visited.append(node[0][0])
            successors = problem.getSuccessors(node[0][0])

            for successor in successors:
                if successor[0] not in visited:
                    cost = node[1] + successor[2]
                    priority = cost + heuristic(successor[0], problem)
                    currentpath = nodes[:]
                    currentpath.append([successor, cost])
                    priorityqueue.push(currentpath, priority)
    return []

def GreedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priorityqueue = util.PriorityQueue()
    visited = []
    action = []

    startstate = problem.getStartState()

    if problem.isGoalState(startstate):
        return 'Stop'
    priority = heuristic(startstate, problem)
    priorityqueue.push([[(startstate, 'Stop', 0), 0]], priority)

    while not priorityqueue.isEmpty():
        nodes = priorityqueue.pop()

        node = nodes[-1]
        if problem.isGoalState(node[0][0]):
            for path in nodes[1:]:
                action.append(path[0][1])
            return action

        if node[0][0] not in visited:
            visited.append(node[0][0])
            successors = problem.getSuccessors(node[0][0])

            for successor in successors:
                if successor[0] not in visited:
                    cost = node[1] + successor[2]
                    # priority = cost + heuristic(successor[0], problem)
                    priority = heuristic(successor[0], problem)
                    currentpath = nodes[:]
                    currentpath.append([successor, cost])
                    priorityqueue.push(currentpath, priority)
    return []


# def CostofAction(aPath):
    #     actions = [x[1] for x in aPath]
    #     return problem.getCostOfActions(actions)
    #
    # # cost = lambda aPath: problem.getCostOfActions([x[1] for x in aPath])
    # # cost =
    # # print type(cost)
    #
    # # priorityqueue = util.PriorityQueueWithFunction(cost)
    # priorityqueue = util.PriorityQueueWithFunction(CostofAction)
    #
    # visited = []
    # realpaths = []
    # # paths = []
    # action = []
    #
    # startstate = problem.getStartState()
    # if problem.isGoalState(startstate):
    #     return 'Stop'
    #
    # priorityqueue.push([(startstate, 'Stop', 0)])
    # # paths.append([startstate])
    #
    # while not priorityqueue.isEmpty():
    #     nodes = priorityqueue.pop()
    #     node = nodes[-1]
    #
    #     if problem.isGoalState(node[0]):
    #         break
    #
    #     if node[0] not in visited:
    #         visited.append(node[0])
    #         successors = problem.getSuccessors(node[0])
    #
    #         for successor in successors:
    #             if successor[0] not in visited and problem.isGoalState(successor[0]):
    #                 successorPath = nodes[:]
    #                 successorPath.append(successor)
    #                 priorityqueue.push(successorPath)
    #                 # temppath = []
    #                 # temppath = currentpath[:]
    #                 # temppath.append(successor)
    #                 # paths.append(temppath)
    #
    # for realpath in nodes[1:]:
    #     action.append(realpath[1])
    # return action


# def aStarSearch(problem, heuristic=nullHeuristic):
    # cost = lambda aPath: problem.getCostOfActions([x[1] for x in aPath]) + heuristic(aPath[len(aPath)-1][0], problem)
    #
    # priorityqueue = util.PriorityQueueWithFunction(cost)
    # explored = []
    # priorityqueue.push([(problem.getStartState(), "Stop", 0)])
    #
    # while not priorityqueue.isEmpty():
    #     path = priorityqueue.pop()
    #     s = path[len(path) - 1]
    #     s = s[0]
    #     # print "s: ", s
    #     if problem.isGoalState(s):
    #         # print "FOUND SOLUTION: ", [x[1] for x in path]
    #         return [x[1] for x in path][1:]
    #
    #     if s not in explored:
    #         explored.append(s)
    #         # print "EXPLORING: ", s
    #
    #         for successor in problem.getSuccessors(s):
    #             # print "SUCCESSOR: ", successor
    #             if successor[0] not in explored:
    #                 successorPath = path[:]
    #                 successorPath.append(successor)
    #                 # print "successorPath: ", successorPath
    #                 priorityqueue.push(successorPath)
    #                 # else:
    #                 # print successor[0], " IS ALREADY EXPLORED!!"
    #
    # return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gdy = GreedySearch
