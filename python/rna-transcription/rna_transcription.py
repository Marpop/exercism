def to_rna(dna_strand):
    rna = list(dna_strand)
    for index, nucleotid in enumerate(rna):
        if nucleotid == 'C':
            rna[index] = 'G'
            continue
        if nucleotid == 'G':
            rna[index] = 'C'
            continue
        if nucleotid == 'T':
            rna[index] = 'A'
            continue
        if nucleotid == 'A':
            rna[index] = 'U'
            continue
        else:
            raise ValueError
    rna = ''.join(rna)
    return rna
