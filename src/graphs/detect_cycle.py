from enum import Enum

class State(Enum):
    NOT_EXPLORED = 0
    BEING_EXPLORED = 1
    EXPLORED = 2

def _has_cycle(G, node, explored):
    explored[node] = State.BEING_EXPLORED
    for child in G[node]:
        if explored[child] == State.BEING_EXPLORED:
            return True
        elif explored[child] == State.NOT_EXPLORED:
            if _has_cycle(G, child, explored):
                return True
    explored[node] = State.EXPLORED
    return False

def has_cycle(G):
    n = len(G)
    explored = [State.NOT_EXPLORED for _ in range(n)]
    for node in range(n):
        if explored[node] == State.NOT_EXPLORED:
            if _has_cycle(G, node, explored):
                return True
    return False
