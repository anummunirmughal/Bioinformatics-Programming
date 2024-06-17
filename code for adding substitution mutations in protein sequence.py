def replace_amino_acid(protein_sequence, index, new_amino_acid):
    if index < 0 or index >= len(protein_sequence):
        print("Index out of range.")
        return protein_sequence
    else:
        new_protein_sequence = list(protein_sequence)
        print("Amino acid at index", index, "is:", protein_sequence[index])
        new_protein_sequence[index] = new_amino_acid
        return ''.join(new_protein_sequence)

def main():
    protein_sequence = input("Enter the protein sequence: ")
    index = int(input("Enter the index number where you want to replace the amino acid: "))
    if index < 0:
        print("Index should be a non-negative integer.")
        return
    elif index >= len(protein_sequence):
        print("Index is out of range for the provided protein sequence.")
        return
    
    current_amino_acid = protein_sequence[index]
    print("Current amino acid at index", index, "is:", current_amino_acid)
    
    new_amino_acid = input("Enter the new amino acid: ")
    
    modified_sequence = replace_amino_acid(protein_sequence, index, new_amino_acid)
    print("Modified protein sequence:", modified_sequence)

if __name__ == "__main__":
    main()
