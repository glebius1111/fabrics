# import the necessary packages
import pickle

from scipy.spatial import distance

storedFeatures = {}

import numpy as np
import csv
class Searcher:

	def __init__(self, indexPath):

		# store our index path
		self.indexPath = indexPath
		self.storedFeatures = {}
		print(indexPath)
		self.read()

	def read(self):
		with open(self.indexPath, 'rb') as handle:
			self.storedFeatures = pickle.load(handle)

	def search(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = []
		for key in self.storedFeatures:
				features = self.storedFeatures[key]
				#features = [float(x) for x in key[][1:]]
				#d = self.chi2_distance(features, queryFeatures)
				d = self.cosine(features, queryFeatures)
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results.append([d, key])

		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results.sort(key=lambda x: x[0], reverse=False)

		# return our (limited) results
		return results[:limit]
	def cosine(self, histA, histB):
		dst = distance.cosine(histA, histB)
		return dst
	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# return the chi-squared distance
		return d