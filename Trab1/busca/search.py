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
import time

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

    raiz = problem.getStartState()

    visitado = []

    def dfsProblemSolver(problem, raiz, visitado, directions):
        visitado.append(raiz)
        caminho = []

        if directions is not None:
            caminho.append(directions)

        if problem.isGoalState(raiz):
            caminho.append(directions) 
            return caminho

        filhoList = problem.getSuccessors(raiz)

        for filho in filhoList:
            if filho[0] in visitado: continue

            retorno = dfsProblemSolver(problem, filho[0], visitado, filho[1])

            if retorno is not None:
                for i in retorno:
                    caminho.append(i)
                return caminho

        return None

    return dfsProblemSolver(problem, raiz, visitado, None)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    def bfsProblemSolver(problem, raiz):
        global solutions
        pre = []
        cor = []
        distancia = []
        fila = []
        translate = []
        visitado = []

        fila.append(raiz)
        cor.append((raiz, 'b'))
        distancia.append((raiz, 0))
        pre.append((raiz, None))
        visitado.append(raiz)
        solved = False
        print solutions

        while fila and not solved:
            atual = fila.pop(0)

            for n, i in enumerate(cor):
                if cor[n][0] == atual:
                    cor[n] = (raiz, 'c')
                    counter = distancia[n][1]

            filhoList = problem.getSuccessors(atual)
            print filhoList

            for filhos in filhoList:
                if filhos[0] in visitado: continue
                if filhos[0] in solutions:
                    goal = filhos[0]
                    goal_aux = filhos[0]
                    solved = True
                    solutions.remove(filhos[0])

                fila.append(filhos[0])
                cor.append((filhos[0], 'b'))
                distancia.append((filhos[0], filhos[2] + counter))
                pre.append((filhos[0], atual))
                translate.append((filhos[0], filhos[1]))
                visitado.append(filhos[0])
            for n, i in enumerate(cor):
                if cor[n][0] == atual:
                    cor[n] = (raiz, 'p')

        retorno = []

        while goal is not raiz:
            for n, i in enumerate(translate):
                if translate[n][0] == goal:
                    retorno.insert(0, translate[n][1])

            for n, i in enumerate(pre):
                if pre[n][0] == goal:
                    goal = pre[n][1]

        return retorno, goal_aux

    global solutions
    aux = problem.getStartState()
    raiz = aux[0]
    solutions = aux[1]

    if isinstance(raiz, int):
        raiz = aux
        solutions = [(1,1)]
        print solutions
        print raiz
    else:
        solutions = list(solutions)
        print solutions
    path_aux = []

    while solutions:
        path, raiz = bfsProblemSolver(problem,raiz)
        path_aux = path_aux + path

    return path_aux

def iterativeDeepeningSearch(problem):
    """
    Start with depth = 0.
    Search the deepest nodes in the search tree first up to a given depth.
    If solution not found, increment depth limit and start over.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    "*** YOUR CODE HERE ***"

    depth = 0
    queue = []
    global solved
    global cost
    solved = False
    global visited_vertex
    visited_vertex = []

    def ids__(node, actualDepth):
        global visited_vertex
        global cost
        global solved

        caminho = []
        if node[1] is not "begin":
            caminho.append(node[1])
            cost.append(actualDepth)
        visited_vertex.append(node[0])
        returned_list = []

        if actualDepth == depth:
            if problem.isGoalState(node[0]):
                solved = True
            return caminho
        else:
            for son in problem.getSuccessors(node[0]):
                try:
                    if actualDepth > cost[visited_vertex.index(son[0])]:
                        return None
                    else:
                        continue
                except:
                    pass

                returned_list = ids__(son, actualDepth + 1)
                if(solved == True):
                    break
            if returned_list == None:
                return caminho
            else:
                return caminho + returned_list

    while solved == False:
        cost = []
        visited_vertex = []
        returned = ids__([problem.getStartState(),'begin',0], 0)
        depth+=1
    return returned

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = []
    root = problem.getStartState()
    # root vertex, path, cost
    queue.push((problem.getStartState(),[]),0)
    actions = []
    alt = []

    while queue:
        actions = []
        vertex = queue.pop()
        visited.append(vertex[0])
        actions.append(vertex[1])

        if problem.isGoalState(vertex[0]):
            return actions[0]

        for son in problem.getSuccessors(vertex[0]):
            if not son[0] in visited:
                alt = actions[0] + [son[1]]
                queue.push((son[0],alt), problem.getCostOfActions(alt))

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = []
    root = problem.getStartState()
    # root vertex, path, cost
    queue.push((problem.getStartState(),[]),0)
    actions = []
    alt = []

    while queue:
        actions = []
        vertex = queue.pop()
        visited.append(vertex[0])
        actions.append(vertex[1])

        if problem.isGoalState(vertex[0]):
            return actions[0]

        for son in problem.getSuccessors(vertex[0]):
            if not son[0] in visited:
                alt = actions[0] + [son[1]]
                queue.push((son[0],alt), problem.getCostOfActions(alt) + heuristic(son[0], problem))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
