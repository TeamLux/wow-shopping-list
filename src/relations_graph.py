import csv

class RelationsGraph:

	def __init__ (self):
		self.labels = {}
		self.rels = {}

	def importRelations (self, pathname):
		relationsFile = open(pathname, "r")
		csvReader = csv.reader(relationsFile, delimiter='\t')

		for relation in csvReader:
			dstId = relation[0]
			dstName = relation[1]
			srcId = relation[2]
			srcName = relation[3]
			quantity = relation[4]

			self.labels[dstId] = dstName
			self.labels[srcId] = srcName

			if srcId not in self.rels:
				self.rels[srcId] = []

			self.rels[srcId].append((
				int(relation[4]),
				relation[0]
			))

		relationsFile.close()
	
	def getEdges (self, srcId):
		if srcId not in self.rels:
			return []
		else:
			return self.rels[srcId]

	def getLabel (self, vertexId):
		if vertexId not in self.labels:
			return "UNKNOWN"
		else:
			return self.labels[vertexId]
