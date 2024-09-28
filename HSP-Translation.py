import time

# How translation works, code flow diagram [Harman, Shaan, Prigorian].

def translation(mrna_sequence):
    # 1. start
    print("Start")
    time.sleep(1) # Wait

    # 2. ribosome binds to mRNA
    print("Ribosome binds to mRNA")
    time.sleep(1) # Wait

    # 3. tRNA with start codon anticodon binds
    print("tRNA with start codon anticodon binds")
    time.sleep(1) # Wait

    # initialize variables for reading the mRNA
    amino_acid_chain = ""
    position = 0

    while position < len(mrna_sequence):
        # 4. codon recognized?
        codon = mrna_sequence[position:position + 3]
        if not is_codon_valid(codon):
            print("Codon not recognized, stopping translation.")
            break
        
        print(f"Codon recognized: {codon}")
        time.sleep(1) # Wait

        # 5. amino acid added to chain
        amino_acid = get_amino_acid(codon)
        amino_acid_chain += amino_acid
        print(f"Amino acid '{amino_acid}' added to chain")
        time.sleep(1) # Wait

        # 6. stop codon reached?
        if is_stop_codon(codon):
            print("Stop codon reached, stopping translation")
            break
        
        # 7. move to next codon
        position += 3

    # 8. protein released
    print(f"Protein released: {amino_acid_chain}")
    time.sleep(1) # Wait

    # 9. end
    print("End of translation")
    return amino_acid_chain




# helpers
def is_codon_valid(codon):
    # check if codon is a valid triplet (basic check for length)
    return len(codon) == 3

def get_amino_acid(codon):
    # Simplified mapping of codons to amino acids
    codon_to_amino_acid = {
        'AUG': 'Methionine',  # Start codon
        'UAA': '',            # Stop codon
        'UAG': '',            # Stop codon
        'UGA': '',            # Stop codon
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        # it can be endless, i put this much for now
    }
    return codon_to_amino_acid.get(codon, 'Unknown Amino Acid')

def is_stop_codon(codon):
    # check if codon is stop codon
    return codon in ['UAA', 'UAG', 'UGA']




# variables
mrna_sequence = input("Enter the mRNA sequence (e.g., AUGUUUAA): ")
translated_protein = translation(mrna_sequence)
