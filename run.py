# Search methods

import search

ab = search.GPSProblem('G', 'S'
                       , search.romania)

print("-----Búsqueda en anchura-----")
print(search.breadth_first_graph_search(ab).path())

print("-----Búsqueda en profundidad-----")
print(search.depth_first_graph_search(ab).path())

print("-----Búsqueda por branch and bounding-----")
print(search.bab_graph_search(ab).path())

print("-----Búsqueda por branch and bounding oon subestimación-----")
print(search.heu_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
