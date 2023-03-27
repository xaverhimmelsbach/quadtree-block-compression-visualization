import csv

# Define the input and output file paths
input_file = './data/deduplication.csv'
output_file = './data/deduplication_sorted.csv'

# Define the columns to sort by
sort_columns = ['file_name', 'similarity']

# Read the input file and store the data in a list
with open(input_file, 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Sort the data by the specified columns
data.sort(key=lambda x: (x[sort_columns[0]], x[sort_columns[1]]))

# Write the sorted data to the output file
with open(output_file, 'x', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(data)