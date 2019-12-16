#!/usr/bin/python
import csv

def main():
    alist = []

    columns = [
                {
                    "name": "orderkey",
                    "type": "BIGINT"
                },
                {
                    "name": "partkey",
                    "type": "BIGINT"
                },
                {
                    "name": "suppkey",
                    "type": "BIGINT"
                },
                {
                    "name": "linenumber",
                    "type": "INTEGER"
                },
                {
                    "name": "quantity",
                    "type": "DOUBLE"
                },
                {
                    "name": "discount",
                    "type": "DOUBLE"
                },
                {
                    "name": "tax",
                    "type": "DOUBLE"
                },
                {
                    "name": "returnflag",
                    "type": "VARCHAR"
                },
                {
                    "name": "linestatus",
                    "type": "VARCHAR"
                },
                {
                    "name": "shipdate",
                    "type": "VARCHAR"
                },
                {
                    "name": "commitdate",
                    "type": "VARCHAR"
                },
                {
                    "name": "receiptdate",
                    "type": "VARCHAR"
                },
                {
                    "name": "shipinstruct",
                    "type": "VARCHAR"
                },
                {
                    "name": "shipmode",
                    "type": "VARCHAR"
                },
                {
                    "name": "comment",
                    "type": "VARCHAR"
                }
            ]

    with open('./presto/presto-example-http/src/test/resources/example-data/lineitem-1.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        # spamreader = csv.reader(csvfile)
        for row in spamreader:
            alist.append(row)

    with open("./test.csv", "wb") as csvfile:
        wr = csv.writer(csvfile)
        
        for row in alist:
            wr.writerow(row)

if __name__ == "__main__":
    main()