#!/bin/bash

# Check for the correct number of arguments
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_h5ad_path>"
    exit 1
fi

# Variables to hold input path
input_h5ad="$1"

# Extract the directory path from the input file path
input_dir=$(dirname "$input_h5ad")

# Extract the base name without extension
base_name=$(basename "$input_h5ad" .h5ad)

# Construct the output RDS file name using the same base name
output_rds="${input_dir}/${base_name}.rds"

# Directory for temporary files
temp_dir="${input_dir}/temp_files"
mkdir -p "$temp_dir"

# Step 1: Run Python script to convert .h5ad to intermediary files
python h5ad_to_mtx.py "$input_h5ad" "$temp_dir"

# Step 2: Run R script to load intermediary files and save as .rds
Rscript mtx_to_rds.R "$temp_dir" "$output_rds"

# Optional: Clean up temporary files
rm -r "$temp_dir"

echo "Conversion completed. Output available at $output_rds"
