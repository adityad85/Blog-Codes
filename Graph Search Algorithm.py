def graphSearch(problem,technique):
    start= problem.getStartState()
    explored=set([start[0]])
    technique.push(start)

    while not technique.empty():
        node = technique.pop()
        if problem.isGoalState(node):
            return node[i]
        for move in problem.getSuccessors(node):
            if move[0] not inexplored:
                explored.add(move[0])
                technique.push(move)
    return None