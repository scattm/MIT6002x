from graph import *

nodes = [Node("ABC"), Node("ACB"), Node("BAC"), Node("BCA"), Node("CAB"), Node("CBA")]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[3], nodes[5]))
g.addEdge(Edge(nodes[4], nodes[5]))
