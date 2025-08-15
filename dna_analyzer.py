# DNA Sequence Analyzer (all in one file)

from Bio.Seq import Seq
import matplotlib.pyplot as plt

# Example DNA sequence
seq = Seq("ATGCGTACGTTAGCTAGCTAGCGTATGCTAGCTAGCGATCGATGCTAG")

print("Sequence:", seq)

# Length and GC content
print("Length:", len(seq))
gc_content = 100 * float(seq.count("G") + seq.count("C")) / len(seq)
print("GC content:", round(gc_content, 2), "%")

# Reverse complement
print("Reverse complement:", seq.reverse_complement())

# Find motif positions
motif = "ATG"
positions = [i for i in range(len(seq)) if seq[i:i+len(motif)] == motif]
print(f"Positions of {motif}:", positions)

# Nucleotide distribution plot
nts = ["A", "T", "G", "C"]
counts = [seq.count(nt) for nt in nts]
plt.bar(nts, counts, color=['skyblue','orange','green','red'])
plt.title("Nucleotide Distribution")
plt.show()
