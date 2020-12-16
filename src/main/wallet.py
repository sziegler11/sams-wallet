"""
Wallet class
"""
import hashlib
import os
import sys
from bitstring import BitArray

# TODOS: implement a converter from bytes to bits in python.

# TODO: this below could be HDWallet, implement a base Wallet first that just has very basic functionality
class Wallet:

	def __init__(self):
		# TODO: replace this with a custom tree class to store HD wallet keys
		self._pkeys = set()
		self._words = _load_words()
		self._mnemonic = self._initialize_mnemonic()

	def _initialize_mnemonic(self):
		rand_bytes = os.urandom(32)
		rand_bytes_bin = _zero_pad(bin(int.from_bytes(rand_bytes, sys.byteorder))[2:])
		rand_hash_hex = hashlib.sha256(rand_bytes).hexdigest()
		rand_hash_bin = BitArray(bytes=rand_hash_hex.encode()).bin
		checksum = rand_hash_bin[:8] # first byte is the checksum, as a bit string
		mnemonic_bits = rand_bytes_bin + checksum
		word_bitstrings = _split_string(mnemonic_bits, 11)
		mnemonic_words = []
		for bits in word_bitstrings:
			mnemonic_words.append(self._words[int(bits, 2)])
		return mnemonic_words

	def get_mnemonic(self):
		return self._mnemonic

def _split_string(str, split_size):
	if len(str) % split_size != 0:
		raise ValueError("String length must be a multiple of split_size!")
	ix = 0
	s = ix + split_size
	ret = [str[ix:s]]
	while s < len(str):
		ix = s
		s = ix + split_size
		ret.append(str[ix:s])
	return ret

def _load_words():
	with open("../resources/words.txt") as words_file:
		words = [line.rstrip('\n') for line in words_file]
	return words

def _zero_pad(bits, num_bits=256):
	pad = "".join(['0' for i in range(num_bits-len(bits))])
	return pad + bits



