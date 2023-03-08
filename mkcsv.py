import os
import csv

# Set the directory that contains the subdirectories
root_dir = "/home/xaver/Nextcloud/Semester 11/Measurements/_deduplication"

# Open the output CSV file
with open("deduplication.csv", "w", newline="") as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["file_name", "file_size_original", "file_size_transcoded",
                       "compression_ratio", "transcoding_time", "similarity"])

    # Iterate over the subdirectories in the root directory
    for subdir in os.listdir(root_dir):
        # Construct the path to the input and output files
        input_path = os.path.join(root_dir, subdir, "input.png")
        output_path = os.path.join(root_dir, subdir, "output")

        # Get the file sizes of the input and output files
        file_size_original = os.path.getsize(input_path)
        file_size_transcoded = os.path.getsize(output_path)

        # Calculate the compression ratio
        compression_ratio = file_size_transcoded / file_size_original

        # Read the second line of the meta.txt file
        meta_path = os.path.join(root_dir, subdir, "meta.txt")
        with open(meta_path, "r") as metafile:
            meta_lines = metafile.readlines()
            similarity = meta_lines[0].split('_')[1]
            # Convert seconds to milliseconds
            transcoding_time = round(float(meta_lines[1].strip()) * 1000)
            filename = meta_lines[2].strip().rstrip('.png')

        # Write a row to the CSV file
        csvwriter.writerow([filename, file_size_original, file_size_transcoded,
                           compression_ratio, transcoding_time, similarity])
