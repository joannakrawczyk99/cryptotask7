from hashlib import sha256
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        """
        Defining a single block
        :param index:
        :param transactions:
        :param timestamp:
        :param previous_hash: for protecting entire chain integrity
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        Hashing each block for  immutability and security.
        :return: hashed block
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()