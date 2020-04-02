import os
import pandas as pd
import glob

root_dir = 'Data/MeasureBoundingBoxAnnotations'

directories = os.listdir(root_dir)

all_csv_files = []

for directory in directories:
    file_path = root_dir + '/' + directory + '/'
    all_csv_files += [i for i in glob.glob(file_path + '*.csv')]

combined_csv = pd.concat([pd.read_csv(f) for f in all_csv_files])

combined_csv.to_csv('all_data.csv', index=False)
