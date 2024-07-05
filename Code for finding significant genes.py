import pandas as pd

# Load the SNP and Indel datasets using ISO-8859-1 encoding with low_memory=False
try:
    snp_data = pd.read_csv('/mnt/data/B26.snp.annot.csv', encoding='ISO-8859-1', low_memory=False)
    indel_data = pd.read_csv('/mnt/data/B26.indel.annot.csv', encoding='ISO-8859-1', low_memory=False)
    
    # Display basic information about each dataset to ensure they loaded correctly
    print("SNP Data Info:")
    print(snp_data.info())
    print("\nIndel Data Info:")
    print(indel_data.info())
    
    # Display the first few rows of each dataset
    print("\nSNP Data Head:")
    print(snp_data.head())
    print("\nIndel Data Head:")
    print(indel_data.head())
    
    # Merge the datasets
    merged_variants = pd.concat([snp_data, indel_data], axis=0)
    
    # Save the merged dataset to a new CSV file
    merged_variants.to_csv('/mnt/data/merged_variants.csv', index=False)
    
    # Load and display the first few rows of the merged dataset to verify
    merged_variants = pd.read_csv('/mnt/data/merged_variants.csv', encoding='ISO-8859-1', low_memory=False)
    print("\nMerged Variants Head:")
    print(merged_variants.head())

except Exception as e:
    print(f"Error: {e}")

# Code for cleaning the dataset by removing least significant results

# Load the merged dataset with low_memory=False to optimize memory usage
try:
    merged_variants = pd.read_csv('/mnt/data/merged_variants.csv', encoding='ISO-8859-1', low_memory=False)
    
    # Display basic information about the merged dataset
    print("Merged Variants Info:")
    print(merged_variants.info())
    
    # Check for missing values
    missing_values = merged_variants.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    # Handle missing values:
    # - Drop columns with more than 50% missing values
    threshold = len(merged_variants) * 0.5
    cleaned_data = merged_variants.dropna(thresh=threshold, axis=1)
    
    # - For remaining missing values, fill numerical columns with the median and categorical columns with the mode
    for column in cleaned_data.columns:
        if cleaned_data[column].dtype in ['float64', 'int64']:
            cleaned_data[column].fillna(cleaned_data[column].median(), inplace=True)
        else:
            cleaned_data[column].fillna(cleaned_data[column].mode()[0], inplace=True)
    
    # Save the cleaned dataset to a new CSV file
    cleaned_data.to_csv('/mnt/data/cleaned_merged_variants.csv', index=False)
    
    # Display basic information about the cleaned dataset
    print("\nCleaned Merged Variants Info:")
    print(cleaned_data.info())

except Exception as e:
    print(f"Error: {e}")


# Filter Most significant genes

# Step 1: Read the data from the uploaded CSV file
input_file = '/mnt/data/cleaned_merged_variant.csv'  # This should match the uploaded file path
df = pd.read_csv(input_file)

# Define the priority for impact levels
impact_priority = {
    'HIGH': 1,
    'MODERATE': 2,
    'LOW': 3,
    'MODIFIER': 4
}

# Step 2: Create a column for impact priority
df['ImpactPriority'] = df['Impact'].map(impact_priority)

# Find the minimum impact priority (most significant)
min_impact_priority = df['ImpactPriority'].min()

# Select all variants with the most significant impact priority
most_significant_variants = df[df['ImpactPriority'] == min_impact_priority]

# Step 3: Save the results to a new CSV file
output_file = '/mnt/data/most_significant_variants.csv'
most_significant_variants.to_csv(output_file, index=False)

print(f"All most significant variants have been saved to {output_file}")
