#!/usr/bin/env python3
"""  Log stats """


from pymongo import MongoClient
list_all = __import__('8-all').list_all


def count_by_methods(collection, match):
    """ function that return a logs by method """
    return collection.find(*match).count()


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    all_logs_list = list_all(logs)

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f'{len(all_logs_list)} logs')

    print('Methods:')
    for met in method:
        logs_by_method = count_by_methods(logs, [{'method': met}])
        print(f'\tmethod {met}: {logs_by_method}')

    count_path = count_by_methods(
        logs,
        [{'path': '/status'}, {'method': 'GET'}])
    print(f'{count_path} status check')
