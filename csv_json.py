import pandas as pd

# Specify the input CSV file and output JSON file
csv_file_path = 'spinny3.csv'
json_file_path = 'spinny.json'

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Write DataFrame to a JSON file
df.to_json(json_file_path, orient='records', indent=2)

# print(f'Conversion completed. JSON file saved at: {json_file_path}')
