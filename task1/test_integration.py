import os, subprocess


def check_output(output, argv, file_name):
    """
   check if the csv generated correctly

   :param output: program exit state
   :param argv: bash argv
   :param file_name: saved csv file name
   """
    if output == 0:
        with open(os.path.join(argv[2], file_name)) as f:
            try:
                assert f.readline()[:22] == "firstName,lastName,age"
            except:
                print("Test Fail: Wrong File Header Generated")

            try:
                assert sum(1 for _ in f) == int(argv[1])
            except AssertionError:
                print(sum(1 for _ in f), int(argv[1]))
                print("Test Fail: Wrong File Rows Generated")
    else:
        try:
            assert output == 1
        except:
            print("Test Fail: Wrong argv Which Should Exit")


def teardown(argv, file_name):
    """
    delete test file after tested

    :param argv: bash argv
    :param file_name: file to be deleted
    """
    file = os.path.join(argv[2], file_name)
    os.remove(file)
    print("Removing Test Generated File.")


if __name__ == "__main__":
    run_file = "csv_generator.py"
    file_name = 'genesys.csv'
    cwd = os.getcwd()
    argvs = [[run_file, "1", cwd],
             [run_file, "10000", cwd],
             [run_file, "2", cwd],
             [run_file, "9999", cwd],
             [run_file, "1000", "123"],
             [run_file, "1.2", cwd],
             [run_file, "abc", cwd],
             [run_file, "20", cwd]]

    print("Start {} test(s): \n".format(len(argvs)))
    for i in range(len(argvs)):
        print("Start Test {}:".format(i + 1), end=' ')
        process = subprocess.Popen(['python'] + argvs[i], shell=False,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        process.wait()
        output = process.returncode
        if output:
            print("No File Generated.")
            check_output(output, argvs[i], file_name)
        else:
            print("File Generated Successfully.", end=" ")
            teardown(argvs[i], file_name)
    print("\nFinished All Test")
