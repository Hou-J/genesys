import os, subprocess


def check_output(output, argv, file_name):
    # print("c")
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
            print("Test Fail: Wrong argv Did not exit")


def teardown(argv, file_name):
    # print("t")
    file = os.path.join(argv[2], file_name)
    os.remove(file)
    print("Removing Test Generated File.")


if __name__ == "__main__":
    file_name = 'genesys.csv'
    argvs = [["csv_generator.py", "1", os.getcwd()],
             ["csv_generator.py", "10000", os.getcwd()],
             ["csv_generator.py", "2", os.getcwd()],
             ["csv_generator.py", "9999", os.getcwd()],
             ["csv_generator.py", "1000", "123"],
             ["csv_generator.py", "1.2", os.getcwd()],
             ["csv_generator.py", "abc", os.getcwd()],
             ["csv_generator.py", "20", os.getcwd()]]

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
