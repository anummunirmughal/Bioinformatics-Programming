#filter variants in coding regions only

filtered_variants = []

with open("vep_output.txt", "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        # Ensure the line has the minimum required number of fields
        if len(fields) < 8:
            # Skip lines with fewer fields than expected
            continue
        
        genomic_location = fields[0] + ":" + fields[1]
        annotation = fields[7]
        if "coding_sequence_variant" in annotation or "exon_variant" in annotation:
            # Variant is within protein-coding regions
            filtered_variants.append(line)
        elif "INTRONIC" not in annotation and "UTR" not in annotation and "DOWNSTREAM" not in annotation and "UPSTREAM" not in annotation and "INTERGENIC" not in annotation:
            # Variant is not in non-coding or intergenic regions
            filtered_variants.append(line)

# Write filtered variants to a new file
with open("filtered_vep_output.txt", "w") as f:
    f.writelines(filtered_variants)


# filter variants with moderate or high impact only

deleterious_variants = []

with open("filtered_vep_output.txt", "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        # Ensure the line has the minimum required number of fields
        if len(fields) < 8:
            # Skip lines with fewer fields than expected
            continue
        
        # Extract the annotation field
        impact_annotation = fields[4]
        
        # Check if the variant is predicted to have a moderate impact
        if "MODERATE" in impact_annotation:
            # Add the line containing the variant to the list
            deleterious_variants.append(line)

# Write the deleterious variants to a new file
with open("moderate_impact_variants.txt", "w") as f:
    f.writelines(deleterious_variants)

# filter deleterious mutations from moderate impact mutations.
deleterious_variants = []

with open("moderate_impact_variants.txt", "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        # Ensure the line has the minimum required number of fields
        if len(fields) < 32:
            # Skip lines with fewer fields than expected
            continue
        
        # Extract the annotation field
        annotation = fields[31]  # Assuming "deleterious" is in the 32nd column
        
        # Check if the variant is predicted to be deleterious
        if "deleterious" in annotation:
            # Add the line containing the variant to the list
            deleterious_variants.append(line)

# Write the deleterious variants to a new file
with open("deleterious_moderate_impact_variants.txt", "w") as f:
    f.writelines(deleterious_variants)

# find possibly damaging mutations from these deleterious mutations.
filtered_variants = []

with open("deleterious_moderate_impact_variants.txt", "r") as f:
    for line in f:
        fields = line.strip().split("\t")
        # Ensure the line has the minimum required number of fields
        if len(fields) < 33:
            # Skip lines with fewer fields than expected
            continue
        
        # Extract the annotation field
        annotation = fields[32]  # Assuming "probably damaging" or "possibly damaging" is in the 33rd column
        
        # Check if the variant is predicted to be probably damaging or possibly damaging
        if "probably_damaging" in annotation or "possibly_damaging" in annotation:
            # Add the line containing the variant to the list
            filtered_variants.append(line)

# Write the filtered variants to a new file
with open("filtered_deleterious_moderate_impact_variants.txt", "w") as f:
    f.writelines(filtered_variants)