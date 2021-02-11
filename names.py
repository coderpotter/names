import getopt, sys
from Levenshtein import distance
import pandas as pd

name = sys.argv[1]
argumentList = sys.argv[2:]
options = "g:s:l:n:"
long_options = ["Gender =", "Starting =", "Length =", "Number ="]
gender, starting, length, number = None, None, len(name), 10

try:
    arguments, values = getopt.getopt(argumentList, options)
    for a, v in arguments:
        if a in ("-g", "--Gender"):
            gender = v.upper()
        elif a in ("-s", "--Starting"):
            starting = v
        elif a in ("-l", "--Length"):
            length = int(v)
        elif a in ("-n", "--Number"):
            number = int(v)
except getopt.error as err:
    print(str(err))

print('Reading the file')
names = pd.read_csv("archive/NationalNames.csv")
names = names[names.Name.str.len() <= length]
if gender:
    names = names[names.Gender == gender]
if starting:
    names = names[names.Name.startswith(starting[0])]

print('Generating results')
close_names = sorted(list(set(names.Name.tolist())), key=lambda x: distance(name, x))
print(close_names[:number])