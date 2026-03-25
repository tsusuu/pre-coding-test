import sys

numOfComs = int(sys.stdin.readline())
numOfConect = int(sys.stdin.readline())


graph = dict()
for _ in range(numOfConect):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)
    if y not in graph.keys():
        graph[y] = set([x])
    else:
        graph[y].add(x)


def find_graph(graph, startnode):  # DFS 수정 -> 순서대로 가지 않으면 추가가 정상적으로 되지 않음
    visited = list()  # TODO : 재귀함수로 구현할것
    visited.append(int(1))

    i = startnode
    while i in graph.keys():
        if i in visited:
            visited.extend(graph.get(i))
            i += 1
        else:
            i += 1

    setVisited = set(visited)
    visited = list(setVisited)

    return visited


numOfVisited = len(find_graph(graph, 1)) - 1


print(graph)
print(find_graph(graph, 1))

print(numOfVisited)
