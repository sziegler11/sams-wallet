"""
Wallet class
"""

class Wallet:

	def __init__(self):
		self.phrase = []
		# TODO: replace this with a custom tree class to store HD wallet keys
		self.pkeys = set()

	def _initialize_phrase(self):
		pass
