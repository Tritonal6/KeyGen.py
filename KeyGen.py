#! python 3

import random, sys

class KeyGen():
	
	def __init__(self):
		global i
		i = int(input("How many serial codes are you looking for? \n"))
		print("")
		self.main(i)

	def main(self, count):
		""" """
		seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		store = []

		for i in range(count):
			print('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(5)))

		print("\nCreated {} serial keys for you, m'lord.".format(count))

if __name__ == '__main__':
	app = KeyGen()