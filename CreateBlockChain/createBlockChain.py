import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building the Blochain


class Blockchain:

    def __init__(self):
        self.chain = []  # List of blocks is a chain
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        block = {'index': self.chain+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'prev_hash': prev_hash, }  # Key-value pairs of everything a block will have
        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]

    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while(check_proof is False):
            hash_operation = hashlib.sha256(
                str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            # check_proof = True
            # print(hash_operation)
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        prev_block = chain[0]
        block_index = 1
        while(block_index < len(chain)):
            block = chain[block_index]
            if(block_index['prev_hash'] != self.hash(prev_block)):
                return False
            prev_proof = prev_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - prev_proof**2).encode()).hexdigest()
            if(hash_operation[:4] != '0000'):
                return False
            prev_block = block
            block_index += 1
        return True

# if __name__ == "__main__":
#     bla = Blockchain()
#     bla.proof_of_work(7)
