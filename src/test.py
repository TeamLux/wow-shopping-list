from dependency_graph import DependencyGraph

dependencyGraph = DependencyGraph()

dependencyGraph.addVertex("A")
dependencyGraph.addVertex("B")
dependencyGraph.addVertex("C")
dependencyGraph.addVertex("D")

print "\n"
print dependencyGraph.es
print dependencyGraph.vs["A"]["depList"]
print dependencyGraph.vs["B"]["depList"]
print dependencyGraph.vs["C"]["depList"]
print dependencyGraph.vs["D"]["depList"]

dependencyGraph.addEdge("B", 2, "A")
dependencyGraph.addEdge("C", 5, "B")
dependencyGraph.addEdge("D", 1, "B")

print "\n"
print dependencyGraph.es
print dependencyGraph.vs["A"]["depList"]
print dependencyGraph.vs["B"]["depList"]
print dependencyGraph.vs["C"]["depList"]
print dependencyGraph.vs["D"]["depList"]

# dependencyGraph.setPrice("C", 2)
# print "-" * 40
# print "(A)", dependencyGraph.vs["A"]["directPrice"], "-", dependencyGraph.vs["A"]["craftPrice"]
# print "(B)", dependencyGraph.vs["B"]["directPrice"], "-", dependencyGraph.vs["B"]["craftPrice"]
# print "(C)", dependencyGraph.vs["C"]["directPrice"], "-", dependencyGraph.vs["C"]["craftPrice"]
# print "(D)", dependencyGraph.vs["D"]["directPrice"], "-", dependencyGraph.vs["D"]["craftPrice"]

# dependencyGraph.setPrice("D", 6)
# print "-" * 40
# print "(A)", dependencyGraph.vs["A"]["directPrice"], "-", dependencyGraph.vs["A"]["craftPrice"]
# print "(B)", dependencyGraph.vs["B"]["directPrice"], "-", dependencyGraph.vs["B"]["craftPrice"]
# print "(C)", dependencyGraph.vs["C"]["directPrice"], "-", dependencyGraph.vs["C"]["craftPrice"]
# print "(D)", dependencyGraph.vs["D"]["directPrice"], "-", dependencyGraph.vs["D"]["craftPrice"]

# dependencyGraph.setPrice("B", 20)
# print "-" * 40
# print "(A)", dependencyGraph.vs["A"]["directPrice"], "-", dependencyGraph.vs["A"]["craftPrice"]
# print "(B)", dependencyGraph.vs["B"]["directPrice"], "-", dependencyGraph.vs["B"]["craftPrice"]
# print "(C)", dependencyGraph.vs["C"]["directPrice"], "-", dependencyGraph.vs["C"]["craftPrice"]
# print "(D)", dependencyGraph.vs["D"]["directPrice"], "-", dependencyGraph.vs["D"]["craftPrice"]

# dependencyGraph.setPrice("A", 30)
# print "-" * 40
# print "(A)", dependencyGraph.vs["A"]["directPrice"], "-", dependencyGraph.vs["A"]["craftPrice"]
# print "(B)", dependencyGraph.vs["B"]["directPrice"], "-", dependencyGraph.vs["B"]["craftPrice"]
# print "(C)", dependencyGraph.vs["C"]["directPrice"], "-", dependencyGraph.vs["C"]["craftPrice"]
# print "(D)", dependencyGraph.vs["D"]["directPrice"], "-", dependencyGraph.vs["D"]["craftPrice"]

dependencyGraph.setPrice("A", 30)
dependencyGraph.setPrice("B", 20)
dependencyGraph.setPrice("C", 2)
dependencyGraph.setPrice("D", 6)

print "\n"
print dependencyGraph.getPriceDiffs()
