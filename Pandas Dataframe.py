import os
import pandas as pd
import numpy as np
import kaggle
from sklearn.datasets import load_diabetes

# Manually enter your Kaggle username and API key
kaggle_username = input("Enter your Kaggle username: ")
kaggle_key = input("Enter your Kaggle API key: ")

# Set your Kaggle API credentials
os.environ["KAGGLE_USERNAME"] = kaggle_username
os.environ["KAGGLE_KEY"] = kaggle_key

# Download the dataset (replace with the appropriate dataset name)
dataset_name = "mathchi/diabetes-data-set"
kaggle.api.dataset_download_files(dataset_name, path=".")

# Unzip the dataset (if it's zipped)
import zipfile
with zipfile.ZipFile(f"{dataset_name.split('/')[1]}.zip", "r") as zip_ref:
    zip_ref.extractall(".")

print(f"Dataset '{dataset_name}' downloaded and unzipped successfully!")

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

column_names = df.columns
print("Column names:")
for col in column_names:
    print(col)
    
column_data_types = df.dtypes
print("Data types of each column:")
print(column_data_types)
print(df.head())
print(df.tail())

# Assuming you want to set all rows to 'Yes'
df['Record Active'] = 'Yes'

# Assuming df is your DataFrame
df.loc[df['bp'] < 0, 'Record Active'] = 'No'

print(df['Record Active'])

active_rows = df[df['Record Active'] == 'Yes']
print(active_rows)

inactive_rows = df[df['Record Active'] == 'No']
print(inactive_rows)

df.drop(columns=['Record Active'], inplace=True)

# Generate random values for each column
random_values = np.random.rand(len(df.columns))

# Create a new DataFrame with the random values
new_row = pd.DataFrame([random_values], columns=df.columns)

# Append the new row to your existing DataFrame
df = df.append(new_row, ignore_index=True)

print("New row added successfully!")

# Remove the first row
df = df.iloc[1:]
# Remove the last row
df = df.iloc[:-1]
n = int(input("Enter the row you want to delete: "))  # Replace with the desired row number (0-indexed)
df = df.drop(index=n)

x = int(input("Enter the initial row number you want to delete from : "))  # Replace with the starting row index (0-indexed)
y = int(input("Enter the last row number you want to delete to : "))  # Replace with the ending row index (0-indexed)

df = df.drop(index=range(x, y + 1))

df.rename(columns={'s1': 'z1'}, inplace=True)

bmi_mask = df['bmi'] > 25
bmi_filtered_df = df[bmi_mask]
print(bmi_filtered_df.head())

age_mask = df['age'] < 50
bp_mask = df['bp'] > 80
age_filtered_df = df[age_mask & bp_mask]
print(age_filtered_df.head())

female_mask = df['sex'] == 1  # Assuming 1 represents female
bmi_range_mask = (df['bmi'] >= 22) & (df['bmi'] <= 28)
female_bmi_filtered_df = df[female_mask & bmi_range_mask]
print(female_bmi_filtered_df.head())

sorted_df = df.sort_values(by='bmi')
print(sorted_df.head())

multi_sorted_df = df.sort_values(by=['age', 'bp'])
print(multi_sorted_df.head())

df['Years'] = df['Years'].fillna(0)

df_dropped_rows = df.dropna()

df['age'] = df['age'].astype(int)

columns_to_convert = ['age', 'bmi', 'bp']
df[columns_to_convert] = df[columns_to_convert].astype(int)

df['age'] = df['age'].astype(float)

columns_to_convert = ['age', 'bmi', 'bp']
df[columns_to_convert] = df[columns_to_convert].astype(float)

df_trans = df.T
print(df_trans.head())

columns_to_check = ['age', 'bmi']
df_no_duplicates_specific = df.drop_duplicates(subset=columns_to_check)

df = df.drop_duplicates()

# Create a DataFrame from the head (first 5 rows)
df_head = df.head()

# Create a DataFrame from the tail (last 5 rows)
df_tail = df.tail()

# Concatenate the two DataFrames vertically
combined_df = pd.concat([df_head, df_tail])

# Reset the index
combined_df.reset_index(drop=True, inplace=True)

print(combined_df)

# Create a pivot table using the 'Gender' column as the index
p_table = pd.pivot_table(df, index=['gender'])
print(p_table)
