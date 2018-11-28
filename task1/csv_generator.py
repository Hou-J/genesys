import sys, os
import random
import pandas as pd
import numpy as np


def name_generator(num):
    """
    Generate num of first and last unique name combinations

    :param num: number of lines (N) in the file
    :return: list of names
    """
    # The first and last names in the files can generate 20000 unique name combinations
    if num > 20000:
        sys.exit(1)
    female_first_names = np.array(pd.read_csv("names/female.first.txt", header=None))
    male_first_names = np.array(pd.read_csv("names/male.first.txt", header=None))
    last_names = np.array(pd.read_csv("names/last.txt", header=None))

    names = set()
    while len(names) < num:
        if random.choice([0, 1]):
            names.add(" ".join([random.choice(female_first_names)[0], random.choice(last_names)[0]]))
        else:
            names.add(" ".join([random.choice(male_first_names)[0], random.choice(last_names)[0]]))
    return list(names)


def age_generator(num):
    """
    Generate num of random ages, 1 < age < 100

    :param num: number of lines (N) in the file
    :return: list of ages
    """
    # num should greater than 1
    return [random.randint(2, 99) for _ in range(num)] if num >= 1 else sys.exit(1)


if __name__ == "__main__":
    # Exit if wrong argvs numbers
    if len(sys.argv) != 3:
        print("Fail: Wrong argvs, usage: python csv_generator.py [number of lines] [file path]")
        sys.exit(1)

    # Exit if wrong argvs types or ranges
    try:
        if not 1 < int(sys.argv[1]) < 10000:
            print("Fail: Wrong number range, N is in valid interval 1<N<10 000")
            sys.exit(1)
        elif not os.path.isabs(sys.argv[2]):
            print("Fail: Wrong path, please input a correct path")
            sys.exit(1)
    except ValueError:
        print("Fail: Wrong number type, N is in valid interval 1<N<10 000")
        sys.exit(1)

    line_num = int(sys.argv[1])
    file_dir = sys.argv[2]

    # define file name and header
    file_name = 'genesys.csv'
    file_path = os.path.join(file_dir, file_name)
    headers = ['firstName', 'lastName', 'age']

    # Start generate csv
    print("Start generating {} lines csv file \"{}\" at the path \"{}\".".format(line_num, file_name, file_dir))

    names = name_generator(line_num)
    ages = age_generator(line_num)
    df = pd.DataFrame({headers[0]: [n.split()[0] for n in names],
                       headers[1]: [n.split()[1] for n in names],
                       headers[2]: [a for a in ages]})
    df = df.reindex(columns=headers)
    df.to_csv(file_path, sep=',', header=True, index=False)

    print("Done generating file \"{}\".".format(file_path))
