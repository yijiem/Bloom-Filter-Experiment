from bitarray import bitarray
import mmh3

class BloomFilter:

	def __init__(self, size, hashcount):
		self.size = size
		self.hash_count = hashcount
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def add(self, string):
		for seed in xrange(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			self.bit_array[result] = 1

	def lookup(self, string):
		for seed in xrange(self.hash_count):
			result = mmh3.hash(string, seed) % self.size
			if self.bit_array[result] == 0:
				return "No";
		return "Probably"




