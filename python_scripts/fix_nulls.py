import os
import pandas as pd

# Relative path to .csv files that need cleaned
data_folder_path = '../data/'

# For every .CSV in the 'data' folder
for file in os.listdir(data_folder_path):
    if file.endswith('.csv'): # If file is .csv
        
        # Create path to csv file
        data_file_path = os.path.join(data_folder_path, file)
        
        # Read the data into Pandas, replace the \N's with NULL values then save the file
        df = pd.read_csv(data_file_path)
        df = df.replace('\\N', '')
        df.to_csv(data_file_path, index=False)