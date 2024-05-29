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
    
    def get_transactions_by_month(self, month):
        transactions = []
        for street in self.data:
            # @todo: filter transactions by month 
            for txn in street["transaction"]:
                cd = txn["contractDate"]
                if cd[:2] == month:
                    transactions.append(txn)
        print(transactions)
        return transactions