# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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
import copy

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

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
    evaluated = set()
    evalnext = util.Queue()
    initial = [problem.getStartState(), None, 0]
    if problem.isGoalState(initial[0]):
        return []
    evalnext.push([initial, []])
    while evalnext:
        current = evalnext.pop()
        if current[0][1] is None:
            path = current[1]
        else:
            path = current[1] + [current[0][1]]
        if problem.isGoalState(current[0][0]):
            return path
        if ((current[0][0] not in evaluated)):
            evaluated.add(current[0][0])
            successors = problem.getSuccessors(current[0][0])
            for successor in successors:
                evalnext.push([successor, path])
    print "Error, no solution found"
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth.

    Begin with a depth of 1 and increment depth by 1 at every step.
    """
    "*** YOUR CODE HERE ***"
    def DFShelper(state, problem, path, depth, evaluated):
        evaluated.add(state)
        if problem.isGoalState(state):
            return path
        if depth == 0:
            return []
        successors = problem.getSuccessors(state)
        tovisit = []
        for successor in successors:
            if successor[0] not in evaluated:
                evaluated.add(successor[0])
                tovisit += [successor]
        for successor in tovisit:
            temp = DFShelper(successor[0], problem, path + [successor[1]], depth - 1, evaluated)
            if len(temp) > 0:
                return temp
        return []
    state = problem.getStartState()
    path = []
    if problem.isGoalState(state):
        return path
    depth = 1
    while len(path) == 0:
        path = DFShelper(state, problem, [], depth,  set())
        depth += 1
    return path

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    evaluated = set()
    evalnext = util.PriorityQueue()
    initial = [problem.getStartState(), None, 0]
    evalnext.push([initial, [], 0], heuristic(initial[0], problem))
    while evalnext:
        current = evalnext.pop()
        if ((current[0][0] not in evaluated)):
            g = current[2] + current[0][2]
            if current[0][1] is None:
                path = current[1]
            else:
                path = current[1] + [current[0][1]]
            if problem.isGoalState(current[0][0]):
                return path
            else:
                evaluated.add(current[0][0])
                successors = problem.getSuccessors(current[0][0])
                for successor in successors:
                    f = g + heuristic(successor[0], problem) + successor[2]
                    evalnext.push([successor, path, g], f)
    print "Error, no solution found"
    return None

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
