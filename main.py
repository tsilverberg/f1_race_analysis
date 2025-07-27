# Assignment #3: Hands-On Data Prep - F1 GP Race Wins Analysis

# Step 1: Imports and Dataset Download
import os

os.environ["KAGGLE_CONFIG_DIR"] = os.path.join(os.getcwd(), ".kaggle")


# Assignment #3: Hands-On Data Prep - F1 GP Race Wins Analysis

# Step 1: Imports and Dataset Download
import os
import pandas as pd
import kagglehub

# Set output directory for dataset
output_dir = os.path.join(os.getcwd(), 'f1_data')
os.makedirs(output_dir, exist_ok=True)

# Download the dataset
path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")
print("Dataset path:", path)

# Step 2: Load Required CSVs
races_df = pd.read_csv(os.path.join(path, 'races.csv'))
results_df = pd.read_csv(os.path.join(path, 'results.csv'))
drivers_df = pd.read_csv(os.path.join(path, 'drivers.csv'))

# Step 3: Filter GP Race Winners (positionOrder == 1)
gp_winners_df = results_df[results_df['positionOrder'] == 1]

# Step 4: Merge with Driver Names
winners_with_names = pd.merge(gp_winners_df, drivers_df, on='driverId')
winners_with_names['driverName'] = winners_with_names['forename'] + ' ' + winners_with_names['surname']

# Step 5: Clean Up - Drop duplicates and nulls
winners_with_names.dropna(subset=['driverName'], inplace=True)
winners_with_names.drop_duplicates(subset=['raceId', 'driverId'], inplace=True)

# Step 6: Count GP Wins Per Driver
gp_win_counts = winners_with_names['driverName'].value_counts().reset_index()
gp_win_counts.columns = ['driverName', 'raceWins']

# Step 7: Save Output to f1_data folder
output_file = os.path.join(output_dir, 'gp_race_win_counts.csv')
gp_win_counts.to_csv(output_file, index=False)

# Step 8: Display the Results
print("Number of F1 GP race wins per driver:")
print(gp_win_counts.head(15))
print(f"\nSaved output to: {output_file}")
