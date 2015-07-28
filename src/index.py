from dependency_graph import DependencyGraph
from relations_graph import RelationsGraph
import requests

# configuration
serverName = "garona"

relationsGraph = RelationsGraph()
relationsGraph.importRelations("/ABSOULTE_PATH_TO/data/item-relations.tsv")

# get server auction house summary file
req = requests.get("http://eu.battle.net/api/wow/auction/data/garona")
res = req.json()

# get server auction house items
req = requests.get(res["files"][0]["url"])
res = req.json()

dependencyGraph = DependencyGraph()

auctions = res["auctions"]["auctions"]
total = len(auctions)
count = 0

# loop through auctions and create dependency graph
for auction in auctions:
	count += 1

	if count % 1000 == 0:
		print count, "/", total, "(", (count / (total / 100)), "%)"

	auctionItem = str(auction["item"])
	auctionPrice = auction["buyout"]
	auctionQuant = auction["quantity"]
	auctionPricePU = float(auctionPrice) / auctionQuant

	dependencyGraph.addVertex(auctionItem)

	vertexPrice = dependencyGraph.getPrice(auctionItem)

	if vertexPrice > auctionPricePU:
		dependencyGraph.setPrice(auctionItem, auctionPricePU)

	edges = relationsGraph.getEdges(auctionItem)

	for edge in edges:
		dependencyGraph.addEdge(auctionItem, edge[0], edge[1])

# get a sorted list of craft / direct price differences
diffs = dependencyGraph.getPriceDiffs()

# dump price differences to file
diffFile = open("/ABSOULTE_PATH_TO/data/diff-file.csv", "w")

for diff in diffs:
	diffFile.write(
		",".join([
			relationsGraph.getLabel(diff[0]),
			str(diff[0]),
			str(diff[1]),
			str(diff[2]),
			str(diff[3]),
			"\n"
		])
	)

diffFile.close()
