from block import Block
import time


class Blockchain:
    difficulty = 2

    def __init__(self):
        """
        Defining a blockchain.
        """
        self.pending_transactions = []
        self.chain = [] #an empty list that we add block to
        self.create_block()

    def create_block(self):
        """
        Generating block and appending it to the chain.
        """
        genesis_block = Block(0, "+100 PLN", time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

        genesis_block2 = Block(1, "-20 PLN", time.time(), genesis_block.hash)
        genesis_block2.hash = genesis_block2.compute_hash()
        self.chain.append(genesis_block2)

    @property
    def last_block(self):
        """
        :return: block that was added most recently
        """
        return self.chain[-1]

    def add_new_block(self, block, proof):
        """
        Adding block to the chain after verification.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid(self, block, block_hash):
        """
        Checking if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine(self):
        """
        Adding pending transactions to the blockchain.
        """
        if not self.pending_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.pending_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_new_block(new_block, proof)

        self.pending_transactions = []
        return new_block.index
