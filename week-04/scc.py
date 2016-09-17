#!/usr/bin/env python

def make_graph(file, reverse):
    graph = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            id, target = map(lambda i: int(i), line.strip().split())
            if reverse:
                target, id = id, target

            if target not in graph:
                graph[target] = []

            if id not in graph:
                graph[id] = [target]
            else:
                graph[id].append(target)

    return graph

def dfs_loop(graph, retsccs):
    seen = set()
    allfins = {}
    fintime = 1
    sccs = []
    n = len(graph.keys())
    for i in range(n, 0, -1):
        if i not in seen:
            fintime, fins = dfs(graph, seen, fintime, i)
            allfins.update(fins)
            if retsccs:
                sccs.append((len(fins.keys()), fins))

    if retsccs:
        return sccs
    else:
        return allfins

def dfs(graph, seen, fintime, start):
    #print "dfs start:", start, fintime
    fins = {}
    stack = [start]
    while stack:
        #print stack
        id = stack.pop()
        if id not in seen:
            #print "visit", id
            seen.add(id)
        else:
            pass
            #print "retreat to", id

        has_unexplored = False
        for vert in graph[id]:
            if vert not in seen:
                has_unexplored = True
                stack.append(id)
                stack.append(vert)
                break

        if has_unexplored:
            pass
            #print "more to explore"
        else:
            #print "finished", id, "at", fintime
            fins[id] = fintime
            fintime += 1

    #print "dfs id finish order", fins
    #print
    return fintime, fins

def graphfins(graph, fins):
    new_graph = {}
    for id in graph.keys():
        new_graph[fins[id]] = [fins[x] for x in graph[id]]
    return new_graph

file = "./graph.in.huge"

print "first pass...",
graph = make_graph(file, reverse=True)
allfins = dfs_loop(graph, False)
print "done"

print "remap...",
graph = make_graph(file, reverse=False)
ngraph = graphfins(graph, allfins)
print "done"

print "second pass...",
sccs = dfs_loop(ngraph, True)
print "done"

print "sort...",
sccs.sort(cmp=lambda a, b: cmp(a[0], b[0]))
print "done"

for size, scc in reversed(sccs[-5:]):
    print size,
