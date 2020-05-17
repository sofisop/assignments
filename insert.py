import sqlite3
import argparse

# Setup for CLI. Do not touch!
# ===== BEGIN CLI BLOCK ===== #

parser = argparse.ArgumentParser()
parser.add_argument("db", default=":memory:", help="The file path of the database to be edited")
parser.add_argument("-r", "--roster")
args = parser.parse_args()

# ===== END CLI BLOCK ===== #

conn = sqlite3.connect(args.db)
cur = conn.cursor()

if args.roster:
    with open(args.roster) as f:
        for record in f:
            name = record.strip()
            cur.executescript(f"INSERT INTO students (name) values ('{name}')")
            conn.commit()
        conn.close()

else:
    while True:
        name = input("Type your first and last name and hit enter to register. Hit Ctrl+C to quit.\n> ")
        cur.execute(f"INSERT INTO students (name) VALUES ('{name}');")
        conn.commit()

