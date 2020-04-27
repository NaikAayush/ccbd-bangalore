import os
import glob
import pandas as pd

def write_csv():
    os.chdir(".")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    print(all_filenames)
    combined_csv = pd.concat([pd.read_csv(f,header=None) for f in all_filenames ])
    combined_csv.to_csv("./combined.csv", index=False,header=False)

write_csv()
