import sys

if __name__ == "__main__":
    # Exit if wrong argvs
    if len(sys.argv) != 3:
        print("Fail: Wrong argvs, usage: python csv_generator.py [number of lines] [file path]")
        sys.exit(1)

    line_num_csv = sys.argv[1]
    path_csv = sys.argv[2]
    print("Start generating {} lines csv file in the path \"{}\".".format(line_num_csv, path_csv))
