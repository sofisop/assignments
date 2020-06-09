#!/usr/bin/env python3
import argparse
import sqlite3

parser = argparse.ArgumentParser(
        description="Access Key Club Database Views")
parser.add_argument("-v", "--view", help="display named view")
args = parser.parse_args()

conn = sqlite3.connect('keyclub.sqlite')
cur = conn.cursor()

if args.view:
    name = args.view
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace(';', '')
    name = name.replace("'", '')
    for row in cur.execute(f"SELECT * FROM {args.view}"):
        print(row)
else:
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='view'"):
        print(row[0])
