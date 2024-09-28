import time

# How transcription works, code flow diagram [Harman, Shaan, Prigorian].

def transcription(dna_sequence):
    # 1. Start: double stranded DNA
    print("Start: double stranded DNA")
    time.sleep(1)  # Wait 

    # 2. RNA polymerase binds to the promoter region
    promoter_region = find_promoter_region(dna_sequence)
    print(f"RNA polymerase binds to promoter region at position {promoter_region}")
    time.sleep(1)  # Wait 

    # 3. DNA double helix unwinds
    unwound_dna = unwind_dna(dna_sequence)
    print("DNA double helix unwinds")
    time.sleep(1)  # Wait

    # initialize variables for reading the template strand
    rna_sequence = ""
    template_strand = unwound_dna['template']

    # 4-6. RNA polymerase reads the template strand and adds complementary nucleotides
    position = 0
    while position < len(template_strand):
        nucleotide = template_strand[position]
        rna_nucleotide = add_complementary_rna_nucleotide(nucleotide)
        rna_sequence += rna_nucleotide
        print(f"RNA polymerase adds {rna_nucleotide} to RNA sequence")
        time.sleep(1)  # Wait 
        
        # check for termination sequence
        if check_termination_sequence(rna_sequence):
            print("Termination sequence found, stopping transcription")
            time.sleep(1)  # wait 
            break
        position += 1

    # 7. RNA polymerase releases
    print("RNA polymerase releases")
    time.sleep(1)  # wait 

    # 8. Pre-mRNA is formed
    pre_mrna = rna_sequence
    print(f"Pre-mRNA formed: {pre_mrna}")
    time.sleep(1)  # wait 

    # 9. post-transcriptional modifications
    mature_mrna = post_transcriptional_modifications(pre_mrna)
    print(f"Mature mRNA: {mature_mrna}")
    time.sleep(1)  # wait 

    # 10. End: mRNA ready for translation
    print("End: mRNA ready for translation")
    time.sleep(1)  # wait 
    return mature_mrna



# helpers
def find_promoter_region(dna_sequence):
    return 0  # assume promoter is at position 0, just for simplicity

def unwind_dna(dna_sequence):
    # simplified unwinding of DNA 
    return {'template': dna_sequence[::-1], 'coding': dna_sequence} 

def add_complementary_rna_nucleotide(dna_nucleotide):
    # DNA to RNA complementary nucleotide map
    complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complement[dna_nucleotide]

def check_termination_sequence(rna_sequence):
    # terminates after these sequences
    termination_sequences = ["UAA", "UAG", "UGA"]
    return any(rna_sequence.endswith(seq) for seq in termination_sequences)

def post_transcriptional_modifications(pre_mrna):
    # simplified 5' capping, 3' poly-A tail, and splicing
    return "5'-Cap-" + pre_mrna + "-Poly-A"



# variables
dna_sequence = input("Enter the DNA sequence, for example, ATGCGTACGCTAGCTTACGTA: \n\n\n ")
mature_mrna = transcription(dna_sequence)