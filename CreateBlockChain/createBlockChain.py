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
