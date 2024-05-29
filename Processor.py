import json
import os
import sys

class Processor:
    def __init__(self, data):
        self.data = data

    def get_streets(self):
        streets = []
        for d in self.data:
            if d["street"] not in streets:
                streets.append(d["street"])
        return streets
    
    def get_transactions_by_street(self, street):
        transactions = []
        for d in self.data:
            if d["street"] == street:
                transactions = d["transaction"]
        return transactions
    
    def get_transactions_by_street_and_block(self, street, block):
        transactions = []
        for d in self.data:
            if d["street"] == street and d["block"] == block:
                transactions = d["transaction"]
        return transactions