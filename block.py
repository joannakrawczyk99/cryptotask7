from hashlib import sha256
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        """
        Defining a single block
        :param index: an index of transaction
        :param transactions: transaction that we want to add to blockchain
        :param timestamp: stamp the block when it’s created
        :param previous_hash: hashed version of recently approved block
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