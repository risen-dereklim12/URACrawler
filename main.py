from Processor import Processor
from os import path
import json

# Path: URACrawler/main.py

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "data", "latestPtePptyTransactions5y.json"))

data = open(filepath, "r")
data = json.load(data)
data = data["Result"]

p = Processor(data)
streets = p.get_streets()
hillViewTransactions = p.get_transactions_by_street("HILLVIEW AVENUE")