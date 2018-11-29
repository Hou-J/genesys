import subprocess, sys, pymongo, os


def check_output(output, argv):
    """
    check if the data saved correctly

    :param output: program exit state
    :param argv: bash argv
    """
    if output == 0:
        client = pymongo.MongoClient(url)
        db = client["genesys"]
        col = db["people"]
        with open(argv[1]) as f:
            try:
                assert col.count() == sum(1 for _ in f) - 1
                print("Data Saved Successfully.", end=" ")

                # delete collection after test
                teardown(col)
            except AssertionError:
                print("Fail: Wrong Number of Rows Saved")
    else:
        try:
            assert output == 1
        except:
            print("Test Fail: Wrong argv Which Should Exit")


def teardown(col):
    """
    delete collection

    :param col: collection
    """
    col.remove()
    print("Removing Collection.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Fail: Wrong argvs, usage: python test_integration.py [MongoDB Connection String]")
        sys.exit(1)

    run_file = "csv_to_mongodb.py"
    cwd = "../task1/genesys.csv"

    if not os.isfile(cwd):
        print("Fail: No csv File in Task1 Folder")
        sys.exit(1)

    url = sys.argv[1]
    argvs = [[run_file, cwd, "asd"],
             [run_file, "123", url],
             [run_file, cwd, url]]

    print("Start {} test(s): \n".format(len(argvs)))
    for i in range(len(argvs)):
        print("Start Test {}:".format(i + 1), end=' ')
        process = subprocess.Popen(['python'] + argvs[i], shell=False,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        process.wait()
        output = process.returncode
        if output:
            print("No Data Saved")
        else:
            check_output(output, argvs[i])
    print("\nFinished All Test")
