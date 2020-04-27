from multiprocessing import Process
import api
import os
import glob
import pandas as pd

INDEX = 0
LIMIT = 10000

NO_OF_PROCESSES = os.cpu_count()

def write_csv():
    os.chdir("./new")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    print(all_filenames)
    combined_csv = pd.concat([pd.read_csv(f,header=None) for f in all_filenames ])
    combined_csv.to_csv("./combined.csv", index=False,header=False)

if __name__ == '__main__':
    inputfile = './remaining.csv'
    outputfile = ['./new/data'+str(x)+'.csv' for x in range(1,NO_OF_PROCESSES+1)]
    p = ['p'+str(x) for x in range(1,NO_OF_PROCESSES+1)]
    for i in range(1, NO_OF_PROCESSES):
        p[i]=Process(target=api.start, args=(INDEX, INDEX+LIMIT, API_KEY, inputfile, outputfile[i]))
        INDEX=INDEX+LIMIT
    for i in range(1, NO_OF_PROCESSES):
        p[i].start()
    for i in range(1, NO_OF_PROCESSES):
        p[i].join()
    write_csv()
