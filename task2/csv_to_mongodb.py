import pprint,sys, csv, os

import pymongo
from pymongo import errors


def csv_to_mongodb(path, url):
    """
    Generate num of first and last unique name combinations

    :param path: number of lines (N) in the file
    :param path: number of lines (N) in the file
    :return: True if successful, False if not
    """
    client = pymongo.MongoClient(url)
    db = client["genesys"]
    col = db["people"]

    header = ['firstName', 'lastName', 'age']

    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                col.insert_one({header[0]: row[header[0]],
                                header[1]: row[header[1]],
                                header[2]: row[header[2]]})
            except errors.ConnectionFailure:
                print("Fail: Server Not Available")
                return False
            except Exception:
                print("Fail: Unknown Mongodb Error")
                return False

    r = col.count()
    print(r)

    return True


if __name__ == "__main__":
    # Exit if wrong argvs numbers
    path, url = sys.argv[1], sys.argv[2]
    client = pymongo.MongoClient(url)

    if len(sys.argv) != 3:
        print("Fail: Wrong argvs, usage: python csv_to_mongodb.py [file path] [MongoDB Connection String]")
        sys.exit(1)

    # Exit if wrong argvs
    if not os.path.isfile(path):
        print("Fail: Wrong path, please input a correct path")
        sys.exit(1)

    try:
        client.admin.command("ismaster")
    except errors.ConnectionFailure:
        print("Fail: Server Not Available")
        sys.exit(1)

    print("Start saving csv file \"{}\" to Mongodb.".format(path))

    result = csv_to_mongodb(path, url)

    print("Successfully Saved to Mongodb") if result else print("Failed to Save to Mongodb")
