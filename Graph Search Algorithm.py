def graphSearch(problem,strategy):
    start= problem.getStartState()
    explored=set([start[0]])
    strategy.push(start)

    while not strategy.empty():
        node = strategy.pop()
        if problem.isGoalState(node):
            return node[i]
        for move in problem.getSuccessors(node):
            if move[0] not inexplored:
                explored.add(move[0])
                strategy.push(move)
    return None