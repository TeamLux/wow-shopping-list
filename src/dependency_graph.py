class DependencyGraph:

	def __init__ (self):
		self.vs = {}
		self.es = {}

	def addVertex (self, vertexId):
		if vertexId not in self.vs:
			self.vs[vertexId] = {
				"depQuants": [],
				"depList": [],

				# "price": 0,
				"price": float("inf"),

				"id": vertexId
			}

		return self.vs[vertexId]

	def addEdge (self, srcId, quantity, dstId):
		srcVertex = self.addVertex(srcId)
		dstVertex = self.addVertex(dstId)

		if srcId not in self.es:
			self.es[srcId] = set()

		edge = self.es[srcId]

		if dstId not in edge:
			dstVertex["depQuants"].append(quantity)
			dstVertex["depList"].append(srcId)

			self.es[srcId].add(dstId)

		return self.es[srcId]

	def getPrice (self, vertexId):
		vertex = self.addVertex(vertexId)

		return vertex["price"]

	def setPrice (self, vertexId, price):
		vertex = self.addVertex(vertexId)

		vertex["price"] = price

		return price

	def getCheapestCraftPrice (self, srcId, tuples):
		srcVertex = self.vs[srcId]

		if len(srcVertex["depList"]) == 0:
			return srcVertex["price"]

		depSum = 0

		for index, depId in enumerate(srcVertex["depList"]):
			quantity = srcVertex["depQuants"][index]

			if (srcId + "-" + depId) in tuples or (depId + "-" + srcId) in tuples:
				continue

			tuples.add(srcId + "-" + depId)
			tuples.add(depId + "-" + srcId)

			depSum += quantity * self.getCheapestCraftPrice(depId, tuples)

		return min(depSum, srcVertex["price"])

	def getPriceDiffs (self, limit=None):
		diffs = []

		for vertexId in self.vs:
			vertex = self.vs[vertexId]

			directPrice = vertex["price"]
			craftPrice = self.getCheapestCraftPrice(vertexId, set())

			diffs.append(
				(
					vertexId,
					craftPrice,
					directPrice,
					(directPrice - craftPrice)
				)
			)

		diffs = filter(lambda diff: diff[3] != 0 and diff[3] != float("inf"), diffs)
		diffs = filter(lambda diff: diff[0] != "UNKNOWN", diffs)
		diffs.sort(key=lambda diff: -1 * diff[3])

		return diffs[:limit] if limit != None else diffs

